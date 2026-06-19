---
name: ingest
description: Compile raw material into the wiki. Reads files from raw/ (excluding raw/09-archive/), extracts entities and concepts, creates/updates wiki pages with bidirectional links, registers them in wiki/index.md, appends to wiki/log.md, then moves the processed source file to raw/09-archive/. Triggered by /ingest (scan all unarchived raw files), /ingest <path> (process a specific file), or natural-language requests like "ingest this article", "import this into my knowledge base", "add this to the wiki".
user-invocable: true
---

# ingest skill

## Core workflow: inbox → archive

You are maintaining an LLM Wiki (Obsidian knowledge base). `raw/` is the inbox; `wiki/` is the compiled output layer.

**Directory map:**
- `raw/01-articles/` — web clippings (markdown)
- `raw/02-papers/` — PDFs and academic papers
- `raw/03-transcripts/` — video/podcast transcripts
- `raw/04-meeting_notes/` — meeting notes, brainstorming
- `raw/09-archive/` — **already-processed sources. Never read from here.**
- `wiki/sources/` — one summary per raw file (kebab-case filenames)
- `wiki/entities/` — people, companies, tools, products (TitleCase)
- `wiki/concepts/` — frameworks, methodologies, theories (TitleCase)

## Trigger logic

1. **`/ingest`** — scan all subdirectories of `raw/` (excluding `09-archive/`), find unprocessed files. If multiple are found, list them and ask the user which to process (or confirm batch processing).
2. **`/ingest <path>`** — process the specific file at `<path>`.
3. **Implicit trigger** — when the user says "ingest this", "import this into my wiki", "add this article to the knowledge base", or similar, run the ingest pipeline on the named or current file.

## Compilation pipeline

For each source file, execute these steps strictly in order:

### Step 1: Read the source

- `.md` files: read the full content.
- `.pdf` files: attempt text extraction with available tools. If extraction fails or returns empty, record file metadata only (filename, page count if known) and note in the source summary that body text wasn't extractable.
- If a referenced image in a markdown source is critical to understanding, read it separately.

### Step 2: Extract & translate

From the source, identify:
- **Core thesis** — what is this material fundamentally about? (1–2 sentences)
- **Entities** — concrete nouns: people, companies, tools, products, projects.
- **Concepts** — abstract nouns: frameworks, methodologies, theories, patterns.

If the source is in a non-English language, translate to English. Preserve original-language proper nouns and key terminology in parentheses where helpful.

### Step 3: Create the source summary

Create `wiki/sources/summary-{slug}.md`. Slug is kebab-case derived from the filename or title.

```markdown
---
title: "summary-{slug}"
type: source
tags: [source, original-material]
sources: [raw/01-articles/example.md]
last_updated: YYYY-MM-DD
---

## Core Summary

[3–5 sentence distillation of the core thesis and main arguments.]

## Key Points

- [bullet of major claim or finding]
- [bullet of major claim or finding]
- [bullet of major claim or finding]

## Related

- [[EntityName]] — related entity
- [[ConceptName]] — related concept
```

### Step 4: Build the knowledge network (entities & concepts)

For each entity and concept extracted in Step 2:

**Target folder:**
- Entity → `wiki/entities/EntityName.md`
- Concept → `wiki/concepts/ConceptName.md`

**Logic:**
1. **Page does not exist** → create a new page using the template below.
2. **Page already exists** → read it, **incrementally merge** the new information (add bullets, expand sections, add a new source citation). Don't rewrite existing content.
3. **Conflict detected** (new info contradicts existing claim) → **pause immediately**. Report the conflict to the user with both claims and ask how to proceed (see Conflict handling below). Do not write to the page until resolved.

**Page template:**

```markdown
---
title: "PageName"
type: entity | concept
tags: [tag1, tag2]
sources: [raw/01-articles/example.md]
last_updated: YYYY-MM-DD
---

## Definition

[Concise definition of the entity or concept.]

## Key Information

[Detailed information drawn from the source(s). Use bullets, sub-headings, or short paragraphs as appropriate.]

## Related

- [[summary-{slug}]] — source summary
- [[OtherEntity]] — related entity
- [[OtherConcept]] — related concept
```

### Step 5: Update global registries

**`wiki/index.md`:** add the new page(s) under the correct category, in `[[PageName]] — one-sentence description.` format.

**`wiki/log.md`:** append (do not edit existing entries):

```markdown
## [YYYY-MM-DD] ingest | <one-line summary of the source>
- **Changes**: created [[summary-slug]], created [[NewEntity]], updated [[ExistingConcept]], updated [[index.md]]
- **Conflicts**: none
```

If conflicts were paused on, note: `**Conflicts**: paused on [[ConflictPage]] — awaiting user decision`.

### Step 6: Archive the source

Once **all** of the following are confirmed:
- Source summary created in `wiki/sources/`
- All entity/concept pages created or updated
- `wiki/index.md` updated
- `wiki/log.md` updated

…move the source file from its original location to `raw/09-archive/`, preserving the subfolder structure (e.g. `raw/01-articles/foo.md` → `raw/09-archive/01-articles/foo.md`).

**Never modify the contents of the source file.** Only the path changes.

## Conflict handling

When ingestion would contradict existing wiki content:

1. **Pause** — stop the current ingest pipeline.
2. **Report** — tell the user clearly:
   - Which page has the conflict.
   - What the existing claim says (with citation).
   - What the new claim says (with citation).
3. **Ask** the user to choose:
   - **A)** Keep both as a `## Knowledge Conflicts` section on the page (default for genuine debate or evolving understanding).
   - **B)** Replace the old claim with the new one (use when the old was incorrect).
   - **C)** Abort this ingest entirely.
4. **Continue** based on the choice. If A, add the conflict block. If B, update and note the supersession in the source citation. If C, leave wiki unchanged and don't archive.

## Hard rules

- Never read from `raw/09-archive/`.
- Never modify the body of a `raw/` file. Only the move-to-archive operation is allowed.
- Every wiki page must have a `## Related` section. No orphans.
- All wiki content is in English. Translate non-English sources.
- Entity & concept filenames: `TitleCase.md`. Source & synthesis filenames: `kebab-case.md`.
- Always update `index.md` and `log.md` after any wiki mutation.
