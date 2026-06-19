---
title: "SecondBrain"
type: concept
tags: [concept, knowledge-management, claude-code, obsidian, skills, personal-productivity]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"
last_updated: 2026-06-20
---

## Definition

A "Second Brain" in [[ColeMedin]]'s usage is a personal knowledge / ideation / research system using [[ClaudeCode]] as the agent, [[Obsidian]] as the markdown canvas, and [[ClaudeSkills]] as the capability layer. The thesis: a coding agent minus its code-intelligence tool is a powerful general-purpose CLI agent. Pair with a markdown-native knowledge tool (Obsidian) and you get a personal research/ideation/organization engine that scales to dozens of capabilities without context bloat.

> **This concept is the direct philosophical ancestor of the wiki this knowledge base lives in.** The pattern Cole describes here is essentially the [[KarpathyLLMWiki]] pattern (forward-reference, fully described in the batch-C ingest of the `20260406` video) implemented via Claude Code + Obsidian + Skills.

## Key Information

### Full architecture (from the comprehensive guide)

Cole's `summary-full-guide-ai-second-brain` lays out three pillars beyond the basic Claude-Code-+-Obsidian-+-Skills frame:

#### 1. The memory layer (inspired by [[OpenClaw]])

Markdown files loaded at session start via a **session-start hook**:
- `soul.md` — the personality/persona of the second brain.
- `user.md` — facts about the user; evolves over time.
- `memory.md` — key decisions; the single most important file; concise promoted knowledge.
- `daily logs/` — raw dump of every conversation (the `raw/` equivalent), one file per day.

**Promotion process** (daily cron via Claude Agent SDK): extract key decisions / lessons / facts from the long daily log → promote into `memory.md`. RAG over daily logs (SQLite-indexed) for things not promoted but still searchable later. This is the [[KarpathyLLMWiki]] compile loop applied to internal conversation data.

#### 2. Skills = the "arms"

[[ClaudeSkills]] provide all capabilities — Cole uses *no MCP servers* directly, just skills. Skills are *powered by the memory layer*: a generic YouTube-script skill becomes Cole-specific because every session loads `user.md`/`memory.md`. Direct integrations (Gmail, Asana, Slack, Circle) via a Python API layer with careful per-capability permissions (zero-trust default).

#### 3. The heartbeat = proactivity

A scheduled process: gather context deterministically via integration APIs → send to [[ClaudeCode]] (via Agent SDK) with a preconfigured prompt → agent reasons and acts (draft replies, handle PRs) → Slack notification keeps the human in the loop. "The heartbeat saves me the most time out of everything."

### Security: the [[LethalTrifecta]]

A second brain inherently has all three trifecta pillars (private data access + untrusted content + exfiltration vector), making it maximally exposed to prompt injection. This is *why* Cole argues for building your own rather than running [[OpenClaw]]: you control permissions, start zero-trust, and layer capabilities deliberately. See [[LethalTrifecta]] for the full security model.

### The three-use-case frame

A Second Brain serves three intertwined purposes:

| Use case | Capabilities required |
|---|---|
| **Research** | Web search, terminal execution, file operations |
| **Ideation** | File search across accumulated notes, LLM reasoning, examples retrieval |
| **Organization** | File operations, search, linking |

[[ClaudeCode]]'s native capabilities cover all three. Coding-agent-minus-code-intelligence = general purpose CLI agent on a markdown filesystem.

### Why this stack specifically

#### [[ClaudeCode]] — the agent
- Strong at the agentic loop (long-running, multi-step tasks).
- Native filesystem ops + terminal execution + web search.
- Designed to run autonomously for hours when needed.

#### [[Obsidian]] — the canvas
- Pure markdown on the filesystem. Markdown is the LLM's native format.
- No abstraction layer (unlike Notion, which would require an MCP server).
- Graph view + backlinks + plugins for human-side reading and curation.
- Cole calls Obsidian his "canvas" — Claude Code generates content there; he applies the human touch.

#### [[ClaudeSkills]] — the capability layer
- [[ProgressiveDisclosure]]: short descriptions load upfront, full instructions load only when invoked.
- Avoids the [[ContextRot]] failure mode of MCP-server-fat agents.
- Each skill specializes the agent for a particular capability without bloating the rest.

### The three-purpose constraint

[[ColeMedin]] is explicit:

> *"The main point is to help me ideate, stay organized, and research things for me. Not to automate our business, replace us, or generate a bunch of AI slop to post all over social media."*

Every skill in his template falls under one of: ideation, organization, research. The human touch is preserved at the publication boundary.

### Skills Cole's template ships

| Skill | Purpose |
|---|---|
| **Brand & voice generator** | One-time setup; produces the project's brand spec for downstream skills |
| **Skill creator** (Anthropic-published) | Meta-skill that creates new skills |
| **MCP-to-Skill** | Wraps an MCP server's tools as a skill — sidesteps MCP context bloat |
| **PowerPoint generator** | Python-script-based slide generation, on-brand |
| **Excalidraw diagram generator** | Diagrams for content |
| **YouTube script generator** | Long-form scripts |
| **X / LinkedIn post drafts** | Short-form ideation |
| **Remotion (video B-roll)** | AI-generated video clips |
| **Email / Asana retrieval** | Pull data from external tools (via MCP-to-Skill) |

### Why Skills > MCP for personal capabilities

[[ModelContextProtocol]] servers expose all their tools' descriptions upfront — a 20-tool MCP loads ~5K tokens of tool descriptions per session whether you need them or not. With dozens of capabilities, this blows up the context window before you've sent a prompt.

Skills are lazy: a 50-skill system loads ~50 short descriptions (a few hundred tokens) upfront. Only the active skill's full instructions load on-demand.

For a Second Brain that grows over time, this is the difference between a system that scales and one that collapses under its own context weight.

### Why Obsidian beats Notion for this

Notion is rich and beautiful for humans, but it's a database behind an API. Claude Code can't directly own a Notion workspace — it has to talk to Notion via an MCP server abstraction. Obsidian is just markdown files. Claude Code reads, writes, links, refactors them natively.

(For people who use Notion for their own reasons: Cole's MCP-to-Skill pattern can wrap a Notion MCP and give the agent access — just with the costs of MCP integration. Direct filesystem access in Obsidian is cheaper.)

### Outcome

Cole reports the Second Brain "saves me dozens of hours every single week" and makes him "more excited to wake up every single day." The pattern is:

1. Idea or input arrives (web article, meeting note, voice memo).
2. Claude Code (with relevant skill loaded) processes / structures / organizes / writes-to-Obsidian.
3. Human reviews, edits, adds judgment.
4. Final artifact lives in Obsidian; future sessions can build on it via filesystem search.

## Related

- [[ClaudeCode]] — agent layer
- [[Obsidian]] — canvas layer
- [[ClaudeSkills]] — capability layer
- [[ProgressiveDisclosure]] — context-efficiency primitive that makes Skills work at scale
- [[ContextRot]] — the failure mode SecondBrain pattern is engineered to avoid
- [[KarpathyLLMWiki]] — the broader knowledge-management pattern this implements
- [[LethalTrifecta]] — the security model driving the build-your-own argument
- [[OpenClaw]] — inspiration-not-to-run foil; source of the memory-layer + heartbeat ideas
- [[PRDFirstDevelopment]] — how Cole helps you scope your own build
- [[ColeMedin]] — articulator
- [[summary-second-brain-with-claude-code-obsidian-skills]] — intro source
- [[summary-full-guide-ai-second-brain]] — comprehensive architecture source
