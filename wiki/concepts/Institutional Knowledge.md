---
title: "Institutional Knowledge"
type: concept
tags: [knowledge-management, enterprise, agents, documentation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Institutional Knowledge is the domain-specific knowledge that exists within a company — in its people, processes, systems, and documentation. In the Demand-Driven Context framework, it is the "red" category of knowledge that AI agents lack and must be taught: knowledge that sits within the company and within people, not in general training data or teachable skills.

## Key Information
- **Three Knowledge Categories**: Green (general knowledge LLMs already know, e.g., API standards), Orange (teachable via agent skills/extensions), Red (institutional knowledge — the gap that prevents agents from completing enterprise tasks).
- **Enterprise Knowledge Reality**: 20% outdated, 20% unreliable, 10% duplicated across different places, 40% tribal knowledge (never documented).
- **The Enterprise AI Gap**: 88% of companies use AI but only ~6% see value creation (McKinsey 2026). The gap is institutional knowledge — agents can code but can't complete Jira tickets because they lack domain context.
- **Sources**: Confluence, Jira, SharePoint, Slack, GitHub, and people's heads.
- **Monolith Problem**: Institutional knowledge exists as an undifferentiated monolith that agents cannot effectively navigate, regardless of how many MCP servers or RAG pipelines are built.
- **The Fix**: Must be decomposed into context blocks (analogous to microservices decomposition) using a methodology like Demand-Driven Context.
- **Nobody Will Fix It For You**: LLM providers focus on model quality, agent builders focus on harnesses, the retrieval market ($9B) focuses on retrieval — but nobody will come to your company and fix your knowledge base. You have to fix it yourself.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Demand-Driven Context]] — methodology for transforming institutional knowledge
- [[Knowledge Base Monolith]] — the current state of institutional knowledge
- [[Context Blocks]] — the desired state after decomposition
- [[TribalKnowledge]] — the 40% that is never documented
- [[Agent Failure as Discovery]] — using failures to surface undocumented institutional knowledge
- [[Knowledge Curation]] — the process of documenting institutional knowledge
- [[Agent as Knowledge Manager]] — agent role in managing institutional knowledge
