---
title: "DecisionAwareAgents"
type: concept
tags: [agents, decision-making, context-graphs, neo4j]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition

Decision-aware agents go beyond knowledge provision (what they can do) to incorporate policies, rules, and reasoning (why they should do something). They use context graphs with structured decision-making frameworks to make better autonomous choices, especially important in multi-agent systems and long-running autonomous workflows.

## Key Information

- Beyond knowledge: agents need to understand not just what but why — captured via policies and rules in context graphs
- Decision framework: local context (causality, objective, environment) → global context (past decisions) → informed decision
- Built on three-layer memory: short-term (conversations), long-term (organizational context), reasoning (policies/rules)
- Multi-agent systems amplify the need: agents must be self-aware and aware of each other's decisions
- Transferring implicit human understanding to explicit agent instructions is key

## Related

- [[summary-20260528 - Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j]] — source
- [[Context Graphs]] — underlying architecture
- [[Neo4j]] — graph database platform
- [[Agent Memory]] — memory model
- [[ContextEngineering]] — parent practice
