---
title: "CrewAI"
type: entity
tags: [tool, agent-framework, multi-agent, llm, company, open-source, enterprise]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-26
---

## Definition
CrewAI is a production-ready multi-agent AI orchestration framework and company founded by Joao Moura. It enables building and orchestrating multiple AI agents that collaborate in "crews" with shared memory, caching, and tools. The platform executes over 10 million agents monthly and 100,000+ crews daily.

## Key Information
- **Founder/CEO**: Joao Moura (Brazilian engineer, previously at Clearbit)
- **Scale**: 10M+ agents/month, 100K+ crews/day, 16K+ GitHub stars, 8K+ Discord members
- **Architecture**: Agents organized into specialized crews with shared memory, caching, and tools. Multiple crews can coordinate with each other.
- **Investors**: Dharmesh Shah (CTO of HubSpot), Jack Altman, and others
- **Key Features**:
  - **Code Execution**: `allow_code_execution` flag lets agents write and execute their own code to build tools dynamically
  - **Train Your Crew**: CLI for baking instructions into agent memory for consistent results over time
  - **Third-Party Agent Integration**: Universal platform bringing LlamaIndex, LangChain, AutoGen agents into CrewAI with shared features
  - **CrewAI Plus**: Enterprise offering — push crews to GitHub, get autoscaling API with bearer token auth and private VPC, one-click React component export
- **Meta-agent**: A crew that builds crews — takes email + company name, creates and deploys a crew to GitHub
- **Used by**: Multiple enterprise companies for production agent deployments
- Aman Khan originally had a Colab notebook for tracing CrewAI but switched to LangGraph for an Arize workshop demo.
- Represents one of several agent orchestration frameworks in the ecosystem.

## Related
- [[Joao Moura]] — founder and CEO
- [[LangGraph]] — alternative multi-agent framework
- [[MultiAgentArchitecture]] — architectural pattern
- [[AgentCrewOrchestration]] — orchestration pattern central to CrewAI
- [[AgentCompanyPattern]] — demonstrated by CrewAI's own operations
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
