---
title: "SemanticCodeRetrieval"
type: concept
tags: [code-search, vector-search, embeddings, code-retrieval, semantic-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer.md"]
last_updated: 2026-06-30
---

## Definition
Semantic code retrieval is the use of vector embeddings to search codebases by semantic meaning rather than keyword matching. Code is chunked, embedded using a code-specific embedding model (e.g., Voyage code model), and indexed in a vector database. Queries are also embedded, and the most semantically similar code chunks are returned.

## Key Information
- Uses vector search (embedding similarity) rather than grep/keyword search
- Enables finding behaviorally-related files that don't share keywords (e.g., different ORM implementations across libraries)
- Works best on codebases with good inline comments and documentation — comments help the embedding model capture meaning
- Cursor uses built-in semantic code search (powered by Turbopuffer) with a custom embedding model that injects synthetic comments
- Claude Code uses agentic (grep-based) search by default; early versions experimented with a local vector DB but abandoned it
- TurboGrep is a tool that adds semantic code search to Claude Code as an add-on tool
- Benchmarking shows semantic search improves file-level precision from 65% to 87% on ContextBench
- Semantic search and grep-based search complement each other: semantic search excels at behavioral adjacency, grep excels at import tracing and keyword matching
- Long-term winners will provide multiple lightweight tools for finding context in different ways

## Related
- [[CacheCompute]] — the thesis that embeddings are upfront cached compute
- [[AgenticSearch]] — the grep-based alternative used by Claude Code
- [[VectorDatabases]] — infrastructure for semantic search
- [[ContextBench]] — benchmark for evaluating code retrieval
- [[TurboGrep]] — CLI tool that enables semantic code search
- [[Turbopuffer]] — vector database used for semantic search
- [[Voyage]] — embedding model provider
- [[summary-20260603 - Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer]] — source
