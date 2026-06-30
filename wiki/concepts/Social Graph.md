---
title: "Social Graph"
type: concept
tags: [context-engineering, social-graph, agent-context, personalization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Definition

A social graph (also called an expert graph or social engineering graph) is a component of a context engine that maps relationships between engineers, code repositories, and organizational decisions. It captures who works with whom, code review relationships, PR history, and areas of expertise, enabling the context engine to personalize context retrieval based on the identity and work patterns of the person (or agent) making the query.

## Key Information

- Maps nodes (engineers) and edges (collaboration, code review, shared code areas) procedurally from code repository data
- Used as a pivot point for context retrieval: knowing who you are and who you work with narrows the search space to relevant codebases and patterns
- Node size can represent contribution volume (e.g., who ships the most code)
- Includes heat map grids of who reviews whom, peer tables of collaborators, and expertise labeling via LLM classification
- When an agent or engineer asks a question, the context engine pivots on the social graph to determine which codebases and patterns are most relevant
- Distinct from Neo4j-style context graphs, which focus on knowledge graph memory architecture; social graphs specifically map human engineering relationships
- Open-source tool demonstrated at AI Engineer World's Fair 2026 that generates social graphs from code repos

## Related

- [[summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked]] — source
- [[ContextEngine]] — parent system that uses social graphs
- [[Context Graphs]] — related but distinct concept (knowledge graph memory architecture)
- [[Brandon Waselnuk]] — speaker who demonstrated the open-source tool
- [[Unblocked]] — company building context engines with social graph components
