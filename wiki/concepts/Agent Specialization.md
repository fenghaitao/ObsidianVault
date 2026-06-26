---
title: "Agent Specialization"
type: concept
tags: [ai, agents, multi-agent, design-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Agent Specialization is the design pattern of creating multiple specialized AI agents, each with a distinct purpose (work, personal, fitness, etc.), rather than using a single general-purpose agent. Each specialized agent has its own provider model, system prompt (soul), tools/MCPs, and permissions.

## Key Information
- Kitze's critique of single-agent approach: "one-on-one chat with one agent sucks because if you think about delegating in your life... you don't want to have like one employee loaded with all the information about your life"
- OpenClaw supports specialized agents with: provider model, level of thinking, system prompt or soul, list of tools and MCPs, list of permissions
- "I like that this is like packaged and we're going to talk with this agent about fitness"
- Kitze created many bots, each with a purpose: work, personal, fitness, etc.
- Ended up with five Discords, each with many channels, threads, forum posts
- People moved to Telegram topics, Discord, Slack to organize conversations with different specialized agents
- Wolfer supports this with workspaces and agent management UI (right-side panel shows agent name, model, capabilities)

## Related
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source
- [[Kitze]] — advocate
- [[MultiAgentArchitecture]] — broader architectural pattern
- [[OpenClaw]] — framework supporting specialization
- [[Wolfer]] — Kitze's implementation
- [[AgentPersonality]] — the "soul" component of specialized agents
- [[AgentToAgentCommunication]] — how specialized agents coordinate
- [[Nested Context]] — Wolfer's alternative to memory for specialization
