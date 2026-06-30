---
title: "Agent-Specific MD Files"
type: concept
tags: [agents, configuration, context, markdown, agent-md, customer-md, multi-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md"]
last_updated: 2026-06-29
---

## Definition
Agent-Specific MD Files is a pattern where each agent instance is configured with markdown files that define its role, behavior, and domain-specific context. The pattern uses two layers: a general agent.md (harness — how to use the system, how to react to inputs/outputs) and a customer-specific MD file (customer quirks, access levels, discounts, special rules).

## Key Information
- Demonstrated by Matthias Luebken in Seven AI's per-customer agent architecture
- **Agent MD**: The general harness — defines the agent's role, how to use the system, how to react to certain inputs and outputs, standard operating procedures
- **Customer MD**: Customer-specific context — specific quirks, access levels, discounts, special pricing rules, unique workflows for that customer
- Each customer gets their own agent instance with both files loaded as context
- The two-layer approach separates reusable system knowledge (agent.md) from customer-specific configuration (customer.md)
- When a new customer is added, only the customer.md needs to be created — the agent.md is shared
- Combined with session reuse, this provides both static configuration context and dynamic conversation context
- The pattern is an instance of the broader [[AgentsDotMd]] concept, applied specifically to multi-agent business systems where each agent serves a different customer
- Enables agents to handle customer-specific variations without hardcoding rules into the agent's system prompt

## Related
- [[summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon]] — source
- [[AgentsDotMd]] — broader pattern of markdown-based agent configuration
- [[Agent Session Reuse]] — complementary dynamic context pattern
- [[Multi-Channel Agent Routing]] — routing pattern that directs to the right agent/customer.md
- [[Seven AI]] — company implementing this pattern
- [[Matthias Luebken]] — speaker who demonstrated the pattern
- [[AgentHarnessSeparation]] — related concept of separating agent harness from domain logic
- [[SoulMD]] — related concept for agent personality configuration
