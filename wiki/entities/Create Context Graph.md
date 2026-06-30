---
title: "Create Context Graph"
type: entity
tags: [cli-tool, neo4j, context-graphs, scaffolding, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Create Context Graph is an open-source CLI scaffolding tool by Neo4j that generates full-stack context graph applications with a single command (`uvx create-context-graph`). It provides boilerplate back end, front end, demo data, and ontology for building decision-aware AI agents powered by graph-based memory.

## Key Information
- **One-line setup**: `uvx create-context-graph` with parameters for app name, domain, agent framework, and demo data
- **22 built-in domains**: Healthcare, FinServ, and custom domain support with automatic ontology/graph schema generation
- **Agent framework support**: Pydantic AI, OpenAI, LangGraph, Crew, Strands, Google ADK, and others
- **Data connectors**: Import data from GitHub, Notion, Jira, Slack — not limited to demo data
- **Built-in features**: Cypher queries, graph native data access, decision trace visualization, MCP server generation, multi-turn conversation
- Built by [[William Lyon]], product manager at [[Neo4j]]
- Underpinned by the [[Neo4j Agent Memory]] package
- Uses [[Graph Data Science]] (GDS) for graph embeddings and structural similarity search
- Open source with community contributions welcome

## Related
- [[Neo4j]] — company behind the tool
- [[William Lyon]] — builder of the tool
- [[Context Graphs]] — architecture the tool scaffolds
- [[Neo4j Agent Memory]] — memory package underpinning the tool
- [[Graph Data Science]] — Neo4j library used for embeddings
- [[Decision Traces]] — concept demonstrated in generated apps
- [[Zach Blumenfeld]] — presented this tool
- [[Pydantic AI]] — one of the supported agent frameworks
- [[summary-20260529 - Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j]] — source
