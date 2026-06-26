---
title: "ThirdPartyAgentIntegration"
type: concept
tags: [agents, integration, interoperability, crewai, orchestration, universal-platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"]
last_updated: 2026-06-26
---

## Definition
Third-Party Agent Integration is a universal platform approach where an agent orchestration framework can incorporate agents built with external frameworks (LlamaIndex, LangChain, AutoGen, etc.) into its crews, giving them access to shared memory, tools, and crew-level features.

## Key Information
- Announced as a CrewAI feature: universal platform that can bring in any third-party agent
- External agents (LlamaIndex agents, LangChain agents, AutoGen agents) gain access to CrewAI features:
  - Shared memory across the crew
  - Shared tool access
  - Crew-level orchestration and coordination
- Positioned as "we don't see agent callers, we want all the agents" — philosophy of inclusion rather than walled-garden
- Enables heterogeneous agent crews where different agents may be implemented with different underlying frameworks
- Reduces lock-in: teams can adopt CrewAI's orchestration layer without rewriting existing agents
- Represents a platform play: become the universal orchestration layer for all AI agents

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[CrewAI]] — platform offering this feature
- [[AgentCrewOrchestration]] — orchestration pattern that external agents join
- [[AgentMemory]] — shared memory feature extended to third-party agents
- [[LangChain]] — one of the frameworks whose agents can be integrated
- [[LangGraph]] — related agent framework
