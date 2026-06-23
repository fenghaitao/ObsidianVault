---
title: "MilestoneBasedBuilding"
type: concept
tags: [methodology, planning, ai-coding, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md, raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md]
last_updated: 2026-06-22
---

## Definition

Milestone-based building is the practice of breaking a software project into self-contained, sequentially-dependent chunks (milestones) that can each be built, tested, and verified independently by an AI coding agent. Each milestone builds on the previous one, and context is passed between them via milestone logs.

## Key Information

### Structure

- Milestones are numbered and sequenced by dependency (e.g., you can't build the Kanban view before contacts and deals exist).
- Each milestone is balanced: enough functionality to be meaningful, small enough to stay within a single coding session's coherence.
- Each milestone has a `prompt.md` that instructs the agent to read the PRD, build only that milestone, and write a milestone log.
- Milestone logs capture: what was built, technical decisions made during implementation, test coverage, and a human-readable summary of what's new.

### Why Milestones Work

- Prevents context rot: each milestone starts with a clean context window.
- Enables review checkpoints: verify each piece before moving on.
- Allows parallel work: different milestones can sometimes be built in different worktrees simultaneously.
- Makes scope manageable: prevents the agent from trying to build everything at once and going off the rails.
- The milestone log is the "baton pass" — it gives the next milestone's agent context about what already exists without carrying forward stale conversation.

### Typical Count

Brian Casel typically breaks projects into 3-7 milestones. His [[PRDCreator]] skill suggests 5 as a default and offers options for fewer (bigger chunks) or more (granular).

## Related

- [[SpecDrivenDevelopment]] — the parent methodology
- [[PRDCreator]] — the skill that automates milestone breakdown
- [[BrianCasel]] — primary advocate
- [[ContextRot]] — what milestones prevent
- [[PIVLoop]] — Cole Medin's related per-phase unit of work
- [[cole-vs-brian-planning-methodologies]] — synthesis comparing Cole's and Brian's planning approaches
