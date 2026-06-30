---
title: "Durable Streams"
type: concept
tags: [event-sourcing, streaming, infrastructure, append-only, offset-tracking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

A Durable Stream is an append-only event log with offset tracking, serving as the foundational storage primitive for event-sourced agent systems. It is a well-known distributed systems pattern — combining aspects of a queue, a pub/sub system, and a streaming database — formalized by the Durable Streams API specification (which systems like ElectricSQL also implement).

## Key Information

- **Core properties**: Append-only, immutable events with auto-incrementing offsets; clients track their last consumed offset to resume from where they left off
- **Event envelope**: Each event has a type, optional payload, stream path, offset, and creation timestamp
- **Path hierarchy**: Streams are organized in a file-system-like hierarchy (e.g., `/jonas/example`) — paths are created implicitly by posting events to them
- **Server-Sent Events (SSE)**: Clients consume streams via HTTP SSE connections; `?live=true` keeps the connection open for real-time streaming
- **Push subscriptions**: Streams can also push events to registered HTTP endpoints (external servers, Slack webhooks, etc.) — enabling processors to run on separate machines
- **Circuit breaker**: Built-in protection against infinite event loops — pauses the stream if more than 100 events arrive in a second
- **Idempotency**: Supports idempotency keys to prevent duplicate events from webhooks or retries
- **Pause/Resume**: Streams can be paused and resumed by appending pause/resume events — the pause mechanism itself is event-sourced
- **Scheduled events**: Events can be scheduled for future delivery by appending schedule events to the stream
- **Spec lineage**: Inspired by the Durable Streams standard but not fully compliant; similar to Kafka's append-only log, NATS JetStream, and cloud pub/sub systems
- **Tolerance**: The service is tolerant of non-conforming payloads — invalid events are appended as error events rather than rejected
- **Event type naming**: Types can be opaque strings but the convention is to use URLs (e.g., `https://events.iterate.com/agent_input_added`) that serve as documentation links

## Related

- [[Event Sourcing]] — the architecture enabled by durable streams
- [[Stream Processor]] — the programming model that consumes durable streams
- [[Dynamic Workers]] — processors deployed via stream events
- [[Push Subscriptions]] — server-push mechanism for distributed processing
- [[Circuit Breaker Pattern]] — infinite loop protection
- [[Server-Sent Events]] — the HTTP streaming protocol
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[events.iterate.com]] — the implementation
