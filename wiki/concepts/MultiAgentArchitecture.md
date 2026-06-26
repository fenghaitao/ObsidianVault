---
title: "MultiAgentArchitecture"
type: concept
tags: [concept, architecture, ai-agents, genbi, pipeline, crewai, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-26
---

## Definition
Multi-Agent Architecture is a design pattern where multiple specialized AI agents work together in a pipeline, each handling a distinct responsibility. In the GenBI context, agents collaborate to understand context, find relevant data, generate queries, and produce business answers.

## Key Information
- Northwestern Mutual's GenBI system uses four specialized agents in a pipeline:
  - **Metadata Agent**: Understands the business context of the question by working with the data catalog and documentation
  - **RAG Agent**: Finds existing certified reports and dashboards that answer the question
  - **SQL Agent**: Generates and executes SQL queries when no suitable report exists, using found reports as seed queries
  - **BI Agent**: Translates raw data results into natural language business answers
- An orchestrator manages the flow: question → metadata agent → RAG agent → (if needed) SQL agent → BI agent → answer
- Conversation context is maintained to avoid re-processing the same data within a session
- Each agent can be independently productized as its own deliverable, enabling incremental value delivery
- The RAG agent alone was productized and automated ~80% of report-finding work
- Governance and trust layers are applied across the entire pipeline
- Aman Khan's AI trip planner demo used a similar multi-agent pattern with LangGraph: budget agent, local experiences agent, and research agent running in parallel, all feeding into an itinerary agent that summarizes their outputs
- The demo showed parallel agent execution visualized as traces and spans in Arize, with each agent producing structured output consumed by the summarization agent

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source (CrewAI crew-based architecture)
- [[summary-20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual]] — source transcript
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[GenBI]] — system built with this architecture
- [[IncrementalDelivery]] — strategy enabled by independently productizable agents
- [[LangGraph]] — framework used for the trip planner multi-agent demo
- [[CrewAI]] — framework with crew-based multi-agent orchestration (10M+ agents/month)
- [[AgentCrewOrchestration]] — CrewAI's crew-based multi-agent coordination pattern
- [[AgentCompanyPattern]] — business application using multi-agent crews
- [[AgentVisualization]] — visual representation of multi-agent systems
- [[NorthwesternMutual]] — company implementing the architecture
