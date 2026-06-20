---
title: "Obsidian"
type: entity
tags: [tool, knowledge-management, markdown, second-brain, vault, plugins]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260302 - Build BEAUTIFUL Diagrams with Claude Code (Full Workflow).md"
last_updated: 2026-06-20
---

## Definition

Obsidian is a local, markdown-based personal knowledge management application. Every note is a plain `.md` file on the filesystem — Obsidian renders, links, and visualizes them with a graph view, backlinks, plugins, and themes. It's [[ColeMedin]]'s "canvas" for his [[SecondBrain]] system, paired with [[ClaudeCode]] as the agent and [[ClaudeSkills]] as the capability layer. **It's the application the wiki this knowledge base lives in is built for.**

## Key Information

### Why Obsidian beats Notion / Roam / Logseq for AI-agent integration

The decisive feature: **Obsidian *is* the filesystem.** No abstraction, no API, no MCP server required. A folder of markdown files works equally well from Obsidian's UI, from [[ClaudeCode]]'s file operations, from `git`, from your editor of choice. By contrast:

- **Notion** — content lives in Notion's cloud; agent access requires an MCP server (with all the [[ContextRot]] overhead [[ClaudeSkills]] avoid).
- **Roam / Logseq** — also DB-backed; markdown export exists but isn't the source of truth.

For agent integration, "the source of truth is markdown on disk" is a substantial advantage.

### Features that matter for agent-driven knowledge management

| Feature | Role |
|---|---|
| **Wiki-style links** `[[Page Name]]` | Bidirectional linking; the agent can author them with no special syntax |
| **Graph view** | Human-side overview of the wiki structure; reveals orphans and clusters |
| **YAML frontmatter** | Per-page metadata the agent can read and write |
| **Plugins** | Community ecosystem (Dataview, Excalidraw, etc.) |
| **Local-first** | No vendor lock-in; the markdown is yours forever |
| **Vault portability** | Sync via iCloud/Dropbox/Git; same vault on multiple machines |

### Plugins relevant to this wiki

- **Realclaudian (Claudian)** — embeds Claude Code as a panel inside Obsidian. The agent operating *this very wiki*.
- **Lean Terminal** — shell access without leaving Obsidian.
- **Obsidian Git** — commit/push/pull from inside the app.
- **Excalidraw** — diagrams that render in Obsidian; [[Excalidraw]] is JSON-based, and Cole has a [[ClaudeSkills|skill]] that generates and self-validates them (`summary-beautiful-diagrams-claude-code`).
- **Dataview** — query frontmatter as if the vault were a database.
- **Marp** — render markdown as slides (mentioned by Karpathy as part of the LLM Wiki pattern).

### Workflow with [[ClaudeCode]]

1. Open the vault in Obsidian (browse, read, link, curate).
2. Open a terminal in the vault root (Cole uses Lean Terminal inside Obsidian).
3. Run [[ClaudeCode]] from that terminal.
4. The agent has filesystem access to the entire vault — reads notes, writes new ones, refactors links.
5. Obsidian's UI updates live as the agent writes.

The combination is **cooperative editing**: human and agent are both editors of the same markdown directory, with their own optimal interfaces.

### Limitations / things to know

- **Embedded images** — Obsidian uses `![[image.png]]` for embeds. The agent can write these, but reading images requires a separate step (image is binary; markdown text alone isn't enough).
- **Plugin source bloat** — many plugins ship megabytes of bundled JS. If you commit `.obsidian/plugins/` to git, the repo grows. (See `.gitignore` strategy in this vault.)
- **Workspace state** — `.obsidian/workspace.json` changes every click; gitignore it.
- **No built-in collaboration** — Obsidian is single-user by design. Multi-user requires Obsidian Sync or the Git plugin + manual coordination.

### Connection to the [[KarpathyLLMWiki]] pattern

[[AndrejKarpathy]]'s framing of an LLM-maintained personal Wiki essentially specifies "markdown on the filesystem with bidirectional links." Obsidian is the application that already implemented exactly this, before LLMs needed it. The pairing is natural: Karpathy's pattern + Obsidian's UI = the wiki you're reading right now.

## Related

- [[ClaudeCode]] — primary agent operating against the vault
- [[Excalidraw]] — diagram format rendered via the Obsidian plugin
- [[ClaudeSkills]] — capability layer
- [[SecondBrain]] — central pattern using Obsidian as canvas
- [[KarpathyLLMWiki]] — the pattern Obsidian naturally hosts
- [[ColeMedin]] — primary advocate in this corpus
- [[summary-second-brain-with-claude-code-obsidian-skills]] — primary source
- [[summary-beautiful-diagrams-claude-code]] — Excalidraw plugin as a diagram render target
