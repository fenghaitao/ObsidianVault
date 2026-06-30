---
title: "Graph RAG"
type: concept
tags: [graph-rag, knowledge-graphs, retrieval, grounded-generation, neo4j, context-graphs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Graph RAG (Retrieval Augmented Generation) is a retrieval technique that uses knowledge graphs instead of (or in addition to) vector databases to ground LLM responses. Unlike vector RAG which retrieves semantically similar chunks, Graph RAG navigates the graph structure to pull in connected, complete information — including relationships, history, and context that similarity search would miss.

## Key Information
- **Progression of Grounding** (healthcare example):
  - **Baseline LLM**: Broad general knowledge, gives generic advice ("prevent damage to lungs")
  - **Vector RAG**: Adds some patient context, gives somewhat tailored advice ("respiratory therapy, deep breathing, coughing exercises")
  - **Graph RAG**: Pulls in complete patient history — previous diagnoses, operations, smoking history. Gives specifically grounded advice ("medication management, smoking cessation counseling, pulmonary rehabilitation exercise") that addresses the patient's actual background
- **Why Graph RAG is Better**: Similarity search loses background information that is structurally distant but critically relevant. Graph RAG traverses relationships to find connected knowledge that vector similarity alone cannot surface.
- **Performance**: Knowledge graphs are highly performant for multi-hop traversal, enabling navigation of complex structures at speed — a key advantage cited in graph RAG research papers.
- **Explainability**: Graph RAG queries (Cypher) are visible and traversable, making the retrieval path auditable and explainable — unlike black-box vector similarity search.
- **Combined Approach**: Graph RAG can be combined with vector search — graph embeddings (FastRP) provide vector lookups as entry points, then graph navigation algorithms (Louvain) traverse the connected structure for comprehensive retrieval.

## Related
- [[Knowledge Graphs]] — foundational data structure for Graph RAG
- [[Context Graphs]] — architecture that uses Graph RAG for agent memory retrieval
- [[Cypher]] — query language for graph-based retrieval
- [[Neo4j]] — graph database used for Graph RAG implementations
- [[Agentic RAG]] — broader category of RAG techniques for agents
- [[summary-20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — source
