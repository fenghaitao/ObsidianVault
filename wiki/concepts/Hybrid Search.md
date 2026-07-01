---
title: "Hybrid Search"
type: concept
tags: [search, vector-search, keyword-search, rag, open-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition

Hybrid Search combines vector (semantic) search with keyword (lexical) search to retrieve more relevant results than either approach alone. In the OpenRAG stack, OpenSearch provides hybrid vector and keyword search out of the box.

## Key Information

- **Vector search**: Finds semantically similar content using embedding proximity
- **Keyword search**: Matches exact terms and phrases using traditional text indexing
- **Combined approach**: OpenRAG uses both simultaneously for more robust retrieval
- **Configurable filtering**: OpenSearch exposes sophisticated filtering and aggregation on top of hybrid search
- **Multi-vector support**: OpenSearch can search over multiple embedding models simultaneously (useful for model migration, though it slows search)
- **JVector integration**: OpenRAG uses the JVector KNN plugin (disk-based DiskANN architecture) for the vector component, enabling live indexing and scaling beyond memory limits

## Related

- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[OpenSearch]] — database providing hybrid search
- [[OpenRAG]] — uses hybrid search
- [[JVector]] — vector index plugin
- [[VectorDatabases]] — broader category
- [[Agentic Retrieval]] — search paradigm using hybrid search
- [[RAG]] — core technique
