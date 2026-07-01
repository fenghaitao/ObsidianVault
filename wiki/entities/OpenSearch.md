---
title: "OpenSearch"
type: entity
tags: [tool, search, open-source, vector-database, elasticsearch]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition
OpenSearch is the open-source fork of Elasticsearch, used in the OpenRAG stack as the search and indexing database. It provides hybrid vector and keyword search with configurable filtering and aggregation.

## Key Information
- Open-source fork of Elasticsearch
- Provides hybrid vector + keyword search out of the box
- Supports configurable filtering and aggregation for targeted searching
- Supports multi-vector search over multiple embedding models (useful for model migration)
- Default plugin in OpenRAG is JVector KNN (disk-based architecture, live indexing, not memory-bound)
- Also supports HNSW and IVF vector indexes via the standard nearest neighbors plugin

## Related
- [[OpenRAG]] — uses OpenSearch as the search component
- [[JVector]] — default KNN plugin used in OpenRAG
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[Hybrid Search]] — search approach enabled by OpenSearch
- [[VectorDatabases]] — broader category
