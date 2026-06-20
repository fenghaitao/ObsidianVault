---
title: "BuildingEffectiveAgents"
type: source
tags: [source, article, anthropic, agent-architecture, reference, external]
sources: []
last_updated: 2026-06-20
---

## Core Summary

"Building Effective Agents" is an [[Anthropic]] article that has become the canonical taxonomy of agent architectures in the AI-engineering community. [[ColeMedin]] cites it repeatedly across his content as the reference for agent design patterns. It's an **external source** (not a transcript in this vault's `raw/`), recorded here because so many wiki pages reference it.

> **Note**: This is an external article, not one of the ingested Cole Medin transcripts. It has no `raw/` source file. If the article is later clipped into `raw/`, convert this into a proper source summary. For now it documents what Cole reports about it across multiple videos.

## Key Information

### The architecture taxonomy

Anthropic's article lays out a progression of agent patterns, from simplest to most complex:

| Pattern | Shape | Wiki page |
|---|---|---|
| **Prompt chaining** | Sequential single-agent calls, each using the prior output | — |
| **Routing** | A router classifies input and dispatches to a specialized handler | — |
| **Parallelization** | Multiple agents on the same input simultaneously, results aggregated | [[ParallelAgentArchitecture]] |
| **Orchestrator-workers** | An orchestrator dynamically spawns and coordinates workers | [[ParallelAgentArchitecture]] (LLM-aggregator variant) |
| **Evaluator-optimizer** | A generator-critic loop iterating until quality threshold | [[AdversarialDev]] (a coding-specific realization) |

### The framework warning

The article's most-quoted line (Cole cites it in the [[LangChain]] context):

> Frameworks are "a level of abstraction that can sometimes be dangerous."

It recommends understanding the underlying building blocks before reaching for framework conveniences — the same spirit as [[CapabilitiesOverTools]] and Cole's preference for [[PydanticAI]] + [[LangGraph]] over heavier abstractions.

### Why it's cited so often in this corpus

Cole treats it as the shared vocabulary for agent design:
- The [[ParallelAgentArchitecture]] deep dive is essentially his expanded implementation of the article's "parallelization" pattern.
- The [[AdversarialDev]] harness is a GAN-flavored take on "evaluator-optimizer."
- The agent-harness evolution ([[AgentHarness]]) builds on the article's foundations.
- His learning roadmap points students to it for multi-agent architecture.

### Anthropic's broader agent publishing

The article is one of several Anthropic resources Cole references — alongside the [[ContextualRetrieval]] article and Anthropic's open-source [[AgentHarness|initializer-coder harness]]. Anthropic's pattern of publishing reference architectures has shaped how the community builds agents.

## Related

- [[Anthropic]] — author
- [[ParallelAgentArchitecture]] — the "parallelization" / "orchestrator-workers" patterns
- [[AdversarialDev]] — a realization of "evaluator-optimizer"
- [[AgenticWorkflow]] — the umbrella the taxonomy describes
- [[AgentHarness]] — builds on these foundations
- [[CapabilitiesOverTools]] — shares the framework-skepticism stance
- [[LangChain]] — context where Cole quotes the framework warning
- [[ColeMedin]] — frequent citer
