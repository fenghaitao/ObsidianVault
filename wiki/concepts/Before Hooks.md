---
title: "Before Hooks"
type: concept
tags: [event-sourcing, architecture, hooks, filtering, agent-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Before Hooks are pre-append filters that can intercept and potentially block events before they enter an event stream. Jonas Templestein argues strongly against exposing before hooks to third-party processors, advocating instead for eventual consistency — wait for a short timeout for external processors to contribute, then proceed regardless. Before hooks are reserved for built-in server functions like the circuit breaker.

## Key Information

- **Jonas's position**: "Broadly speaking, I'm very against before hooks." He cites examples where before hooks caused massive performance regressions, cost increases, and broke context caching in systems like OpenClaw
- **Eventual consistency alternative**: Instead of blocking the stream until a safety checker or RAG processor responds, the agent loop waits up to ~200ms for contributions, then proceeds regardless
- **Resilience benefit**: "This needs to be a resilient system" — if an external service is slow or unavailable, the agent should still function
- **RAG example**: A RAG processor can "try to squeeze in a little bit of extra context if I think it's relevant, but if I don't get there in time, it's like totally chill. The whole thing still works."
- **Built-in exceptions**: The circuit breaker and stream pause mechanism use before hooks because they must prevent events from ever entering the stream — these are server-internal, not exposed to third parties
- **Third-party limitation**: External processors cannot implement before hooks — they can only react to events after they are appended
- **Context caching protection**: Before hooks can destroy context caching efficiency by forcing re-computation on every event

## Related

- [[Event Sourcing]] — the architecture where before hooks apply
- [[Circuit Breaker Pattern]] — a legitimate use of before hooks
- [[Stream Processor]] — the after-the-fact processing model that replaces before hooks
- [[Push Subscriptions]] — the mechanism for external processors to contribute within the timeout window
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
