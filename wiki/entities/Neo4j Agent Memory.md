---
title: "Neo4j Agent Memory"
type: entity
tags: [open-source, neo4j, agent-memory, context-graphs, memory-package]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Neo4j Agent Memory is an open-source package that provides a complete memory API for AI agents, built on Neo4j's graph database. It implements the three-layer memory architecture — short-term memory, long-term memory, and reasoning traces — within a context graph structure, enabling agents to persist and retrieve conversation history, extracted entities, and decision provenance.

## Key Information
- **Complete memory API** with three integrated layers:
  - **Short-term memory**: Conversation history and session context
  - **Long-term memory**: Entities extracted from conversations, resolved and deduplicated over time
  - **Reasoning traces**: Decision paths and causal chains stored in the context graph
- **Entity extraction pipeline**: Multi-stage approach from spaCy → gliner → more advanced → LLM fallback, with merging, deduplication, and enrichment strategies
- Underpins the [[Create Context Graph]] scaffolding tool
- Integrates with Microsoft Agent Framework, Google ADK, and other agent frameworks
- Open source and available on GitHub
- Schema includes conversations, extracted entities (connecting to reasoning traces), and reasoning traces

## Related
- [[Neo4j]] — company providing the package
- [[Context Graphs]] — architecture the package implements
- [[Agent Memory]] — broader concept of agent memory
- [[Create Context Graph]] — CLI tool built on this package
- [[Decision Traces]] — reasoning traces stored via this package
- [[Zach Blumenfeld]] — presented this package
- [[summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — source
