---
name: ingest
description: Compile raw material into the wiki. Reads files from raw/ (excluding raw/05-vtts/), extracts entities and concepts, creates/updates wiki pages with bidirectional links, registers them in wiki/index.md, and appends to wiki/log.md. Raw files are never moved — a source counts as processed when its mirrored summary exists under wiki/sources/. Triggered by /ingest (scan all un-summarized raw files), /ingest <path> (process a specific file), or natural-language requests like "ingest this article", "import this into my knowledge base", "add this to the wiki".
user-invocable: true
---

# ingest skill

## Core workflow: inbox → compiled, no archiving

You are maintaining an LLM Wiki (Obsidian knowledge base). `raw/` is the inbox; `wiki/` is the compiled output layer.

**Raw files are immutable and stay in place forever — never moved, never archived.** A raw file is "already processed" when its **mirrored summary** exists under `wiki/sources/` (see the path scheme in Step 3). The link between a summary and its source is therefore deterministic and reversible by path alone, and the `sources:` frontmatter stays valid permanently.

**Directory map:**
- `raw/01-articles/` — web clippings (markdown)
- `raw/02-papers/` — PDFs and academic papers
- `raw/03-transcripts/` — video/podcast transcripts (markdown)
- `raw/04-meeting_notes/` — meeting notes, brainstorming
- `raw/05-vtts/` — **raw WebVTT subtitle inputs. Never ingest these.** They are upstream artifacts used to *generate* the markdown transcripts in `raw/03-transcripts/`. Ignore the entire folder during scans.
- `wiki/sources/` — one summary per raw file, **mirroring the raw subpath** (see Step 3)
- `wiki/entities/` — people, companies, tools, products (TitleCase)
- `wiki/concepts/` — frameworks, methodologies, theories (TitleCase)

**Ingestable sources are markdown/PDF content files only.** When scanning, skip:
- The entire `raw/05-vtts/` tree (input artifacts, not content).
- `.vtt` files anywhere.
- Dotfiles and bookkeeping files (e.g. `.keep`, `.download_archive.txt`, anything starting with `.`).
- Any non-source extension (only `.md` and `.pdf` are ingestable).

**Detecting what's already processed (replaces the old archive marker):** a raw file is already compiled iff its **mirrored summary** exists under `wiki/sources/` (path rule in Step 3). To list un-summarized sources, compute each candidate's mirrored summary path and check whether that file exists on disk.

## Trigger logic

1. **`/ingest`** — scan all subdirectories of `raw/` (excluding `05-vtts/`), find raw `.md`/`.pdf` files whose mirrored summary does **not** yet exist. If multiple are found, list them and ask the user which to process (or confirm batch processing).
2. **`/ingest <path>`** — process the specific file at `<path>`.
3. **Implicit trigger** — when the user says "ingest this", "import this into my wiki", "add this article to the knowledge base", or similar, run the ingest pipeline on the named or current file.

### Batch processing

When the user confirms processing multiple files in one run:
- **De-duplicate first.** If the same source appears in more than one form (e.g. a transcript and its subtitle twin), keep only the canonical .md/.pdf content file and drop the rest. Never compile the same underlying source twice.
- **Process oldest-first** (by filename date prefix where present) so the wiki accretes in chronological order.
- **Use parallel workers for content creation (Steps 1–4 only).** Each file gets its own subagent that reads the source, extracts entities/concepts, creates the mirrored source summary, and creates/updates entity and concept pages. Workers must **never** touch index.md or log.md — those are shared state edited in the consolidation step below. For entity/concept pages, workers may safely read and write their own pages in parallel since each entity/concept page is a distinct file.
- **A conflict pauses the whole batch.** If Step 4 hits a conflict on any file, the worker stops, reports it, and the orchestrator waits for the user's decision before resuming the remaining files (see Conflict handling). Already-completed files stay done; the rest wait.
- **Consolidate registries after the batch (Steps 5–6 once).** After all workers finish, a single sequential process updates index.md and log.md once for the entire batch. This eliminates race conditions on shared state.

#### Batch orchestration protocol

1. **Dispatch workers in parallel** — one subagent per file. Each worker executes Steps 1–4 only. Workers create source summaries, entity pages, and concept pages. Workers must NOT read or write wiki/index.md or wiki/log.md.
2. **Collect results** — wait for all workers to finish. Gather the list of created/updated pages from each worker's summary.
3. **Run consolidation** — a single sequential process:
   a. Read wiki/index.md once.
   b. Add every new source summary, entity, and concept entry to the appropriate section. Check for duplicates (parallel workers may have created the same entity/concept pages — pick one entry per page).
   c. Write wiki/index.md once.
   d. Append one log entry per ingested file to wiki/log.md.
4. **Summarize at the end**: list which files were ingested, total pages created/updated, any conflicts that paused, and any workers that failed.


## Compilation pipeline

For each source file, execute these steps strictly in order:

### Step 1: Read the source

- `.md` files: read the full content.
- `.pdf` files: attempt text extraction with available tools. If extraction fails or returns empty, record file metadata only (filename, page count if known) and note in the source summary that body text wasn't extractable.
- If a referenced image in a markdown source is critical to understanding, read it separately.
- **Media handling:** if an image (or other attachment) is worth preserving in the wiki, copy it into `assets/` and reference it from the wiki page with an Obsidian embed: `![[filename.png]]`. Never hotlink an external URL as the permanent reference, and never store the wiki's asset copy inside `raw/` (raw is the immutable source layer). Keep a descriptive filename.

### Step 2: Extract & translate

From the source, identify:
- **Core thesis** — what is this material fundamentally about? (1–2 sentences)
- **Entities** — concrete nouns: people, companies, tools, products, projects.
- **Concepts** — abstract nouns: frameworks, methodologies, theories, patterns.

If the source is in a non-English language, translate to English. Preserve original-language proper nouns and key terminology in parentheses where helpful.

### Step 3: Create the source summary (mirrored path)

The summary **mirrors the raw file's path** so the two are linked deterministically and reversibly, with no archiving:

- **Mirror the raw subpath** under `wiki/sources/`, and name the file `summary-` + the raw file's exact basename. The summary is always a markdown file.
- Markdown source → keep the basename as-is (it already ends in `.md`):
  - `raw/03-transcripts/Cole Medin/Channel Only/20260101 - AI Exploded.md`
  - → `wiki/sources/03-transcripts/Cole Medin/Channel Only/summary-20260101 - AI Exploded.md`
- PDF (or other) source → keep the full basename and append `.md` (so the summary stays markdown):
  - `raw/02-papers/building-effective-agents.pdf`
  - → `wiki/sources/02-papers/summary-building-effective-agents.pdf.md`
- **Reverse lookup** (summary → raw): strip the `wiki/sources/` prefix and the `summary-` filename prefix, drop a trailing `.md` only if it was appended to a non-`.md` source, then prepend `raw/`.
- Preserve the original (possibly non-ASCII) characters in the basename exactly — do not re-slugify. Spaces, fullwidth colons (`：`), curly quotes, etc. are fine and **must match the raw filename byte-for-byte** so the mapping holds.
- Create any mirrored subdirectories under `wiki/sources/` as needed.

```markdown
---
title: "summary-{raw-basename}"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260101 - AI Exploded.md"]
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

- [[summary-{raw-basename}]] — source summary
- [[OtherEntity]] — related entity
- [[OtherConcept]] — related concept
```

### Step 5: Update global registries

**`wiki/index.md`:** add the new page(s) under the correct category, in `[[PageName]] — one-sentence description.` format.

**`wiki/log.md`:** append (do not edit existing entries):

```markdown
## [YYYY-MM-DD] ingest | <one-line summary of the source>
- **Changes**: created [[summary-{raw-basename}]], created [[NewEntity]], updated [[ExistingConcept]], updated [[index.md]]
- **Conflicts**: none
```

If conflicts were paused on, note: `**Conflicts**: paused on [[ConflictPage]] — awaiting user decision`.

### Step 6: Finalize (no archiving)

**Do not move or modify the raw file — ever.** It stays in place permanently. The existence of the mirrored summary at `wiki/sources/<subpath>/summary-<basename>` is itself the "processed" marker, so no archive is needed.

Before considering the source done, confirm **all** of:
- Mirrored source summary created in `wiki/sources/` (correct mirrored path; `sources:` points to the real raw path).
- All entity/concept pages created or updated.
- `wiki/index.md` updated.
- `wiki/log.md` updated.

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
4. **Continue** based on the choice. If A, add the conflict block. If B, update and note the supersession in the source citation. If C, leave the wiki unchanged and don't create the summary (so the source remains un-processed and will resurface on the next scan).

## Hard rules

- **Never move or modify a `raw/` file.** Raw is strictly read-only and immutable; there is no archive. "Processed" = the mirrored summary exists under `wiki/sources/`.
- Source summaries mirror the raw subpath: `wiki/sources/<subpath>/summary-<raw-basename>` (markdown summary; reversible to the raw path by construction). The `sources:` frontmatter must match the real raw filename byte-for-byte.
- Every wiki page must have a `## Related` section. No orphans.
- All wiki content is in English. Translate non-English sources.
- Entity & concept filenames: `TitleCase.md`. Synthesis filenames: `kebab-case.md`.
- Always update `index.md` and `log.md` after any wiki mutation.
- **Use the real current date** for every `last_updated` field and log entry — read it from the injected current-date context or run `date +%F`. Never guess or copy the `YYYY-MM-DD` placeholder literally.
