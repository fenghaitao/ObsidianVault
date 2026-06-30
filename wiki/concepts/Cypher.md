---
title: "Cypher"
type: concept
tags: [cypher, query-language, neo4j, knowledge-graphs, llm-compatible]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Cypher is Neo4j's query language for knowledge graphs. It is designed to be both LLM-friendly (LLMs can generate Cypher queries to interact with graph data) and human-readable (representing information the way humans would draw it on a whiteboard).

## Key Information
- **LLM Compatibility**: LLMs can generate Cypher queries, create knowledge graphs from unstructured documents, and navigate graph structures programmatically
- **Human-Readable**: The syntax represents graph relationships in a way that mirrors how humans naturally think about connected information
- **Dual Purpose**: Cypher serves both as a query language for tooling and as a representation format that bridges machine and human understanding of graph data
- **Explainability**: Cypher queries are visible and traversable — in the financial services demo, users could see the exact Cypher queries executed, making the AI's reasoning path auditable
- **Used In**: Neo4j context graph architecture, Lenny's Podcast demo (extracting entities and locations), financial services application (querying account history, risk factors, fraud patterns)

## Related
- [[Neo4j]] — creator of Cypher
- [[Knowledge Graphs]] — data structure queried by Cypher
- [[Context Graphs]] — architecture using Cypher for memory retrieval
- [[Graph RAG]] — retrieval technique using Cypher queries
- [[summary-20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — source
