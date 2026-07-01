---
name: search
description: Fast vault search using Obsidian CLI's native search index. Triggered by /search <query>, or natural-language "search my wiki for X", "find pages mentioning Y", "what files talk about Z", "show me backlinks to X", "list pages tagged #foo". For deep synthesis and multi-page answers, use /query instead. Requires Obsidian to be running with the vault open.
user-invocable: true
---

# search skill

## Goal

Fast, vault-aware search using Obsidian's native search index. Returns file lists, context snippets, backlinks, and tag info instantly. Complements `/query` — search is for fast lookups, query is for deep synthesis.

## Trigger scenarios

- `/search <query>`
- Natural-language: "search my wiki for X", "find pages about Y", "what files mention Z"
- "show backlinks to PageName"
- "list pages tagged #foo", "what tags are in my vault"
- "find all sources from 2026-06"

## Prerequisites

Obsidian must be running with the vault open. The CLI path is:

```
C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com
```

If Obsidian isn't running, launch it first:

```powershell
Start-Process "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.exe" -ArgumentList "obsidian://open?vault=ObsidianVault"
```

Wait 3-5 seconds for the vault to load, then proceed.

## Commands

All commands run via `& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" <command> <options>`.

### Step 1: Full-text search

For a text query, run:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" search query="<query>" path="wiki/" limit=15 format=json
```

- `path="wiki/"` scopes to the wiki directory only (skip raw/, .claude/, etc.)
- `limit=15` returns up to 15 matching files
- `format=json` gives clean machine-parseable output

If the user wants context around matches, use `search:context` instead:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" search:context query="<query>" path="wiki/" limit=10
```

For case-sensitive search, add `case`:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" search query="MCP" path="wiki/" limit=10 case
```

### Step 2: Tag search

List all tags in the vault:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" tags counts sort=count
```

Find pages with a specific tag:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" tag name="mcp" verbose
```

### Step 3: Backlinks

Find all pages linking to a specific page:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" backlinks path="wiki/concepts/MCP.md"
```

Or by file name (wikilink-style resolution):

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" backlinks file="MCP"
```

### Step 4: File listing

List files in a folder:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" files folder="wiki/concepts/" ext="md"
```

Count files:

```powershell
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" files folder="wiki/" ext="md" total
```

### Step 5: Orphans and unresolved links

```powershell
# Pages with no incoming links
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" orphans

# Wikilinks pointing to non-existent pages
& "C:\Users\hfeng1\AppData\Local\Programs\Obsidian\Obsidian.com" unresolved
```

## Output format

Present results as a structured list:

```markdown
## Search: "<query>" — N results

| # | File | Context |
|---|------|---------|
| 1 | PageName | snippet showing the match... |
| 2 | [[OtherPage]] | another match snippet... |

**Top tags**: #mcp (12), #agents (8), #eval (5)
```

For backlinks:

```markdown
## Backlinks to PageName — N pages

- [[LinkingPage1]]
- [[LinkingPage2]]
```

## Comparison with /query

| | /search | /query |
|---|---|---|
| Speed | Instant (Obsidian index) | Slower (reads full pages) |
| Depth | File names + snippets | Full synthesis with citations |
| Use for | "Where did I mention X?" | "What do I know about X?" |
| Backlinks | Yes | Manual |
| Tags | Yes | Manual |
| Requires Obsidian | Yes | No |

## Hard rules

- **Check Obsidian is running first.** If the CLI returns an error, remind the user to open Obsidian.
- **Scope to `wiki/`** by default. Only search `raw/` if the user explicitly asks.
- **Use `format=json`** for `search` to get clean, parseable output.
- **Use `search:context`** when the user wants to see surrounding text, not just file names.
- **Don't replace `/query`.** This skill is for fast lookups. If the user asks a substantive question ("what does my wiki conclude about MCP?"), suggest `/query` instead.
- **Present results clearly.** Use a table when there are multiple results, or inline snippets for small result sets.

## Related

- [[.claude/skills/query/SKILL.md]] — deep synthesis skill
- [[.claude/skills/lint/SKILL.md]] — wiki health audit
- `CLAUDE.md` — wiki schema
