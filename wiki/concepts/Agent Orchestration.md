---
title: "Agent Orchestration"
type: concept
tags: [agents, orchestration, parallelism, architecture, openhands, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
Agent orchestration is the practice of coordinating multiple AI coding agents working in parallel on decomposed sub-tasks of a larger software engineering problem, with human review at intermediate steps. It represents the bleeding edge of AI-assisted development, enabling massive productivity lifts on repeatable, automatable tasks that are too large for a single agent.

## Key Information
- Agent orchestration is the fourth stage in the evolution of AI coding: context-unaware snippets → context-aware code generation → autonomous coding agents → parallel agent orchestration.
- Tasks suited for orchestration are repeatable and automatable: CVE remediation, code modernization, dependency updates, framework migrations, documentation automation.
- One client achieved a 30x improvement in CVE resolution time using orchestrated OpenHands agents.
- The goal is ~90% automation with human review at intermediate steps, not 100% hands-off operation.
- Most developers will use single local agents; only ~1% of early adopters are experimenting with orchestration.
- Key challenges: limited context windows, agent laziness, lack of domain knowledge, compounding errors, and difficulty conveying human intuition.
- Effective orchestration requires decomposing tasks into independently verifiable, parallelizable units with clear dependencies.
- Cloud-based sandboxes (Docker/Kubernetes) are essential for running agents securely and scalably in orchestration scenarios.
- The workflow: decompose task → dispatch parallel agents → review intermediate outputs → collate results → merge.
- AgentCraft takes a gaming-inspired approach: RTS-style file system maps, heat maps for collision detection, muscle-memory agent cycling, and progressive autonomy (quests → campaigns → channels).
- AgentCraft's campaigns run agents in containers with a campaign orchestrator handling coordination, shifting human effort from babysitting to planning and review.
- AgentCraft's channels enable cron-based fully autonomous agent runs that scan external sources for ideas and implement them.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Task Decomposition]] — prerequisite for orchestration
- [[Parallel Agents]] — agents running concurrently
- [[SubAgent Orchestration]] — related architecture pattern
- [[Context Sharing Between Agents]] — coordination mechanism
- [[HumanInTheLoop Orchestration]] — review pattern
- [[CloudBased Agent Sandboxes]] — infrastructure for orchestration
- [[CVE Remediation at Scale]] — example use case
- [[Paperclip]] — agent orchestrator with org-chart-based multi-agent coordination
- [[AgentOrgChart]] — Paperclip's hierarchical orchestration model
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[AgentCraft]] — gaming-inspired agent orchestrator with RTS-style visualization
- [[RTSInspired Agent Orchestration]] — AgentCraft's gaming-inspired paradigm
- [[Agent Campaigns]] — autonomous containerized agent missions
- [[Agent Collision Detection]] — heat map visualization of file conflicts
- [[Agent Channels]] — cron-based autonomous agent execution
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source (leader-follower canvas orchestration)
- [[LeaderFollower Agent Pattern]] — spatial canvas-based orchestration model
- [[Fairies]] — multi-agent canvas implementation
- [[Canvas as Agent Workspace]] — spatial shared state for orchestration
