---
title: "Context Graphs"
type: concept
tags: [context-graphs, knowledge-graphs, agent-memory, graph-rag, neo4j, reasoning-traces, short-term-memory, long-term-memory]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Context Graphs are a unified architecture for agent memory that combines knowledge graphs with three layers of memory: short-term memory (current pipeline state and conversation), long-term memory (domain model and persistent knowledge across interactions), and reasoning traces (decision provenance capturing why decisions were made). The architecture addresses the problem of siloed enterprise knowledge by connecting disparate data sources — Slack, CRM, support tickets, internal business systems — into a single, queryable, and auditable graph structure that grounds agent decisions in complete context.

## Key Information
- **The Problem**: Enterprise knowledge is spread across siloed systems. When agents or applications make critical business decisions without connected context, they produce poor answers.
- **Three-Layer Memory Architecture**:
  - **Short-Term Memory**: Current pipeline state, ongoing conversation, agent activities — persisted in the knowledge graph for use during execution.
  - **Long-Term Memory**: Organized domain model with business processes, entities, and users — spans multiple interactions and users. Requires aggregation and a good schema.
  - **Reasoning Traces**: Captures the "why" behind LLM decisions — the thinking and reasoning that happens behind the scenes. Provides decision provenance for compliance, debugging, and making future decisions smarter by learning from previous traces.
- **Knowledge Graph Foundation**: Context graphs are built on knowledge graphs where relationships are first-class (no joins needed), multi-hop traversal is highly performant, and graph embeddings (FastRP) enable vector lookups as entry points for algorithms like Louvain (community grouping).
- **Architecture**: The agentic architecture uses context graph retrieval tools combining knowledge graphs, vector search, and data science algorithms. After the agent loop completes, results are pushed back into context memory and added to the graph for subsequent queries.
- **Explainability and Auditability**: Unlike traditional audit logs that only capture what happened, context graphs capture the why. Cypher queries are visible and traversable, showing exactly what information was used for each decision. This makes agent reasoning auditable and compliant.
- **Financial Services Demo**: A Next.js application connected to 10 MCP tools (support tickets, CRM, internal business data). When evaluating a loan application, the system queries account history, previous rejections, margin trades, and fraud patterns — surfacing information lost in siloed systems. The AI provides a recommendation with auditable reasons and risk factors.
- **Lenny's Podcast Demo**: Open-source project extracting entities and locations from podcast episodes, visualizing them as maps. Demonstrates holistic data access where the graph returns complete connected data rather than partial similarity matches.
- **Industry Recognition**: Gartner added context graphs to the AI hype cycle. Foundation Capital published a "$3 trillion startup opportunity" post about context graphs.

### Neo4j Agent Memory
The Neo4j Agent Memory is an open-source package that implements the three-layer memory architecture on Neo4j. It provides APIs for agents to access memory as tools, enabling short-term memory, long-term memory, and reasoning traces within a context graph structure. Available on GitHub with an open contribution model.

## Related
- [[Knowledge Graphs]] — foundational data structure for context graphs
- [[Graph RAG]] — retrieval technique that grounds LLM responses in graph-structured knowledge
- [[Reasoning Traces]] — the memory layer capturing decision provenance
- [[Agent Memory]] — the broader concept of agent memory, including Neo4j's graph-based approach
- [[Neo4j]] — company providing the graph database and Agent Memory package
- [[Stephen Chin]] — speaker who presented the context graph architecture
- [[Gartner]] — recognized context graphs on the AI hype cycle
- [[Foundation Capital]] — identified context graphs as a $3 trillion opportunity
- [[Cypher]] — query language used for knowledge graph traversal
- [[Explainable AI]] — context graphs enable explainable and auditable AI decisions
- [[summary-20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — source
