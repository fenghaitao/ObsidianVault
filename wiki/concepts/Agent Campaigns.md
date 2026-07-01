---
title: "Agent Campaigns"
type: concept
tags: [agents, orchestration, autonomy, containers, agent-craft]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md"]
last_updated: 2026-06-29
---

## Definition
Agent Campaigns are high-level, autonomous agent missions in AgentCraft where the human provides a broad goal, and agents spin up containers, decompose the task, plan it, present the plan for review, and then execute autonomously with a campaign orchestrator handling coordination — removing the human from the babysitting loop.

## Key Information
- **Human role**: Provide a broad goal ("I want this feature"), review the plan, then step back
- **Container isolation**: Campaigns run in containers, so agents can do whatever they need without risk to the host system
- **Autonomous decomposition**: Agents break down the high-level goal into sub-tasks without human guidance
- **Plan presentation**: The decomposed plan is presented to the human for approval before execution begins
- **Campaign orchestrator**: A meta-agent that handles the babysitting and coordination that the human would otherwise need to do — "that's his problem"
- **Shift from planning to review**: The human invests effort only in the planning/review phases, not in execution monitoring
- Represents a step up the autonomy ladder: direct prompting → quests → campaigns → channels
- Key benefit: the human can have multiple campaigns running in parallel without being the bottleneck

## Related
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source transcript
- [[AgentCraft]] — the orchestrator implementing campaigns
- [[RTSInspired Agent Orchestration]] — the broader paradigm
- [[Agent Quests]] — simpler agent-suggested tasks
- [[Agent Channels]] — fully autonomous cron-based execution
- [[Agent Orchestration]] — broader orchestration concept
- [[Task Decomposition]] — the decomposition step within campaigns
- [[HumanInTheLoopWorkflows]] — the review/approval pattern
