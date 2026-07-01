---
title: "AgentHarness"
type: concept
tags: [agents, event-sourcing, architecture, harness, reliability, runtime]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-30
---

## Definition

An agent harness is the runtime framework that manages AI agent execution: tool calling, state management, context, and extensibility. Tejas Kumar defines it as "everything around the model that gives it grounding in reality" — the deterministic scaffolding that ties a black-box LLM to a stable environment. An event-sourced approach serializes every action as an immutable event in an append-only log, enabling full debuggability, replay, and composable plugins.

## Key Information

### Tejas Kumar's Definition (2026)
- A harness is everything around the model that gives it grounding in reality — it ties the agent to a stable, deterministic environment
- The purpose of a harness is reliability: making agents do what they're supposed to do irrespective of the black-box model
- Six standard components: Tool Registry, Model, Context Management, Guardrails, Agent Loop, Verify Step (see [[AgentHarnessComponents]])
- Harness engineering, not prompt engineering, is what makes agents succeed — the prompt should not need to change
- With a strong harness, cheap or free models can outperform expensive frontier models without one
- Contrast with ML harnesses (glorified test suites) — agent harnesses are runtime frameworks

### Event-Sourced Approach (Jonas Templestein)
- Event-sourced harness: every action is an event, no hidden side effects
- Each agent gets a URL and speaks HTTP natively
- Plugins are stream processors that consume and produce events, written in any language
- Trade-off: distributed plugins can cause race conditions and loops
- Contrast with traditional harnesses that have state outside the event log
- Inspiration from Pi's extensibility model

## Related

- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — source
- [[AgentHarnessComponents]] — the six standard components
- [[AgentHarnessSeparation]] — architectural principle of decoupling harness from data
- [[LoginHandler]] — harness pattern for programmatic authentication
- [[DynamicHarness]] — future vision of self-generating harnesses
- [[Harness Engineering]] — the discipline (coined by Ryan Lopopolo)
- [[EventSourcing]] — core architectural pattern
- [[StreamProcessing]] — plugin model
- [[Iterate]] — company building event-sourced harnesses
- [[ServerSent Events]] — SSE for streaming
- [[TejasKumar]] — defined the six-component model
- [[Guardrails]] — key harness component
- [[AgentLoop]] — key harness component
- [[Context Management]] — key harness component
