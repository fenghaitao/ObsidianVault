---
title: "events.iterate.com"
type: entity
category: service
tags: [event-sourcing, streaming, infrastructure, api, iterate]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

events.iterate.com is a lightweight streaming event service created by Iterate as a proof-of-concept infrastructure primitive for building event-sourced AI agent harnesses. It provides append-only event streams with auto-incrementing offsets, SSE streaming, push subscriptions, circuit breakers, scheduled events, and dynamic worker deployment.

## Key Information

- **Created by**: [[Iterate]] ([[Jonas Templestein]] and [[Misha]]) — built in the week before the aiDotEngineer workshop
- **Core features**:
  - **Event paths**: File-system-like hierarchy (e.g., `/jonas/example`) — created implicitly by posting
  - **Event envelope**: type, payload, stream path, offset, created_at
  - **SSE streaming**: Pull-based event consumption via HTTP SSE; `?live=true` for continuous streaming
  - **Push subscriptions**: Server pushes events to registered HTTP endpoints
  - **Circuit breaker**: Pauses streams if >100 events/second to prevent infinite loops
  - **Scheduled events**: Append events to be delivered in the future
  - **Idempotency keys**: Prevent duplicate events from retries
  - **Stream pause/resume**: Event-sourced pause mechanism
  - **Dynamic workers**: Deploy stream processors by appending source code as events
- **Web UI**: Available at events.iterate.com with a UI for browsing streams and appending events — the UI itself is a stream processor that reduces events into feed items
- **API docs**: OpenAPI spec available at events.iterate.com/api/docs
- **TypeScript SDK**: NPM package for programmatic access (`createEventsClient`)
- **Security**: No authentication in the proof-of-concept — all streams are publicly visible and writable; not suitable for production secrets
- **Project slug**: Optional HTTP header to create separate namespaces/databases
- **Tolerance**: Accepts non-conforming payloads and appends error events rather than rejecting
- **Type convention**: Event types are strings but the convention is to use documentation URLs (e.g., `https://events.iterate.com/agent_input_added`)
- **Workshop repo**: github.com/iterate/ai-engineer-workshop with examples and workshop.md

## Related

- [[Iterate]] — parent company
- [[Jonas Templestein]] — creator
- [[Misha]] — contributor
- [[Durable Streams]] — the architectural pattern
- [[Dynamic Workers]] — processor deployment feature
- [[Push Subscriptions]] — server-push feature
- [[Circuit Breaker Pattern]] — infinite loop protection
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
