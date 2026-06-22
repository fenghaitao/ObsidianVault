---
title: "AgentMultitasking"
type: concept
tags: [workflow, agent-orchestration, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

Agent multitasking is the 2026-era workflow of running multiple AI coding agents on different features or projects simultaneously using git worktrees for isolation. It emerged as specs became the primary output of creative work and single-agent workflows became a bottleneck.

## Key Information

### Evolution to Multitasking

- 2023: hand-coding everything.
- 2024: AI enhancement (tab completion, ChatGPT for copy).
- 2025: AI collaborator — spec-driven development, all creative work through one agent.
- 2026: agent orchestration — 2-4 features in parallel, agents on schedules, mobile management.

### Enablers

- **Git worktrees**: each feature gets an isolated copy of the codebase so agents don't conflict.
- **Modern agentic development tools**: SuperSet, Conductor, Cursor 3.0, Claude Desktop — all converging on sidebar + conversation + file browser layout.
- **Stronger models**: can handle larger, more complex tasks with less supervision.
- **Mobile**: kick off tasks from phone, review results later.

### Context Blending

Product work and marketing work increasingly run in parallel, sometimes in the same codebase. Brian has reusable skills for spinning up marketing pages and extracting video concepts from build work.

### Tool Preferences

Brian's current daily driver is [[SuperSet]] (native Claude Code CLI, worktree support). He evaluated [[Superconductor]] (wraps Claude Code), Cursor 3.0 (agent sidebar but no native Claude Code), and Claude Desktop (redesigned but limited).

## Related

- [[BrianCasel]] — practitioner
- [[SpecDrivenDevelopment]] — the methodology that enabled it
- [[GitWorktrees]] — the isolation mechanism
- [[SuperSet]] — Brian's daily driver
- [[NightShiftModel]] — the background agent complement
- [[ClaudeCode]] — the primary agent
