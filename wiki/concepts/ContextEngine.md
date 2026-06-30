---
title: "ContextEngine"
type: concept
tags: [context-engineering, agents, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked.md"]
last_updated: 2026-06-29
---

## Definition

A context engine is a system that supplies AI agents with exactly the context they need (and none they don't) in a highly optimized way. It understands the codebase, organizational structure, and historical motivations to provide relevant background before agents execute tasks, avoiding doom loops and making agents "mergeable by default."

## Key Information

- Goal: supply necessary context, exclude unnecessary context, optimize for tokens and time
- Components include social engineering graphs (code, people, organizational decisions)
- Addresses the bottleneck shifting from intelligence to context
- Without a context engine, agents in YOLO mode risk doom loops
- Evolution: humans as context engine → curated context → automated context engines
- Contrast with naive RAG: context engines provide understanding, not just retrieval

## Related

- [[summary-20260503 - Mergeable by default： Building the context engine to save time and tokens — Peter Werry, Unblocked]] — source
- [[ContextEngineering]] — parent practice
- [[DoomLoop]] — failure mode addressed
- [[Unblocked]] — company building context engines
