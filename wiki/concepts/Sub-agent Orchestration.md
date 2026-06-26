---
title: "Sub-agent Orchestration"
type: concept
tags: [agents, architecture, orchestration, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-25
---

## Definition
Sub-agent orchestration is an agent architecture pattern where specialized sub-agents are invoked from the main agentic loop with a fresh context containing only the relevant subset of information. They run to completion and return results to the main loop, providing separation of concerns and reducing context pollution.

## Key Information
- Sub-agents start from a blank slate with only the context the agent builder decides to inject.
- Analogous to separation of concerns in traditional software engineering.
- Significantly improves memories-per-compression: Replit went from ~35 to ~45-50 after implementing sub-agent orchestration.
- Critical for autonomous testing: browser actions and observations would confuse the main loop if not isolated in sub-agents.
- In Replit's architecture, the main loop decides when to verify output, spawns a testing sub-agent, scratches its context after completion, and injects only the final observation back into the main loop.
- Enabled by improvements in how well models handle sub-agent orchestration.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Context Management]] — parent concept
- [[Core Loop as Orchestrator]] — next evolution
- [[Parallel Agents]] — related pattern
- [[Agent Orchestration]] — broader practice
- [[Three Pillars of Autonomy]] — framework
