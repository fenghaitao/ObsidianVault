---
title: "Decision Traces"
type: concept
tags: [decision-traces, context-graphs, agent-memory, reasoning, graph-embeddings, knowledge-graphs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Decision traces are structured records of past decisions stored in a context graph, capturing not just what decision was made but the full causal chain — the context, policies, precedents, and reasoning that led to it. Unlike documents, decision traces encode the why behind decisions, enabling AI agents to find similar past decision patterns via semantic and structural similarity search to inform new decisions.

## Key Information
- **Beyond documents**: Documents capture facts and current state; decision traces capture precedents, causal chains, and expected outcomes
- **Causal chains**: Decision traces are linked by relationships like "caused" or "next," forming chains that show how decisions build on each other over time
- **Hybrid search for precedents**: Finding similar past decisions uses both semantic similarity (vector search on text like "fraud rejection") and structural similarity (graph embeddings matching the shape of decision chains)
- **Graph embeddings**: Each decision trace and its surrounding graph structure is embedded into a vector, enabling similarity lookup over structural patterns — impossible with plain document search
- **Explainability**: Decision traces provide auditable provenance — the agent can show exactly which past decisions and patterns influenced its recommendation
- **Application**: A financial analyst agent uses decision traces to evaluate credit increase requests — it finds past rejections with similar structural patterns (e.g., fraud patterns, margin trades) and uses them as precedents
- **Three-layer memory**: Decision traces form the "reasoning" layer of [[Context Graphs]], alongside short-term memory (conversation history) and long-term memory (entities)
- **Entity extraction pipeline**: Raw conversations are processed through spaCy → gliner → LLM fallback to extract entities, which are then merged, deduplicated, and enriched before linking to decision traces

## Related
- [[Context Graphs]] — architecture that stores decision traces
- [[DecisionAwareAgents]] — agents that use decision traces for better decisions
- [[Graph Embeddings]] — technique for embedding decision trace structures
- [[Neo4j Agent Memory]] — memory package that implements decision trace storage
- [[Create Context Graph]] — CLI tool that scaffolds apps using decision traces
- [[Neo4j]] — graph database storing decision traces
- [[Zach Blumenfeld]] — speaker who presented this concept
- [[Agent Memory]] — broader memory architecture including reasoning traces
- [[Graph Data Science]] — library for graph embedding computation
- [[Cypher]] — query language for traversing decision traces
- [[summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — source
