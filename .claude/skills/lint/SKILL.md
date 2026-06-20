---
name: lint
description: Health check for the wiki knowledge base. Scans wiki/ for dead links (wikilinks pointing to non-existent pages), orphan pages (pages no other page links to), unsynced index (pages that exist on disk but aren't registered in wiki/index.md), and unresolved knowledge conflicts. Triggered by /lint, /scan, /health, or natural-language requests like "check my wiki health", "audit the knowledge base", "find orphans". Read-only by default — produces a structured report and asks the user before applying any fixes.
user-invocable: true
---

# lint skill — wiki health audit

## Goal

Apply software-engineering static analysis to knowledge management. As the wiki grows over weeks and months, it accumulates entropy: dead links from renamed pages, orphan pages no one links to, missing index entries, unresolved conflicts. This skill finds them.

## Trigger conditions

- `/lint`, `/scan`, `/health`
- "Check my wiki health", "audit the knowledge base", "what's the state of my wiki", "find orphans", "find dead links"

## Wiki path resolution

Use the Glob tool to locate the `wiki/` directory in the current working tree. Skip `wiki/index.md` and `wiki/log.md` themselves where appropriate (these are special files, not content pages).

## Audit pipeline

### Step 1: Index consistency

1. Read `wiki/index.md` in full.
2. Extract every `[[Page Name]]` link registered in the index.
3. Use Glob to enumerate every `.md` file in `wiki/` (excluding `index.md` and `log.md`).
4. Cross-check:
   - **Registered but file missing** — entry in `index.md` whose target file doesn't exist on disk. (Stale entries.)
   - **File present but unregistered** — page on disk that doesn't appear in `index.md`. (Index drift.)

### Step 2: Bidirectional link health

1. For every `.md` file in `wiki/`, extract all `[[Wikilink]]` targets in the body.
2. For each target:
   - **Target page does not exist** → flag as **dead link** (record source page → target).
3. Build the inbound-link graph: count how many other **content pages** link to each page.
   - **Exclude `index.md` and `log.md` from the inbound count.** Per `CLAUDE.md`, registration in `index.md` does **not** count as an inbound link (everything is registered there), and `log.md` mentions don't either. A page needs ≥1 inbound link from a real content page (concept/entity/source/synthesis) to not be an orphan.
   - Also exclude self-references (a page linking to itself).
4. Pages with **zero qualifying inbound links** → **orphans**.
   - Be a bit forgiving: a brand-new page added in the last day or two may not have inbound links yet — still flag, but note "recently created".

### Step 3: Cognitive conflict review

1. Search every `.md` file in `wiki/` for an `## Knowledge Conflicts` (or equivalent) section.
2. For each, extract a brief description (which two claims, on which page).
3. Track the count — these are "cognitive technical debt."

### Step 4: Frontmatter sanity (optional, lightweight)

Spot-check a sample of pages for:
- Missing frontmatter or missing required fields (`title`, `type`, `last_updated`).
- `type` mismatched with folder (e.g. `type: source` in `wiki/concepts/`).
- `sources:` referencing paths that don't exist.

Don't exhaustively walk every file unless asked — sample to catch systemic issues.

### Step 5: Filename-convention compliance

Check that filenames match the schema's required style for their folder (`CLAUDE.md` §3):

| Folder | Required filename style | Example |
|---|---|---|
| `wiki/concepts/` | `TitleCase.md` | `RetrievalAugmentedGeneration.md` |
| `wiki/entities/` | `TitleCase.md` | `ClaudeCode.md` |
| `wiki/sources/` | `summary-{slug}.md` (kebab-case) | `summary-karpathy-llm-wiki.md` |
| `wiki/syntheses/` | `{slug}.md` (kebab-case) | `analysis-rag-vs-wiki.md` |

Flag violations as a **yellow** issue (e.g. a source file named `BuildingEffectiveAgents.md` instead of `summary-building-effective-agents.md`, or a concept in kebab-case). Renaming is a fix the user must approve — propose the corrected name, and remember that renaming a page also requires updating every inbound `[[wikilink]]` and its `index.md` entry, so list those downstream edits alongside the rename.

## Report format

Produce the report in this exact structure:

```markdown
## 🩺 Wiki Health Report — YYYY-MM-DD

### ✅ Green
- Total pages: N
- Registered in index: N
- Cross-link density: N links across M pages (avg X per page)
- [Anything else healthy]

### ⚠️ Yellow

- **Orphan pages (N)**: pages with no inbound links.
  - [[OrphanA]] — created YYYY-MM-DD
  - [[OrphanB]] — created YYYY-MM-DD
  - Suggestion: link from a related page or remove if obsolete.

- **Unregistered pages (N)**: pages on disk but missing from `index.md`.
  - [[UnregisteredA]] (wiki/concepts/UnregisteredA.md)
  - Suggestion: I can append these to index.md automatically if you confirm.

- **Frontmatter issues (N)**: pages with missing or inconsistent metadata.
  - [[PageX]] — `type` is `concept` but file is in `wiki/entities/`.

- **Filename-convention violations (N)**: filenames not matching the required style for their folder.
  - `wiki/sources/BuildingEffectiveAgents.md` — should be kebab-case `summary-building-effective-agents.md`.
  - Suggestion: rename + update inbound links and the `index.md` entry (I'll list the downstream edits before applying).

### ❌ Red

- **Dead links (N)**: wikilinks pointing to non-existent pages.
  - [[SourcePage]] → [[MissingTarget]]
  - [[AnotherSource]] → [[AnotherMissing]]
  - Suggestion: create the target page, fix the link, or remove it.

- **Stale index entries (N)**: registered in index.md but file missing.
  - [[GhostPage]] — referenced in index.md, no file on disk.

- **Unresolved conflicts (N)**: pages with `## Knowledge Conflicts` sections.
  - [[ConflictPage]] — claim A vs claim B (brief description).

### 🛠️ Suggested next steps

1. [Specific actionable item, e.g. "fix the 3 dead links by deciding whether each target should exist"]
2. [Specific actionable item, e.g. "merge OrphanA into RelatedPage's `## Related` section"]
3. [Etc.]

Would you like me to apply any of these fixes? I'll list each change before making it and wait for confirmation.
```

## Hard rules

- **Read-only by default.** This skill produces reports. Don't modify, delete, or rename any file before generating the report.
- **Manual confirmation for fixes.** After the report, wait for the user to confirm which fixes to apply. List each intended change before making it.
- **One log entry after fixes.** If fixes are applied, append a single entry to `wiki/log.md`:
  ```markdown
  ## [YYYY-MM-DD] lint | fixed N issues
  - **Changes**: [list specific edits, e.g. "added [[PageA]] to index.md", "removed dead link [[Missing]] from [[PageB]]"]
  ```
- **No silent reorganization.** Don't move files between folders or rename them without explicit user approval.
- **Use the real current date** in the report header and any log entry — read it from the injected current-date context or run `date +%F`. Never copy the `YYYY-MM-DD` placeholder literally.

## Related

- [[wiki/index.md]] — the audit baseline
- [[wiki/log.md]] — where lint runs are recorded
- [[CLAUDE.md]] — schema this audit checks against
