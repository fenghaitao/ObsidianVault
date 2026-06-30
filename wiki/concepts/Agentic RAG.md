---
title: "Agentic RAG"
type: concept
tags: [rag, agents, retrieval, search, context-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Definition

Agentic RAG is the evolution of RAG where a fixed retrieval pipeline is replaced with a search tool that an AI agent can decide to call or not. The agent determines whether retrieval is needed, can rewrite search queries, and can perform multiple rounds of retrieval (multi-hop) rather than a single fixed retrieval step.

## Key Information

- **Fixed RAG limitations**: Always retrieves even when not needed (can confuse the LLM), single retrieval can't handle multi-hop queries where retrieved chunks reveal the need for additional searches
- **Agentic RAG advantages**: Agent decides whether to retrieve at all, can rewrite queries, can retrieve multiple times, can verify results
- **Still one context source**: Basic agentic RAG still operates against a single database — full context engineering spans multiple context sources
- **Latency trade-off**: Agentic RAG has higher latency than fixed RAG due to multiple tool calls and reasoning steps
- **When to use**: RAG is still effective for many use cases; agentic RAG is needed when queries are complex, require multi-hop reasoning, or need verification
- **Switching between RAG and agentic RAG**: Requires agentic logic itself — not a simple routing problem

## Related

- [[summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic]] — source transcript
- [[Agentic Search]] — the broader concept
- [[RAG]] — the earlier paradigm
- [[ContextEngineering]] — the parent paradigm
- [[MultiHopRetrieval]] — key capability enabled by agentic RAG
