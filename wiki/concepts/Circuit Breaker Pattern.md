---
title: "Circuit Breaker Pattern"
type: concept
tags: [event-sourcing, infinite-loops, rate-limiting, resilience, stream-protection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

The Circuit Breaker Pattern in event-sourced agent systems is a protective mechanism that automatically pauses an event stream when event throughput exceeds a threshold, preventing infinite event loops from overwhelming the system. In the events.iterate.com implementation, the circuit breaker itself is a stream processor — it reduces over the event stream, tracks timestamps, and appends a pause event if more than 100 events arrive within a second.

## Key Information

- **Self-referential design**: The circuit breaker is implemented as a stream processor running inside the event service — it monitors the stream it is part of by tracking the last 100 event timestamps
- **Threshold**: Pauses the stream if more than 100 events are appended within a one-second window
- **Pause as event**: Pausing is done by appending a pause event to the stream — consistent with the everything-is-an-event philosophy
- **Resume required**: Once paused, the stream rejects all new events until a resume event is explicitly appended
- **Error events excluded**: When paused, error events from rejected appends are not added to the stream (which would otherwise create an infinite loop of error events)
- **Infinite loop risk**: In distributed event-sourced systems, two processors can send events back and forth creating an endless stream — the circuit breaker is essential protection
- **State tracking**: The circuit breaker processor maintains state: `paused: boolean` and `paused_reason: string | null`
- **Server-enforced**: The circuit breaker is a built-in processor that runs before events are appended — it is one of the few things that cannot be implemented by third-party processors because it needs to prevent events from entering the stream

## Related

- [[Durable Streams]] — the event log protected by the circuit breaker
- [[Stream Processor]] — the pattern used to implement the circuit breaker
- [[EventSourcing]] — the architecture that necessitates circuit breaking
- [[Before Hooks]] — the server-side pre-append mechanism that makes circuit breaking possible
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[Events.iterateCom]] — the implementation
