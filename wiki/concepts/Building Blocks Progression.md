---
title: "Building Blocks Progression"
type: concept
tags: [ai, agents, product-roadmap, anthropic]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

[[Cat Wu]]'s framing of [[Claude Code]] and [[Claude Cowork]]'s product roadmap as a sequence of building blocks: single-task reliability, then multiple simultaneous tasks, then many (50-100+) agents running in parallel and remotely.

## Key Information

- Stage 1 — task success: the core building block is making one clearly-scoped task (with a clear prompt/description) reliably produce acceptable, mergeable/shareable output.
- Stage 2 — multi-tasking: as task success rates rise with model capability, users start running several tasks at once ("multi-clauding"), a behavior Wu says grew steadily through late 2025 and beyond.
- Stage 3 — mass parallelism: as models get smarter still, Anthropic expects users to run tens to hundreds of agents simultaneously, which won't fit on a local machine (not enough RAM) and requires remote infrastructure, a management interface for triaging which tasks need human attention, reliable self-verification, and a feedback loop so the system improves from corrections rather than repeating mistakes.
- Illustrates [[AGI Pilled]] in practice: as models improve, prompt/UI scaffolding built for weaker models (like the to-do-list feature added so early models wouldn't drop tasks mid-refactor) gets progressively stripped out once it's no longer needed — Anthropic re-reads its entire system prompt at every model launch to remove now-unnecessary reminders.

## Related

- [[summary-13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary
- [[Cat Wu]] — describes this roadmap
- [[Claude Code]] / [[Claude Cowork]] — products this roadmap applies to
- [[AGI Pilled]] — related tension this progression navigates
- [[Multi-Clauding]] — dedicated concept page for stage 2 of this progression
