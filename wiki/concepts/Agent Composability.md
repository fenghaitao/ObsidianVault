---
title: "Agent Composability"
type: concept
tags: [agents, architecture, extensibility, distributed-systems, composition]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Agent Composability is the design goal of making agent extensions independently developed, distributed, and combinable — "I made this extension. You made that extension. And you can combine them." In the event-sourced agent model, composability is achieved through shared event types, importable reducers, and distributed stream processors running on different machines in different languages.

## Key Information

- **Vision**: The community doesn't yet know the best recipe for agent harnesses. Composability enables experimentation — different people build different extensions that can be combined
- **Importable reducers**: Processors can import and run other processors' reducers — "It's practically free. You can just import it and run it." This enables building abstractions that rely on other processors' event types
- **Polyglot composition**: A Rust processor on one server and a TypeScript processor on another can both process events from the same stream, contributing different capabilities
- **Sub-agent pattern**: Sub-agents are modeled as child paths in the event hierarchy — the parent appends to `./boris` and subscribes to special events Boris outputs (e.g., "I have the result"), then the parent is automatically woken up
- **Third-party services**: A prompt injection protection service could run as a paid external processor, plugging directly into any agent's event stream
- **Current limitation**: "I don't think that's currently possible in any other way" — existing agent platforms require plugins to proactively hook into the agent loop, whereas event-sourced composability allows passive contribution
- **Composability challenge**: Distributed composition introduces the risk of race conditions and infinite event loops between processors — the circuit breaker is essential protection

## Related

- [[Stream Processor]] — the composable unit
- [[Agent Extensibility]] — the broader extensibility goal
- [[Polyglot Architecture]] — enabling cross-language composition
- [[Push Subscriptions]] — the mechanism for distributed processors
- [[Circuit Breaker Pattern]] — protection against composition-induced loops
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
