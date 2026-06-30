---
title: "Knowledge Graphs"
type: concept
tags: [knowledge-graphs, graph-database, neo4j, embeddings, vector-search, context-graphs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Knowledge graphs are a graph-based data structure that represents knowledge through nodes (people, things, companies), relationships (connections between nodes), properties (attributes on nodes and relationships), and embeddings (vector representations for similarity search). They combine structured knowledge representation with the ability to perform vector-based similarity searches, enabling both exact queries and semantic retrieval.

## Key Information
- **Structure**: Nodes represent entities (people, things, companies), relationships represent connections between nodes (e.g., "lives with," "drives"), and properties hold attributes (e.g., name, age). Embeddings on nodes enable vector similarity search.
- **Combining with LLMs**: Knowledge graphs provide knowledge, context, and enrichments while LLMs provide language, reasoning, and creativity. Together they enable storing relationships, visualizing data, finding hidden patterns, and analyzing insights.
- **First-Class Relationships**: Unlike relational databases where relationships require JOIN operations, knowledge graphs treat relationships as first-class citizens of the data model. This makes multi-hop traversal highly performant.
- **Graph Embeddings**: Techniques like FastRP (Fast Random Projection) create vector embeddings of graph nodes, enabling similarity search as an entry point into graph navigation. The Louvain algorithm enables community detection for grouping related nodes.
- **LLM Compatibility**: LLMs can generate Cypher (the query language), create knowledge graphs from unstructured documents, and navigate graph structures. Knowledge graphs are also human-readable — they represent information the way humans would draw it on a whiteboard.
- **Grounding Advantage**: In a healthcare example, a baseline LLM gave generic medical advice, vector RAG added some patient context, but knowledge graph RAG provided complete, patient-specific information (smoking history, prior operations) that similarity search missed.

## Related
- [[Context Graphs]] — architecture that builds on knowledge graphs with three-layer agent memory
- [[Graph RAG]] — retrieval technique using knowledge graphs for grounded information
- [[Cypher]] — Neo4j's query language for knowledge graphs
- [[Neo4j]] — graph database company providing knowledge graph technology
- [[Reasoning Traces]] — decision provenance stored in the knowledge graph
- [[Agent Memory]] — memory layers implemented on knowledge graphs
- [[summary-20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — source
