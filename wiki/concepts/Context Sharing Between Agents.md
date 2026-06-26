---
title: "Context Sharing Between Agents"
type: concept
tags: [agents, orchestration, context, coordination]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Context sharing between agents refers to strategies for passing learned information across multiple agents working on related sub-tasks, preventing them from all hitting the same problem independently. It ranges from manual human intervention to automated agent-to-agent messaging.

## Key Information
- When a fleet of agents hits the same problem, sharing the solution prevents all of them from getting stuck.
- Naive approach (share everything): every agent sees every other agent's context — equivalent to a single agent, quickly exhausts context windows.
- Manual human intervention: the human pastes information into each agent's chat or modifies agent.md/micro-agent files — not scalable.
- File-based sharing: agents read and write to a shared file like agent.md, potentially submitting PRs to it — requires human review to prevent agents from pushing unimportant information.
- Agent-to-agent messaging: each agent has a tool to send messages to other agents, either broadcast or point-to-point — the most leading-edge approach but increases non-determinism.
- Agents can enter unproductive loops when talking to each other (e.g., two agents looping on wishing each other "zen perfection").
- Human review of shared context is recommended to filter out unimportant information.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Agent Orchestration]] — broader practice
- [[Task Decomposition]] — prerequisite for effective sharing
- [[Parallel Agents]] — execution model
- [[Context Management]] — related concept
