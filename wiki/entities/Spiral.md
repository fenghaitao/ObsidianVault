---
title: "Spiral"
type: entity
tags: [product, writing-tools, agent-adopter, managed-agents, multi-agent]
sources: ["raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration.md"]
last_updated: 2026-07-05
---

## Definition

Spiral is a writing agent product built by [[Every]], exposed through a new API and CLI, powered by [[ClaudeManagedAgents]]' multiagent orchestration and outcomes features.

## Key Information

- **Architecture**: a lead agent (running on Claude Haiku) fields incoming requests and poses quick follow-up questions when needed, then delegates drafting to subagents (running on Claude Opus). When a user asks for multiple drafts, the subagents run in parallel — a productized instance of the [[MultiAgentSystem|orchestrator-subagent pattern]] with model-tiered delegation (cheap/fast lead, capable/slow specialists).
- **Quality gating via outcomes**: writing quality is Spiral's core value, so each draft is scored against a rubric built from Every's editorial principles and the user's voice, both pulled from [[AgenticMemory|memory]]. Only drafts that clear the bar are returned to the user.
- Cited by Anthropic (May 2026) as an example of multiagent orchestration and outcomes used together in production.

## Related

- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] - source announcement
- [[Every]] - the company that built Spiral
- [[ClaudeManagedAgents]] - platform Spiral is built on
- [[MultiAgentSystem]] - the orchestrator-subagent pattern Spiral implements
- [[AgenticMemory]] - memory store Spiral's rubric draws from
