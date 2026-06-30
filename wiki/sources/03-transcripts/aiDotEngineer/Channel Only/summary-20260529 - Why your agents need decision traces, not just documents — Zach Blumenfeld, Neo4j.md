---
title: "summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j"
type: source
tags: [source, transcript, decision-traces, context-graphs, neo4j, graph-embeddings, agent-memory, knowledge-graphs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Core Summary

Zach Blumenfeld from Neo4j presents the case for decision traces over plain documents in AI agent systems. While knowledge bases and RAG help agents answer questions correctly, context graphs with decision traces enable agents to make better decisions — not just retrieve facts but understand why past decisions were made. He demonstrates a financial analyst agent that uses past decision traces, precedents, and graph embeddings to determine whether to accept or reject a credit increase request, with full explainability. He also introduces two practical tools: the Neo4j Agent Memory package (a complete memory API with short-term, long-term, and reasoning layers) and Create Context Graph (a one-line CLI scaffolding tool that generates full-stack context graph applications with domain-specific ontologies).

## Key Points

- **Knowledge bases vs. decision traces**: Traditional RAG helps agents answer questions correctly; decision traces in a context graph help agents make better decisions by understanding why.
- **Financial analyst demo**: An agent evaluates a credit increase request by querying customer info, transactions, policies, and past decision traces with precedents. It uses hybrid search — semantic similarity (vector search on text) and structural similarity (graph embeddings matching the shape of past decision chains) — to recommend accept/reject with reasoning.
- **Graph embeddings**: Similar to text embeddings but applied to graph nodes. Decision traces and their causal chains are embedded into vectors, enabling similarity search over structural patterns — something impossible with plain documents.
- **Neo4j Agent Memory package**: A complete memory API with three layers: short-term memory (conversation history, session context), long-term memory (extracted entities resolved over time), and reasoning traces (the decision paths inside the context graph). Includes an entity extraction pipeline (spaCy → gliner → LLM fallback) with deduplication and enrichment.
- **Create Context Graph**: A CLI tool (`uvx create-context-graph`) that scaffolds a full-stack context graph application. Specify the domain (22 built-in including healthcare, FinServ, or custom), framework (Pydantic AI, OpenAI, LangGraph, Crew, Strands, Google ADK, etc.), and get a complete app with back end, front end, demo data, Cypher queries, and MCP server generation.
- **Data connectors**: Import data from GitHub, Notion, Jira, Slack via built-in connectors — not limited to demo data.
- **Decision trace mechanics**: Decision traces are structured records of past decisions linked in causal chains (linked by "caused" or "next" relationships). Agents query precedents by finding structurally similar past decision chains via graph embeddings and semantically similar ones via vector search.

## Related

- [[Neo4j]] — graph database company
- [[Zach Blumenfeld]] — speaker, research engineer at Neo4j
- [[William Lyon]] — Neo4j product manager who built the demo
- [[Context Graphs]] — the architecture underpinning decision traces
- [[Decision Traces]] — structured records of past decisions with causal chains
- [[Graph Embeddings]] — embedding graph nodes for similarity search
- [[Neo4j Agent Memory]] — open-source memory package
- [[Create Context Graph]] — CLI scaffolding tool
- [[Graph Data Science]] — Neo4j library for graph embeddings (FastRP, Louvain)
- [[Foundation Capital]] — identified context graphs as a $3T opportunity
- [[Agent Memory]] — broader concept of agent memory
- [[DecisionAwareAgents]] — agents that understand why, not just what
- [[Cypher]] — Neo4j graph query language
- [[Pydantic AI]] — one of the supported agent frameworks
