---
title: "ConductorVsOrchestrator"
type: concept
tags: [concept, google, agentic-engineering, developer-role]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good).md"
last_updated: 2026-07-06
---

## Definition

Conductor vs. orchestrator is [[Google]]'s framing (via its agentic-engineering masterclass) of two modes an engineer moves between when working with AI coding assistants. The **conductor** steers every move at the individual-file level (the early "tab-complete" style of generative AI). The **orchestrator** directs much larger units of work spanning whole codebases (or multiple codebases), reviewing outcomes rather than individual changes, often running several agents in parallel.

## Key Information

### The two modes

| | Conductor | Orchestrator |
|---|---|---|
| Granularity | Individual files/lines | Entire codebases, multiple repos |
| What you review | Each change | Aggregate outcomes (e.g. a set of PRs) |
| Parallelism | Single-threaded | Multiple agents running simultaneously |
| Era | Early generative AI (tab-complete) | Recent agentic-engineering focus |

### Google's claim vs. Cole's pushback

Google argues engineers should expect to move **between** both modes — dropping back to conductor-level micromanagement for deep debugging or initial exploration, and living in orchestrator mode otherwise. [[ColeMedin]] is skeptical of the "always moving between both" framing: he argues that once you've built a sufficiently reliable [[HarnessEngineering|harness]] and trust your rules/workflows, you can largely graduate to living at the orchestrator level permanently. He concedes the conductor mode is a useful mental model for teams/organizations just starting their agentic-engineering transition, before their system is mature.

## Related

- [[AIDrivenSDLC]] — the broader framework this distinction comes from
- [[HarnessEngineering]] — the system that lets you graduate from conductor to orchestrator
- [[AICodingAutonomyLevels]] — a parallel, more granular framework (Dan Shapiro's five levels) for the same underlying idea of increasing delegation
- [[Google]] — source of this framing
- [[ColeMedin]] — narrator/analyst; pushes back on part of the claim
- [[summary-20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)]] — primary source
