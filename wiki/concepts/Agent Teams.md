---
title: "Agent Teams"
type: concept
tags: [ai, agents, multi-agent, sub-agents, coordination, claude-code, anthropic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Agent Teams is a Claude Code feature where sub-agents can communicate directly with each other (not just report to the main agent), coordinating independently and only reporting back to the main agent when required. It represents a more general-purpose way to scaffold custom agents with peer-to-peer communication.

## Key Information
- **Peer Communication**: The innovation is that sub-agents communicate with each other, not just the main agent. They coordinate independently and report back only when necessary
- **Release Context**: Shipped alongside Opus 4.6 and Sonnet 4.6, informed by research on long-running agents
- **Difference from Regular Sub-Agents**: Traditional sub-agents always report back to the main agent. Agent teams can coordinate among themselves, reducing the main agent's coordination burden
- **Generator-Evaluator Relationship**: The generator-evaluator pattern can be seen as a subset of the agent teams approach — two agents (builder and critic) in adversarial communication
- **Usage**: "People are using agent teams a ton" — widely adopted internally at Anthropic
- **Experimental Nature**: Anthropic "regularly unships things" — agent teams may evolve or be replaced as patterns mature
- **Cost Efficiency**: Became economical with Haiku 4.5 — running many sub-agents became cost-effective for the first time
- **Relationship to Generator-Evaluator**: Not contradictory — each agent in a team (frontend, backend, integrator) could have its own critic pairing. "You can see how the two concepts overlap"

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[SubAgents]] — predecessor primitive
- [[GeneratorEvaluator Pattern]] — related adversarial pattern
- [[AgentToAgentCommunication]] — MCP primitive for agent communication
- [[MultiAgentArchitecture]] — broader category
- [[Agent Orchestration]] — coordination approaches
- [[ClaudeCode]] — product with this feature
- [[ClaudeAgentSDK]] — framework supporting agent teams
- [[RALPH Loop]] — earlier agent coordination pattern
