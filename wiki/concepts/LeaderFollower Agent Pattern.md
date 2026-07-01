---
title: "Leader-Follower Agent Pattern"
type: concept
tags: [agents, orchestration, multi-agent, delegation, coordination]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
The Leader-Follower Agent Pattern is a multi-agent orchestration model where one agent is elected leader, scouts the current state of the workspace, creates a to-do list, delegates tasks to follower agents, observes their work, and judges completion and correctness.

## Key Information
- **Leader election**: When multiple agents are grouped together, one is automatically elected leader
- **Leader responsibilities**: Scout the canvas to understand the current state, create a to-do list breaking down the work, delegate tasks to follower agents, observe follower progress, judge whether work is done and correct
- **Leader does not do the work**: The leader focuses entirely on coordination and judgment, not execution
- **Follower responsibilities**: Execute delegated tasks on assigned portions of the workspace
- **Shared state challenge**: Agents are "essentially blind while they're working" — they need mechanisms to share state and avoid overlapping work
- **Collision avoidance**: The leader must manage the fact that followers might overlap in their work if not coordinated
- Developed by tldraw in late 2024 (October-December) for the Fairies project, concurrent with the broader industry figuring out agent orchestration
- Analogous to coding agent orchestration patterns but visualized spatially on a canvas
- The leader acts as a verifier and judge, similar to the verifier-fixer pipeline pattern

## Related
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[Fairies]] — implementation of this pattern
- [[Agent Orchestration]] — broader orchestration concept
- [[AgentCrewOrchestration]] — related crew-based pattern
- [[VerifierFixer Pipeline]] — analogous verification pattern
- [[Task Decomposition]] — the leader's to-do list creation
- [[SubAgent Orchestration]] — related architecture
- [[Agent Collision Detection]] — related challenge in multi-agent systems
