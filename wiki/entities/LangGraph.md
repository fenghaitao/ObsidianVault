---
title: "LangGraph"
type: entity
tags: [tool, agent-framework, llm, langchain]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
LangGraph is an agent framework (part of the LangChain ecosystem) for building multi-agent systems with graph-based control flow. It was used in Aman Khan's demo to build an AI trip planner with multiple specialized agents.

## Key Information
- Used to build a multi-agent trip planner with budget, local experiences, research, and itinerary agents.
- Supports parallel agent execution — the demo showed budget, local experiences, and research agents running in parallel before feeding into an itinerary agent.
- Integrates with Arize/Phoenix for observability via OpenTelemetry instrumentation.
- Alternative to CrewAI for multi-agent orchestration.
- **Kiro demo usage**: Al Harris used LangGraph in his "Gramps" dad joke generator demo deployed to AWS Agent Core via CDK. LangGraph's native persistence/checkpointing mechanism was discovered as a more idiomatic alternative to custom S3-based checkpointing.

## Related
- [[CrewAI]] — alternative multi-agent framework
- [[Arize]] — observability platform that integrates with LangGraph
- [[MultiAgentArchitecture]] — architectural pattern used with LangGraph
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AmazonKiro]] — IDE used with LangGraph in the demo
- [[AgentCore]] — AWS service LangGraph agents were deployed to
