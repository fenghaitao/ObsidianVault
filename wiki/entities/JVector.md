---
title: "JVector"
type: entity
tags: [tool, vector-index, open-source, search, knn]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - OpenRAG： An open-source stack for RAG — Phil Nash.md"]
last_updated: 2026-06-30
---

## Definition
JVector is an open-source vector index used as the default KNN (k-nearest neighbors) plugin in OpenRAG's OpenSearch deployment. It provides live indexing and disk-based architecture, meaning the entire index does not need to fit in memory.

## Key Information
- Open-source vector index
- Default KNN plugin in OpenRAG (replaces standard HNSW/IVF plugins)
- Based on DiskANN architecture — index stored on disk, not all in memory
- Provides live indexing capability
- Enables better scaling for data servers since memory is not the limiting factor
- Used as the "secret fourth open-source project" in the OpenRAG stack

## Related
- [[OpenRAG]] — uses JVector as default KNN plugin
- [[OpenSearch]] — database where JVector is deployed
- [[summary-20260408 - OpenRAG： An open-source stack for RAG — Phil Nash]] — source
- [[Hybrid Search]] — search paradigm enabled by the stack
- [[VectorDatabases]] — broader category
