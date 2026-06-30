---
title: "Graph Data Science"
type: concept
tags: [graph-data-science, neo4j, graph-embeddings, graph-algorithms, gds]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Graph Data Science (GDS) is a Neo4j library that provides graph algorithms and machine learning capabilities for graph data, including graph embeddings (FastRP), community detection (Louvain), and other graph-native analytics. In the context of AI agents, GDS enables structural similarity search over decision traces by embedding graph nodes into vectors.

## Key Information
- **Neo4j library**: Part of the [[Neo4j]] ecosystem for running graph algorithms and ML on graph data
- **FastRP**: Fast Random Projection algorithm for generating graph embeddings — embeds nodes based on their structural neighborhood
- **Louvain algorithm**: Community detection for grouping similar nodes or decision patterns
- **Used in context graphs**: Powers the structural similarity search in [[Create Context Graph]] applications — finds past decision traces with structurally similar causal chains
- **Enables hybrid search**: Combines graph embeddings (structural similarity) with vector search (semantic similarity) for comprehensive precedent matching
- **Underpins decision trace retrieval**: Without GDS, finding structurally similar decision patterns would be computationally impractical

## Related
- [[Graph Embeddings]] — primary output of GDS algorithms
- [[Neo4j]] — company providing the GDS library
- [[Decision Traces]] — concept that GDS helps retrieve
- [[Context Graphs]] — architecture using GDS
- [[Create Context Graph]] — CLI tool that uses GDS
- [[Zach Blumenfeld]] — presented GDS in context of decision traces
- [[summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — source
