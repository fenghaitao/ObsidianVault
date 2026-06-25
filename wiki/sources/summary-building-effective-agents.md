---
title: "summary-building-effective-agents"
type: source
tags: [source, anthropic, agent-architecture, external]
sources: []
last_updated: 2026-06-25
---

## Core Summary

Anthropic's canonical article on building effective AI agents, published in late 2024. Defines the taxonomy of agent architectures: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. Heavily cited across the corpus, especially by Cole Medin as the foundational reference for agent architecture patterns.

## Key Points

- Distinguishes between workflows (structured sequences) and agents (autonomous decision-makers)
- Recommends starting simple: don't build an agent when a workflow would suffice
- Warns that frameworks are "a level of abstraction that can sometimes be dangerous"
- Specifically praises LangGraph as a well-designed agent framework
- The five architectural patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer

## Related

- [[Anthropic]] — publisher
- [[ParallelAgentArchitecture]] — the parallelization pattern
- [[AgenticWorkflow]] — the workflow patterns
- [[CapabilitiesOverTools]] — overlapping philosophy
- [[LangGraph]] — praised framework
- [[ColeMedin]] — primary evangelist in this corpus
