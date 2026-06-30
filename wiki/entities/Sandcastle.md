---
title: "Sandcastle"
type: entity
tags: [tool, typescript, agents, parallelization, docker, sandbox, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Sandcastle is a TypeScript library created by Matt Pocock for running parallel AI agent loops. It creates git worktrees, sandboxes them in Docker containers, runs implementer agents in parallel on independent issues, and then merges results with a dedicated merger agent.

## Key Information
- Built by Matt Pocock over approximately one week, out of dissatisfaction with existing options for running agents AFK
- Core function: `run()` creates a worktree, sandboxes it in Docker, and runs a prompt inside it
- Architecture: a planner agent looks at the backlog and chooses issues to work on in parallel based on blocking relationships
- For each chosen issue: create a sandbox, run an implementer agent with the issue details
- If commits were created: pass them to a reviewer agent for code review
- A merger agent takes all branches, merges them, and resolves any conflicts (types, tests, etc.)
- Uses Sonnet for implementation and Opus for reviewing (reviewing needs more "smarts")
- Implements the Push vs Pull pattern: pull for implementers, push for reviewers
- The parallel version is an evolution of the sequential Ralph Loop
- Each sandbox is an isolated git branch that can be merged later

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — creator
- [[Ralph Loop]] — the sequential predecessor
- [[Kanban Board for AI Tasks]] — the backlog it processes
- [[Parallel Agents]] — the execution model
- [[Push vs Pull Coding Standards]] — the standards enforcement pattern
- [[Docker]] — sandboxing technology
- [[Agent Sandbox]] — the general concept
- [[Day Shift Night Shift]] — the workflow it enables
