---
title: "summary-full-guide-ai-second-brain"
type: source
tags: [source, transcript, second-brain, claude-code, openclaw, lethal-trifecta, memory]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]]'s comprehensive guide to his [[SecondBrain]] (3 months of daily use, "saves at least a dozen hours"). Covers the full architecture: a **memory layer** (inspired by [[OpenClaw]]'s `soul.md`/`user.md`/`memory.md`), **skills** for capabilities, and a **heartbeat** for proactivity. Frames the build-your-own argument around the **[[LethalTrifecta]]** security model — why running OpenClaw directly is risky and building your own (taking inspiration, not the code) gives you control over permissions.

## Key Points

### Why build your own (not just run [[OpenClaw]])

The **[[LethalTrifecta]]** — an agent is dangerously exploitable (prompt injection) when all three hold:
1. **Private data access** (email, calendar) — always true for a useful second brain.
2. **Untrusted content** (incoming emails, web pages with possible injected instructions) — always true.
3. **Exfiltration vector** (can send data out) — always true (it can post/message).

A second brain inherently has all three. So you *must* be careful about implementation — limit each pillar as much as possible. OpenClaw doesn't limit private-data-access and exfiltration well, and it's a huge code base you don't understand. Building your own = you control permissions, start zero-trust, layer capabilities deliberately.

> Key move: Cole *takes inspiration* from OpenClaw (points Claude Code at its open-source repo to learn the memory layer and heartbeat) without *running* it. "Stand on the shoulders of giants."

### The memory layer (OpenClaw-inspired)

Markdown files loaded into context at session start via a **session-start hook**:
- `soul.md` — the personality given to the second brain.
- `user.md` — facts about the user; evolves over time.
- `memory.md` — key decisions, the most important file; concise promoted knowledge.
- `daily logs/` — raw dump of every conversation (the "raw" equivalent). One file per day.

**Promotion process** (daily cron via [[ClaudeCode|Claude Agent SDK]]): extract key decisions / lessons / facts from the long daily log → promote to `memory.md`. RAG over daily logs (indexed in SQLite) for things not important enough to promote but worth searching later.

### Skills = the "arms"

[[ClaudeSkills]] provide all capabilities — Cole uses *no MCP servers* in his second brain, just skills. Skills are powered by the memory layer: a generic YouTube-script skill becomes Cole-specific because every session loads `user.md`/`memory.md` and the skill references how he's scripted before.

Direct integrations (Gmail, Asana, Slack, Circle) via a **Python API layer** Cole controls — careful per-capability permissions. Read-only Slack; Gmail drafts but no send; Asana writes only in certain projects. Zero-trust default, add capabilities deliberately. New integrations one-shot easily because they follow a common pattern the agent can reference.

### The heartbeat = proactivity

A scheduled process that:
1. Gathers context deterministically via the integration APIs (what's happening in Cole's life right now).
2. Sends it all into [[ClaudeCode]] (via Agent SDK, programmatically invoked) with a preconfigured prompt.
3. The agent reasons: draft these replies, handle this PR, etc.
4. Sends a Slack notification keeping Cole in the loop; he can reply in-thread to continue.

"The heartbeat saves me the most time out of everything."

### The template

Cole doesn't give away his code base (defeats the purpose). Instead ships a **PRD-generation skill** (`/create-second-brain-prd`): fill out a requirements doc (your info, platforms, tasks, proactivity level [observer→advisor→partner], security boundaries, memory categories, infrastructure), run the skill, get a phased PRD. Build phase by phase ([[PRDFirstDevelopment]]).

## Related

- [[SecondBrain]] — central concept (this is the deep-dive)
- [[LethalTrifecta]] — security model
- [[OpenClaw]] — the inspiration-not-to-run foil
- [[ClaudeCode]] — substrate
- [[ClaudeSkills]] — capability layer
- [[Obsidian]] — canvas
- [[PRDFirstDevelopment]] — how Cole helps you scope your build
- [[KarpathyLLMWiki]] — the broader pattern
- [[ColeMedin]] — author
