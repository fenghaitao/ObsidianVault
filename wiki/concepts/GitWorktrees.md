---
title: "GitWorktrees"
type: concept
tags: [git, development, parallelism, agents]
sources: []
last_updated: 2026-06-25
---

## Definition

Git worktrees allow multiple working directories from a single Git repository, each on a different branch. Used by both Cole Medin and Brian Casel as the isolation mechanism for parallel agent execution — one worktree per agent prevents them from stepping on each other.

## Related

- [[ParallelAgentArchitecture]] — Cole's parallel system
- [[AgentMultitasking]] — Brian's parallel workflow
- [[ColeMedin]] — uses worktrees for parallel agents
- [[BrianCasel]] — uses worktrees for multitasking
