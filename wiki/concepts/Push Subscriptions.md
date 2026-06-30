---
title: "Push Subscriptions"
type: concept
tags: [event-sourcing, streaming, webhooks, distributed-systems, server-push]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Push Subscriptions are a mechanism where an event stream actively pushes new events to registered HTTP endpoints (external servers, webhooks, APIs) rather than requiring clients to poll. This enables stream processors to run on separate computers, in different languages, or as paid third-party services — the stream reaches out to the processor when there is work to do.

## Key Information

- **Push vs. Pull**: Pull subscriptions have the client connect via SSE and consume events. Push subscriptions have the server deliver events to registered endpoints — useful when the processor runs on a separate machine that may not always be connected
- **Filtered push**: Subscriptions can filter which events are pushed, reducing noise for specialized processors
- **Distributed processing**: Enables the polyglot, distributed vision — a Rust processor on one server, a TypeScript processor on another, both receiving events from the same stream
- **Third-party services**: A prompt injection protection service or RAG processor could run as a paid external service, receiving events via push subscription and contributing context within a timeout window
- **Timeout-based resilience**: The agent loop waits up to ~200ms for push subscribers to contribute information, then proceeds regardless — ensuring resilience even if external services are slow or unavailable
- **Configuration**: Push subscriptions are configured by appending events to the stream (e.g., "send events of type X to URL Y")
- **Use cases**: Slack notifications, external API calls, third-party safety checkers, distributed RAG pipelines, sub-agent coordination

## Related

- [[Durable Streams]] — the event log with push capability
- [[Stream Processor]] — the programming model that can use push or pull
- [[Edge Agents]] — agents as publicly routable HTTP services
- [[Agent Composability]] — composing distributed processors
- [[Polyglot Architecture]] — language-agnostic agent systems
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[events.iterate.com]] — the implementation
