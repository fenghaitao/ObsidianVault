---
title: "Graph Embeddings"
type: concept
tags: [graph-embeddings, neo4j, vector-search, graph-data-science, knowledge-graphs, similarity-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Graph embeddings are vector representations of graph nodes and their surrounding structural context, analogous to text embeddings but applied to graph data. Each node and its connected subgraph is embedded into a vector, enabling similarity search over structural patterns — similar graph structures produce similar vectors. This allows lookup of structurally similar decision traces, fraud patterns, or other graph patterns that would be impossible to find with text-based search alone.

## Key Information
- **Analogy to text embeddings**: Just as text embeddings map words/sentences to vectors based on meaning, graph embeddings map graph nodes to vectors based on their structural neighborhood
- **Structural similarity**: Similar decision traces (e.g., fraud rejection patterns with similar causal chains) produce similar embedding vectors, enabling lookup by structure not just content
- **Hybrid search**: Combined with semantic vector search (text-based) for comprehensive precedent matching — semantic similarity finds "fraud rejection" text, structural similarity finds decision chains with similar shapes
- **Neo4j GDS implementation**: Uses [[Graph Data Science]] (GDS) library with algorithms like FastRP (Fast Random Projection) for embedding generation and Louvain for community detection
- **Use case — decision traces**: In a financial analyst agent, graph embeddings enable finding past credit decisions with structurally similar patterns (e.g., a sequence of transactions → flag → review → reject)
- **Beyond text**: Enables retrieval of patterns invisible to document-based search — the shape of how decisions connect matters as much as what they say

## Related
- [[Decision Traces]] — primary use case for graph embeddings
- [[Context Graphs]] — architecture using graph embeddings
- [[Graph Data Science]] — Neo4j library for computing graph embeddings
- [[Neo4j]] — graph database platform
- [[Graph RAG]] — retrieval technique using graph structures
- [[Knowledge Graphs]] — underlying data structure
- [[Zach Blumenfeld]] — presented this concept
- [[summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — source
