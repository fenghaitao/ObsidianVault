---
title: "Demand-Driven Context"
type: concept
tags: [context-management, knowledge-base, agents, enterprise-ai, methodology, institutional-knowledge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Demand-Driven Context is a methodology for transforming monolithic institutional knowledge bases into coherent, agent-usable context blocks. Instead of the industry-standard push approach (building MCP servers and RAG pipelines to feed all knowledge to agents), it uses a pull approach: give agents real work items, let them fail, surface what knowledge is missing, have domain experts fill the gaps, and let the agent curate the new knowledge for reuse.

## Key Information
- **Core Cycle**: (1) Give agent a problem → (2) Agent attempts and fails → (3) Agent produces a checklist of missing information → (4) Domain expert fills the gaps → (5) Agent solves the problem → (6) Agent curates the new knowledge for reuse. Repeat across multiple cycles.
- **Push vs Pull**: Current industry approach pushes all knowledge to agents via MCP servers and RAG. Demand-Driven Context pulls — agents request what they need when they fail.
- **TDD Analogy**: Write failing test cases first, then implement to make them pass. Similarly, give problems agents will definitely fail on, fill gaps, and gradually build institutional knowledge.
- **Monolith to Microservices Analogy**: Just as monolithic legacy systems were decomposed into microservices, institutional knowledge monoliths must be broken into context blocks useful for agents.
- **Memento Analogy**: The movie Memento (protagonist can't hold memory beyond 15 minutes) perfectly describes current AI agents — highly skilled but lacking institutional memory.
- **Three Knowledge Categories**: Green (general knowledge LLMs already know), Orange (teachable via agent skills/extensions), Red (institutional knowledge within company and people — the gap).
- **Confidence Progression**: Starting from 1.5 confidence (everything critical/missing), after 14 incident cycles, confidence reaches 4.4 as knowledge is discovered and documented.
- **Agent as Knowledge Manager**: The agent transitions from consumer to knowledge manager — it doesn't just consume knowledge, it manages the entire knowledge lifecycle including discovery, curation, and documentation.
- **80/20 Rule**: 20% of documentation is most useful; 80% is corner cases. Curate the critical 20% as a cache database (context blocks) and leave the rest as links.
- **Implementation**: Can be implemented with any agent (Copilot, Claude Code, etc.) using skills, rules, agents, hooks, and a knowledge base storage system.
- **Scope Recommendation**: Start at the smallest team level with scoped Jira tickets, incidents, and Confluence pages. At enterprise or domain level, no single person has all the domain expertise needed.
- **Published**: Preprint on RXP in March 2026.
- **Cost**: Per domain, knowledge bases average ~96K tokens — fits easily in modern context windows.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Raj]] — creator of the methodology
- [[Context Gap Scanner]] — automation tool implementing the methodology at scale
- [[Pull vs Push Context]] — core paradigm shift
- [[Agent as Knowledge Manager]] — key role transformation
- [[Knowledge Curation]] — the documentation process
- [[Agent Failure as Discovery]] — using failures to surface gaps
- [[Knowledge Base Monolith]] — what the methodology decomposes
- [[Context Blocks]] — the output of the methodology
- [[Meta Model]] — optional navigation map add-on
- [[Knowledge Base Kanban]] — documentation gap tracking
- [[Institutional Knowledge]] — the "red" category the methodology addresses
- [[TribalKnowledge]] — 40% of enterprise knowledge surfaced by the methodology
- [[TDD with AI]] — analogous approach
- [[MCP]] — the push approach being replaced
- [[RAG]] — the push approach being replaced
