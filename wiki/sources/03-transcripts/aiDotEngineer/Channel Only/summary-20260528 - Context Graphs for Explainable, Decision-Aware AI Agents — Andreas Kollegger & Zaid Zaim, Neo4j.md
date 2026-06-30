---
title: "summary-20260528 - Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j"
type: source
tags: [source, transcript, context-graphs, decision-making, neo4j, knowledge-graphs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j.md"]
last_updated: 2026-06-30
---

## Core Summary

Andreas Kollegger and Zaid Zaim from Neo4j present context graphs for decision-aware AI agents. Beyond providing knowledge (the "what"), context graphs capture policies, rules, and the "why" to help agents make better decisions. They introduce a decision-making framework with local context (causality, objective, environment) feeding into global context (past behavior patterns), powered by Neo4j's graph database.

## Key Points

- Context graphs extend context engineering: beyond knowledge (what an agent can do) to policies and rules (why an agent should do something).
- Three memory types: short-term (conversation history), long-term (organizational context, people), reasoning (policies and rules for decisions).
- The "why" gap: agents are good at language/reasoning/creativity but lack the knowledge graph component for grounded decision-making.
- Decision framework: local context (causality, objective, environment) → global context (past decisions and patterns) → informed decision.
- Autonomous agents and multi-agent systems amplify the need for structured decision-making frameworks.
- Neo4j graph database as the foundation: nodes + relationships + Cypher query language + text-to-Cypher translation.
- Decision-aware agents need memory graphs that combine short-term, long-term, and reasoning traces.

## Related

- [[Neo4j]] — graph database company
- [[ContextGraphs]] — core concept
- [[KnowledgeGraphs]] — graph data structure for AI
- [[ContextEngineering]] — parent practice
- [[AgentMemory]] — three-layer memory model
- [[DecisionAwareAgents]] — agents that understand why, not just what
- [[Cypher]] — Neo4j query language
