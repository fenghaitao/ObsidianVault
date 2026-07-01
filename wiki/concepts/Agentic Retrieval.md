---
title: "Agentic Retrieval"
type: concept
tags: [rag, agents, retrieval, search, context-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition

Agentic Retrieval is a search paradigm where an AI agent, rather than a fixed pipeline, is responsible for deciding what searches to perform and how to use the results. The agent receives the user's query along with instructions and tools, and it can perform as many searches as needed, unlike traditional single-shot embedding-to-search RAG pipelines.

## Key Information

- **vs Traditional RAG**: Traditional RAG embeds the query, performs a single nearest-neighbor search, and presents top-K chunks to the LLM. Agentic retrieval gives the query to an agent with tools and instructions; the model decides what to search and what to do with results.
- **Multi-search capability**: The agent can perform multiple searches, refine queries, and iterate based on intermediate results.
- **Tool integration**: In OpenRAG, the agent has access to tools including OpenSearch multi-model search, URL ingestors, calculators, and MCP servers.
- **Implementation**: OpenRAG implements agentic retrieval in LangFlow, where the agent flow receives chat input through a prompt template (including knowledge filters) and has access to configured tools.
- **Trade-off**: More powerful and flexible than fixed RAG pipelines, but adds latency due to multiple tool calls and reasoning steps.

## Related

- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[OpenRAG]] — implements agentic retrieval
- [[LangFlow]] — orchestration layer for agentic retrieval
- [[Agentic RAG]] — related agent-driven RAG concept
- [[Agentic Search]] — broader concept
- [[RAG]] — the traditional paradigm it improves upon
- [[Hybrid Search]] — search technique used within agentic retrieval
