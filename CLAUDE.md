# LLM Wiki — Schema & Rules

You are maintaining an **LLM Wiki** ([Karpathy's pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). Your job is to compile fragmented information into a structured, heavily cross-linked Obsidian knowledge base.

## Language

Always write all wiki content in **English**. If a source is in another language, translate it to English when ingesting. You may quote short original-language excerpts when faithful preservation matters (proper nouns, terminology), but every page body is English.

## Directory layout & permissions

These permissions are non-negotiable.

- **`/raw/`** — Immutable source layer.
  - **Strictly read-only.** Never modify, rewrite, paraphrase, **move, rename, or delete** files in `raw/`. There is no archive; raw files stay in place permanently.
  - A raw file counts as **processed** when its mirrored summary exists under `wiki/sources/` (see §3), not by being moved.
  - This is the single source of truth.

- **`/assets/`** — Media (images, PDFs, attachments). Reference with Obsidian wikilink embed: `![[filename.png]]`.

- **`/wiki/`** — Compiled output layer. **You own this directory.** Create, update, refine, and resolve contradictions here.

- **No archive.** Earlier versions moved processed files to `raw/09-archive/`; this is removed. The link between a source and its summary is now the **mirrored path** (§3) plus the summary's `sources:` frontmatter, which stays valid because raw files never move.

## Wiki schema

When working in `/wiki/`, you must maintain these foundations:

### 1. `wiki/index.md` — global directory

After adding any new wiki page, append it to `index.md` under the right category.

Format: `[[Page Name]] — one-sentence description.`

- **Entities / Concepts** — `TitleCase` filenames (e.g. `ClaudeCode.md`, `RetrievalAugmentedGeneration.md`)
- **Sources** — mirror the raw subpath: `wiki/sources/<subpath>/summary-<raw-basename>` (e.g. `wiki/sources/03-transcripts/Cole Medin/Channel Only/summary-20260101 - AI Exploded.md`)
- **Syntheses** — `kebab-case` filenames (e.g. `analysis-rag-vs-wiki.md`)

Example structure:

```markdown
# Wiki Index

## Sources
- [[summary-karpathy-llm-wiki]] — Karpathy's pattern for LLM-maintained personal knowledge bases.

## Entities
- [[ClaudeCode]] — Anthropic's terminal-based coding agent.

## Concepts
- [[RetrievalAugmentedGeneration]] — Inference-time retrieval pattern; contrasted with persistent compilation.

## Syntheses
- [[analysis-rag-vs-wiki]] — Detailed comparison of RAG and Wiki paradigms.
```

### 2. `wiki/log.md` — operation log

**Append-only.** Every operation appends an entry:

```markdown
## [YYYY-MM-DD] <action> | <one-line summary>
- **Changes**: created [[PageA]], updated [[PageB]], updated [[index.md]]
- **Conflicts**: none (or: conflict on [[PageX]], flagged in `## Knowledge Conflicts` section)
```

Action types: `ingest`, `query`, `lint`, `sync`.

The format is grep-friendly: `grep "^## \[" log.md | tail -10` shows the last 10 operations.

### 3. Content categories

| Folder | Contains | Filename style |
|---|---|---|
| `wiki/concepts/` | Frameworks, methodologies, theories, abstract patterns | `TitleCase.md` |
| `wiki/entities/` | People, companies, tools, products, projects | `TitleCase.md` |
| `wiki/sources/` | One-to-one summaries of `raw/` files | `<raw-subpath>/summary-<raw-basename>` (mirrors raw path) |
| `wiki/syntheses/` | Cross-document analyses, comparisons, deep dives | `{slug}.md` (kebab-case) |

### 4. Mandatory bidirectional linking

Every wiki page **must** include a `## Related` section using Obsidian wikilinks `[[Page Name]]` to connect it to other pages. **No orphan pages.**

**Orphan definition (authoritative — `lint` enforces this):** a page is an orphan if it has **zero inbound links from other content pages**. Registration in `index.md` does **not** count as an inbound link (everything is registered there). So a page needs at least one *content* page pointing to it via `[[...]]`, not just an index entry.

This applies to syntheses too: when `/query` saves a synthesis, it must add a backlink to it from the `## Related` section of a central page it draws from (see the query skill's Step 4b). A synthesis that only links outward — with nothing linking back — is an orphan and a bug.

### 5. Conflict handling

When new material contradicts existing wiki content:
- **Do not silently overwrite.**
- Add a `## Knowledge Conflicts` section to the affected page.
- Present both claims with their source citations.
- During `ingest`, **pause and report** the conflict to the user before continuing.

## Page frontmatter (YAML)

Every wiki page must start with:

```yaml
---
title: "Page Title"
type: concept | entity | source | synthesis
tags: [tag1, tag2]
sources: [raw/01-articles/example.md, raw/02-papers/foo.pdf]
last_updated: YYYY-MM-DD
---
```

- `type` is one of `concept`, `entity`, `source`, `synthesis` — matching the folder.
- `sources` lists relative paths to `raw/` files this page draws from. Empty list `[]` for pure synthesis pages.

## Workflow commands

When asked to perform these operations, follow the corresponding skill in `.claude/skills/`:

- **`/ingest <path>`** — Read a `raw/` file, distill its core value, integrate into relevant `wiki/` concept/entity pages, create a mirrored source summary, and update index and log. The raw file is left in place (no archiving). See `.claude/skills/ingest/SKILL.md`.

- **`/query <question>`** — Read `wiki/index.md` to locate relevant pages, deep-read them, synthesize an answer with `[[wikilink]]` citations. Optionally save high-value answers as a synthesis page. See `.claude/skills/query/SKILL.md`.

- **`/lint`** — Scan `wiki/` for orphan pages, dead links, unsynced index entries, unresolved conflicts. Produce a structured report. See `.claude/skills/lint/SKILL.md`.

## Reading raw files

- `.md` files: read directly.
- `.pdf` files: attempt text extraction; if not possible, record file metadata (filename, page count) in the source summary and note that body text wasn't extracted.
- Embedded images in markdown: read the markdown text first; view referenced images separately if visual context is needed.

## Hard rules

- **Never modify, move, rename, or delete `raw/` files.** Raw is strictly read-only and immutable; there is no archive.
- **A source is "processed" when its mirrored summary exists** under `wiki/sources/` — that is the single dedup signal.
- **Never create orphan pages.** Every page links somewhere.
- **Never silently resolve conflicts.** Surface them.
- **Never invent citations.** If a claim isn't in the source files, mark it as inferred or omit it.
- **Always update `index.md` and `log.md`** after any wiki mutation.
