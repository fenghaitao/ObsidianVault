---
title: "Core Loop as Orchestrator"
type: concept
tags: [agents, architecture, parallelism, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
Core loop as orchestrator is an agent architecture where the main agentic loop, rather than the user, determines task decomposition and dispatches parallel sub-agents on the fly. This is Replit's main bet for the next evolution of their autonomous coding agent.

## Key Information
- Contrasts with the current "user as orchestrator" model where the user manually decomposes tasks and dispatches agents.
- Advantages: no cognitive burden on the user for task decomposition, and the agent can create tasks that mitigate merge conflicts.
- Merge conflicts remain a challenge but can be reduced through software engineering techniques that prevent sub-agents from stepping on each other's work.
- Enables parallelism without requiring non-technical users to understand concepts like merge conflicts or task decomposition.
- Represents the next frontier beyond the three pillars of autonomy.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Parallel Agents]] — related pattern
- [[SubAgent Orchestration]] — foundational pattern
- [[Autonomous Coding Agents]] — application domain
- [[ReplitAgent]] — product implementing this
