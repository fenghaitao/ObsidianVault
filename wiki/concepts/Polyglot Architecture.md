---
title: "Polyglot Architecture"
type: concept
tags: [architecture, agents, distributed-systems, language-agnostic, interoperability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Polyglot Architecture in agent systems refers to the design principle that agent extensions and processors should be language-agnostic — a processor written in Rust on one server and a processor written in TypeScript on another should both be able to participate in the same agent system. This is enabled by the simple HTTP-based event API that any language can implement.

## Key Information

- **Core insight**: The events.iterate.com API is "exceedingly simple" — an OpenAPI spec with basic HTTP operations — making it trivial to create clients in any language
- **Workshop limitation**: The workshop used TypeScript for convenience, but "the whole point is that we wouldn't have to"
- **HTTP as universal interface**: All interaction with the event stream is via HTTP (POST to append, GET with SSE to consume) — no language-specific SDK required
- **Distributed processing**: "You should be able to have an agent running on one computer, my plugin running over here, and your plugin running over there — and yours is written in Rust and mine is in TypeScript"
- **Trade-off**: Polyglot distribution introduces race conditions and potential infinite event loops between processors — the circuit breaker mitigates this
- **One abstraction**: "I'm kind of a one abstraction kind of guy" — the event is the single primitive; everything (streaming chunks, tool calls, errors, pauses) is an event
- **Web standards**: The system is built on web standards (HTTP, SSE) rather than proprietary protocols, making it inherently polyglot

## Related

- [[Agent Composability]] — the composition enabled by polyglot architecture
- [[Durable Streams]] — the HTTP-accessible event log
- [[Stream Processor]] — the language-agnostic programming model
- [[Push Subscriptions]] — enabling cross-language distributed processors
- [[Edge Agents]] — agents as HTTP-speaking programs
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
