---
title: "Stream Processor"
type: concept
tags: [stream-processing, reduce, event-sourcing, agent-harness, state-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

A Stream Processor is the core programming model for event-sourced agent harnesses. It consists of a synchronous reduce function that derives state from an event stream, plus an optional after-append hook for enacting side effects. The reducer runs on every event to build up world state; the after-append hook fires only after the reducer has caught up, preventing redundant execution of expensive operations like LLM calls.

## Key Information

- **Two-part structure**: 
  - **Reducer**: `(state, event) => newState` — synchronous, pure function that updates agent state from events
  - **After-append hook**: Runs after the reducer catches up on all past events — the place for side effects (LLM calls, API requests, appending new events)
- **Why split reduce from side effects**: When a processor restarts (e.g., laptop closed, reopened), it catches up on past events via the reducer without re-executing side effects. Only after catch-up does it decide what to do with the final state
- **Initial state**: Defined for when the stream has no events yet — e.g., empty history, default model, default system prompt
- **State derivation**: All agent state (conversation history, model selection, compacting status, tool-call-in-progress flags) is derived from events through the reducer
- **Extensibility**: Adding new capabilities requires only 3-4 lines of code — define a new event type, add a case in the reducer, optionally handle in after-append
- **Composability**: Processors can import and run other processors' reducers — "It's practically free. You can just import it and run it." This enables building abstractions that rely on other processors' event types
- **UI as stream processor**: The events.iterate.com UI is itself a stream processor that reduces raw events into feed items for nicer rendering
- **Runtime**: A processor runtime handles the boilerplate of consuming the stream, running the reducer, and calling the after-append hook
- **Processor runtime types**: Pull subscriptions (client connects via SSE and processes locally) or push subscriptions (server pushes events to external HTTP endpoints)
- **Polyglot**: The pattern is language-agnostic — any language can implement a processor using the simple HTTP API

## Related

- [[Reduce Function]] — the synchronous state derivation component
- [[Event Sourcing]] — the architectural foundation
- [[Durable Streams]] — the event log consumed by processors
- [[Agent Harness]] — the system built with stream processors
- [[Dynamic Workers]] — deploying processors via events
- [[Push Subscriptions]] — server-push runtime for processors
- [[Agent Composability]] — composing processors together
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
