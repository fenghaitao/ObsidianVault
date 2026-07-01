---
title: "summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably"
type: source
tags: [source, transcript, ai-ux, streaming, sse, durable-sessions, real-time, pubsub, agents, ably]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

## Core Summary
Mike Christensen (Staff Engineer at Ably) argues that the default direct HTTP streaming model (SSE-based) fundamentally limits the quality and richness of AI product experiences. The root cause: everything is coupled to a single request-response connection. He presents three foundational capabilities that separate fragile demos from great AI products — resilient delivery, continuity across surfaces, and live control — and introduces the durable sessions pattern as the architectural solution. Durable sessions decouple the agent layer from the client layer via a shared, persistent, stateful medium (built on pub/sub), enabling resumable streams, multi-device sync, bidirectional control, and concurrent multi-agent visibility without complex agent-side plumbing.

## Key Points

### Three Foundational Capabilities for Great AI UX
- **Resilient delivery**: Streams that survive disconnections — clients reconnect and pick up exactly where they left off (mobile Wi-Fi/5G handoffs, page refreshes, tab switches)
- **Continuity across surfaces**: Conversation sessions follow the user across devices and tabs, fully in sync including live activity
- **Live control**: Beyond sequential request-response — users can communicate with and steer agents while they work (like Claude Code), requiring bidirectional visibility and communication channels

### Why Direct HTTP Streaming Breaks Down
- **Coupling to a single request**: The health of the live response stream is tied to the health of the end client's connection — if the connection drops, the stream is gone
- **Private pipe problem**: The connection is a private pipe between client and agent — other tabs/devices have no visibility of in-progress responses
- **No shared resource**: Other clients can't reach the agent to interact, steer, or interrupt it
- **SSE-specific limitation**: SSE is strictly one-way (server to client) — a stop/cancel button creates ambiguity: does closing the connection mean cancel or just disconnect? Resume and cancel are mutually exclusive with SSE. Vercel's AI SDK docs explicitly state a "stop" bot is incompatible with resume functionality
- **Bidirectional transport alone isn't enough**: Swapping SSE for WebSockets doesn't solve multi-device visibility or multi-client interaction problems

### Durable Sessions Pattern
- A shared, persistent, stateful medium between the agent layer and client layer
- Agents write events directly to the session without worrying about client connection health
- Clients connect to the session to replay events or resume streams without agent-side logic
- All clients hold a persistent connection to the session that is always active, providing constant visibility
- The session is a shared resource — any client can route to and interact with the agent
- All agents can write independently to the session, eliminating centralized orchestration for granular progress visibility

### Multi-Agent Architectures with Durable Sessions
- Multiple agents participate in the same session, writing independently
- Eliminates the dual-purpose orchestrator problem (orchestrating + proxying granular updates)
- Clients subscribe to a single session entity and get visibility of all agent activity
- Drastically simplifies architecture — no centralized agent relaying updates from sub-agents

### Pub/Sub as the Foundation
- Durable sessions can be built on pub/sub primitives
- Ably channels provide: independent addressability, persistence (messages outlive connections), full resumability
- Ably AI Transport: a drop-in SDK that materializes text chunks into complete responses, provides automatic resumability, multiplexes concurrent activity, and supports multi-client bidirectional control
- Additional tools: push notifications for async agent completion, shared/subscribable data objects for real-time collaboration

### Demo Highlights
- Multi-tab sync out of the box with no additional agent logic
- Page refresh preserves full session state automatically
- Network kill and reconnect — everything carries on automatically
- Concurrent activity: two agents working simultaneously in the session, fully synchronized
- Human handoff: support agent added to session with full visibility of AI interaction history

## Related
- [[Mike Christensen]] — speaker
- [[Ably]] — company and platform
- [[Durable Sessions]] — the core architectural pattern
- [[Live Control]] — bidirectional agent interaction capability
- [[ServerSent Events]] — the default streaming protocol and its limitations
- [[ResumableStreams]] — the resumability problem and solutions
- [[PubSub]] — the underlying messaging pattern
- [[aiDotEngineer]] — conference
- [[ClaudeCode]] — referenced as example of live control UX
