---
title: "Micro-Agents"
type: concept
tags: [agents, architecture, microservices, orchestration, openai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Micro-agents are small, single-purpose AI agents that do one thing and one thing well, analogous to microservices in software architecture. They are a paradigm within the OpenAI Agents SDK where many small agents with independent agentic loops are orchestrated together, either through sequential code or handoffs.

## Key Information
- **Analogy to microservices**: Just as microservices enabled deploying software multiple times a day and scaling independently, micro-agents promise similar benefits for AI agent systems
- **Single responsibility**: Each micro-agent has its own instructions, tools, and agentic loop focused on one task
- **Two orchestration modes in OpenAI Agents SDK**:
  - **"Just code"**: Sequential, parallel, or loop-based orchestration using standard programming constructs — pass results from one agent to the next
  - **Handoffs**: Agent-to-agent transfer within a single agentic loop, effectively switching context/persona without starting a new loop
- **Handoff mechanism**: When an agent hands off to another, it's not starting a new agentic loop — it's changing the context of the existing loop. The agentic loop takes on a different persona.
- **Example**: A triage agent decides whether a query is about weather or local business info, then hands off to the appropriate specialized agent
- **Temporal compatibility**: Both orchestration modes work with Temporal's durability layer
- **Unix philosophy parallel**: "Do one thing and one thing well" — Cornelia notes this makes her "heart sing" as someone who spent time in the Unix world

## Related
- [[OpenAIAgentsSDK]] — the framework enabling micro-agents
- [[AgentHandoffs]] — the handoff orchestration mode
- [[AgenticLoop]] — each micro-agent has its own loop
- [[MultiAgentArchitecture]] — the broader architectural pattern
- [[SubAgent Orchestration]] — related pattern from Replit
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
