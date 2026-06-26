---
title: "Task Decomposition"
type: concept
tags: [agents, orchestration, planning, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Task decomposition is the process of breaking down a large software engineering problem into sub-tasks that a single AI agent can solve in one shot, fit in a single commit, and be independently verified. It is the critical first step in agent orchestration and mirrors how work is broken down for human engineering teams.

## Key Information
- Each sub-task should be solvable by a single agent in one shot, fitting in a single commit/PR.
- Sub-tasks should be parallelizable to maximize speed gains from running multiple agents concurrently.
- Each sub-task must be independently verifiable, ideally through CI/CD status or a quick manual check.
- Clear dependencies and ordering between tasks must be established.
- Three decomposition strategies: piece-by-piece (iterate through files/directories), dependency tree (start from leaf nodes), and scaffolding (allow old and new systems to coexist).
- The piece-by-piece approach works well when dependencies are minimal (e.g., adding type annotations).
- The dependency tree approach adds ordering, starting from utility files and working up to entry points.
- Scaffolding enables incremental validation during migration by letting old and new systems run simultaneously.
- Decomposition mirrors how work is broken down for a team of engineers: separable tasks, parallel execution, clear dependencies.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Agent Orchestration]] — the broader practice
- [[Dependency Graph Refactoring]] — dependency tree strategy
- [[Scaffolding Pattern]] — scaffolding strategy
- [[Parallel Agents]] — execution model
- [[Sub-agent Orchestration]] — related pattern
