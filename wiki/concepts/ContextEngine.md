---
title: "ContextEngine"
type: concept
tags: [context-engineering, agents, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Definition

A context engine is a system that supplies AI agents with exactly the context they need (and none they don't) in a highly optimized way. It understands the codebase, organizational structure, and historical motivations to provide relevant background before agents execute tasks, avoiding doom loops and making agents "mergeable by default."

## Key Information

- Goal: supply necessary context, exclude unnecessary context, optimize for tokens and time
- Six key capabilities: unified system context (reason across all systems of record), targeted exhaustive retrieval, conflict resolution, data governance (secure access model), personalized relevance (social graphs), and token optimization
- Components include social graphs that map engineering relationships (who works with whom, code review history, expertise areas)
- Addresses the bottleneck shifting from intelligence to context ("the gap is not intelligence, it is context")
- Without a context engine, agents in YOLO mode risk doom loops — producing code that compiles but is architecturally wrong
- Evolution: humans as context engine → curated context → automated context engines
- Contrast with naive RAG: context engines provide understanding, not just retrieval; naive RAG fails due to satisfaction of search
- Contrast with MCP-only approaches: MCPs provide access pipes but not understanding or reasoning across data
- Contrast with larger context windows: agents cannot reason effectively over massive context
- Caching correct answers is dangerous: context changes within 24 hours; cached responses become stale lies

## Related

- [[summary-20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked]] — source
- [[summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked]] — source
- [[ContextEngineering]] — parent practice
- [[DoomLoop]] — failure mode addressed
- [[Satisfaction of Search]] — phenomenon that undermines naive RAG
- [[Social Graph]] — key component for personalized relevance
- [[Conflict Resolution]] — key capability for handling conflicting signals
- [[Token Optimization]] — key capability for efficient agent communication
- [[Unblocked]] — company building context engines
