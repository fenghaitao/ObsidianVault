---
title: "Reduce Function"
type: concept
tags: [stream-processing, functional-programming, state-management, event-sourcing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

The Reduce Function is the synchronous, pure component of a stream processor that derives agent state from an event stream. It follows the functional pattern `(state, event) => newState` — taking the current accumulated state and a new event, and returning the updated state. It is the core mechanism for building event-sourced agent state without side effects.

## Key Information

- **Signature**: `(state, event) => newState` — synchronous function with no side effects
- **Pure computation**: The reducer must not perform I/O, make network requests, or modify external state — it only computes the next state from the current state and the incoming event
- **Catch-up replay**: When a processor restarts, it replays all past events through the reducer to reconstruct state — no LLM calls or API requests are re-executed during this phase
- **State as derived value**: All agent state (conversation history, model selection, system prompt, tool-call status, compacting flags) is derived from events through reducer cases
- **Event type matching**: Uses type-safe matching (e.g., Schematch/Zod) to handle different event types — each event type gets its own state update logic
- **Examples of reducer logic**:
  - `agent_input_added` → append user message to history
  - `llm_response_completed` → append assistant response to history
  - `model_changed` → update the model field in state
  - `compacting_started` → set compacting flag to true
- **Simplicity of extension**: Adding a new capability requires only a new event type and a case in the reducer — typically 3-4 lines of code
- **Composability**: Reducers from other processors can be imported and run within your processor — enabling layered abstractions
- **No side effects**: The strict separation from side effects is what enables safe catch-up replay — the after-append hook handles all external interactions

## Related

- [[Stream Processor]] — the full processor pattern containing the reducer
- [[EventSourcing]] — the architecture where reducers derive state
- [[Durable Streams]] — the event log consumed by reducers
- [[Agent Harness]] — the system built with reducers
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
