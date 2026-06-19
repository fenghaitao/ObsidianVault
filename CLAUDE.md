# LLM Wiki — Schema & Rules

You are maintaining an **LLM Wiki** ([Karpathy's pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)). Your job is to compile fragmented information into a structured, heavily cross-linked Obsidian knowledge base.

## Language

Always write all wiki content in **English**. If a source is in another language, translate it to English when ingesting. You may quote short original-language excerpts when faithful preservation matters (proper nouns, terminology), but every page body is English.

## Directory layout & permissions

These permissions are non-negotiable.

- **`/raw/`** — Immutable source layer.
  - **Read-only.** Never modify, rewrite, or paraphrase files in `raw/`.
  - The only allowed mutation is **moving** a fully-processed file to `raw/09-archive/` at the end of an `ingest` run.
  - This is the single source of truth.

- **`/assets/`** — Media (images, PDFs, attachments). Reference with Obsidian wikilink embed: `![[filename.png]]`.

- **`/wiki/`** — Compiled output layer. **You own this directory.** Create, update, refine, and resolve contradictions here.

- **`/raw/09-archive/`** — Processed-file archive. **Never read from this directory** during normal operations; it exists purely so `ingest` knows what's already been compiled.

## Wiki schema

When working in `/wiki/`, you must maintain these foundations:

### 1. `wiki/index.md` — global directory

After adding any new wiki page, append it to `index.md` under the right category.

Format: `[[Page Name]] — one-sentence description.`

- **Entities / Concepts** — `TitleCase` filenames (e.g. `ClaudeCode.md`, `RetrievalAugmentedGeneration.md`)
- **Sources / Syntheses** — `kebab-case` filenames (e.g. `summary-karpathy-llm-wiki.md`, `analysis-rag-vs-wiki.md`)

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
| `wiki/sources/` | One-to-one summaries of `raw/` files | `summary-{slug}.md` (kebab-case) |
| `wiki/syntheses/` | Cross-document analyses, comparisons, deep dives | `{slug}.md` (kebab-case) |

### 4. Mandatory bidirectional linking

Every wiki page **must** include a `## Related` section using Obsidian wikilinks `[[Page Name]]` to connect it to other pages. **No orphan pages.** A page with no inbound or outbound links is a bug to be fixed by `lint`.

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

- **`/ingest <path>`** — Read a `raw/` file, distill its core value, integrate into relevant `wiki/` concept/entity pages, create a source summary, update index and log, then archive the source. See `.claude/skills/ingest/SKILL.md`.

- **`/query <question>`** — Read `wiki/index.md` to locate relevant pages, deep-read them, synthesize an answer with `[[wikilink]]` citations. Optionally save high-value answers as a synthesis page. See `.claude/skills/query/SKILL.md`.

- **`/lint`** — Scan `wiki/` for orphan pages, dead links, unsynced index entries, unresolved conflicts. Produce a structured report. See `.claude/skills/lint/SKILL.md`.

## Reading raw files

- `.md` files: read directly.
- `.pdf` files: attempt text extraction; if not possible, record file metadata (filename, page count) in the source summary and note that body text wasn't extracted.
- Embedded images in markdown: read the markdown text first; view referenced images separately if visual context is needed.

## Hard rules

- **Never modify `raw/` files.** Read-only except for the archive move.
- **Never read `raw/09-archive/`** during normal operations.
- **Never create orphan pages.** Every page links somewhere.
- **Never silently resolve conflicts.** Surface them.
- **Never invent citations.** If a claim isn't in the source files, mark it as inferred or omit it.
- **Always update `index.md` and `log.md`** after any wiki mutation.
