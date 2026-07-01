---
title: "Pull vs Push Context"
type: concept
tags: [context-management, agents, knowledge-base, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Pull vs Push Context describes two opposing strategies for providing institutional knowledge to AI agents. The push strategy (industry standard) pre-builds all MCP servers and RAG pipelines to feed knowledge to agents. The pull strategy (Demand-Driven Context) gives agents work items, lets them fail, and has them request only the knowledge they need — analogous to how new employees are onboarded: given initial orientation, then assigned work and expected to ask questions.

## Key Information
- **Push Strategy (Current)**: Build MCP servers, RAG pipelines, knowledge graphs — push everything to the agent upfront. Problem: the underlying knowledge is undeterministic, unreliable, and untested. 10-30% accuracy at best.
- **Pull Strategy (Proposed)**: Give agents real work items → let them fail → surface what's missing → fill gaps → curate knowledge. Mirrors how humans onboard: initial orientation, then learn by doing and asking questions.
- **Employee Onboarding Analogy**: You don't tell a new employee "go get graduated on this knowledge and come back, then I'll give you work." You assign work, they ask questions, fill gaps, and gradually build institutional knowledge.
- **Agent Role Shift**: In push, the agent is a consumer. In pull, the agent becomes a knowledge manager — discovering gaps, requesting information, and curating what it learns.
- **TDD Analogy**: Push is like building the product first then writing tests. Pull is like TDD — write failing tests first (problems agents fail on), then implement (fill knowledge gaps).
- **Operational vs Pre-Retrieval**: Raj recommends fixing knowledge before retrieval (using the Context Gap Scanner), not during operational use. Doing it in real-time takes too much time and patience.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[DemandDriven Context]] — the pull methodology
- [[Agent as Knowledge Manager]] — the agent's role in pull strategy
- [[MCP]] — the primary push mechanism
- [[RAG]] — another push mechanism
- [[Agent Failure as Discovery]] — how pull surfaces gaps
- [[Knowledge Curation]] — what happens after pull
