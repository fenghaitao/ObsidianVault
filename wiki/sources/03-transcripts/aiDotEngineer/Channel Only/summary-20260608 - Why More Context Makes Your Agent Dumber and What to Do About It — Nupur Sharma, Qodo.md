---
title: "summary-20260608 - Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo"
type: source
tags: [source, transcript, context-engineering, agents, context-optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo.md"]
last_updated: 2026-06-30
---

## Core Summary

Nupur Sharma from Qodo presents the counterintuitive finding that more context makes agents dumber: LLMs exhibit a U-curve attention pattern, focusing on start and end while ignoring middle context. Solutions: strategic context optimization via context engines, hierarchical summarization, knowledge graphs, and iterative retrieval.

## Key Points

- U-curve attention: LLMs focus on initial and final inputs, purge middle context. More data does not equal better results.
- Evolution: static 4K prompts → agentic workflows (infinite search loops) → multi-agent (clashing understandings).
- Solutions: (1) Context engines — search + ranking logic, but scaling across 600+ repos is challenging. (2) Hierarchical summarization — summaries per file/folder, but high LLM processing cost. (3) Knowledge graphs — logical dependencies between files, high initial effort. (4) Iterative retrieval — index-based, good for most tasks.
- Context engine acts as a "bouncer" — determines what's important and what to exclude.
- Qodo does agentic code reviews, transitioning from deterministic devsecops to non-deterministic agents.

## Related

- [[NupurSharma]] — speaker, Qodo
- [[Qodo]] — company, agentic code reviews
- [[ContextOptimization]] — core concept
- [[ContextEngine]] — context management
- [[Knowledge Graphs]] — dependency mapping
- [[IterativeRetrieval]] — retrieval strategy
