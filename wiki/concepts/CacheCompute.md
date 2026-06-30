---
title: "CacheCompute"
type: concept
tags: [embeddings, optimization, token-savings, context, semantic-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Definition
Cache Compute is the thesis that embeddings and vector search act as a form of cached computation. By investing upfront compute to chunk, embed, and index a codebase, agents can retrieve semantic meaning through fast queries instead of repeatedly performing expensive grep-and-read cycles. This amortizes the cost across sessions and agents.

## Key Information
- Presented by Kuba Rogut (Turbopuffer) as the core argument for semantic code search
- Traditional agentic search (grep → read → grep → read) repeats the same compute across every session and every agent
- Semantic search front-loads the cost: chunk + embed + index once, then query cheaply forever
- Token savings per individual query are modest, but compound significantly when running multiple agents (e.g., "I'm running like three at one time")
- Example trace: agentic search uses ~6000 tokens for one query; semantic search gets same context with fewer tokens by querying cached embeddings
- Extends beyond code: vector DBs enable cached compute for knowledge bases, multi-modal data (video, audio, images)
- Vector databases offload the work of repeatedly understanding data into cached semantic meaning

## Related
- [[SemanticCodeRetrieval]] — the application of this concept to code search
- [[VectorDatabases]] — the storage layer for cached embeddings
- [[Turbopuffer]] — vector database company behind this thesis
- [[TokenOptimization]] — related concept of reducing token usage
- [[summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer]] — source
