---
title: "Parallel Agents"
type: concept
tags: [agents, parallelism, architecture, performance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-25
---

## Definition
Parallel agents are multiple AI agents running concurrently to accomplish more work in less time. This trades extra compute for reduced wall-clock time, improving user experience by making autonomous coding feel more responsive and engaging.

## Key Information
- Parallelism is important not for making agents more powerful, but for making the user experience more exciting.
- Current approach: user manually decomposes tasks and dispatches each to its own thread, then resolves merge conflicts.
- Challenges: shared context duplication across agents (~80% overlap), merge conflict resolution (especially hard for non-technical users).
- Benefits: testing can run in parallel with code creation, asynchronous processes can inject useful information into the main loop, and multiple trajectories can be sampled simultaneously.
- Replit's next evolution: core loop as orchestrator, where task decomposition and parallelism are determined on the fly by the agent, not the user.
- Brendan O'Leary identifies parallel agents as a context isolation strategy: splitting work across several agents or sessions helps prevent context accumulation and drives task separation. This is one of the four key context management habits.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Core Loop as Orchestrator]] — next evolution
- [[SubAgent Orchestration]] — related pattern
- [[Agent Orchestration]] — broader practice using parallel agents
- [[Autonomous Coding Agents]] — application domain
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (context isolation strategy)
- [[ContextEngineering]] — the practice parallel agents support
