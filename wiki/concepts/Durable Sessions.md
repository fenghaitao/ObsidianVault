---
title: "Durable Sessions"
type: concept
tags: [ai-ux, streaming, pubsub, real-time, agents, architecture, resilient-delivery, multi-client]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

## Definition

Durable Sessions is an architectural pattern for AI applications that decouples the agent layer from the client layer via a shared, persistent, stateful medium. Instead of clients establishing direct point-to-point connections with agents (the default HTTP streaming/SSE model), agents and clients interact through an independently addressable, persistent, and fully resumable session resource — typically built on pub/sub primitives. This enables resilient delivery, continuity across surfaces, live control, and concurrent multi-agent visibility without complex agent-side plumbing.

## Key Information

### The Problem It Solves
- **Direct HTTP streaming (SSE)**: The default AI UX pattern — client makes a request to an agent, establishes a persistent point-to-point connection, agent streams events back via SSE. Everything is coupled to a single request.
- **Three failure modes**: (1) Connection drops kill the stream, (2) other tabs/devices have no visibility of in-progress responses, (3) other clients can't reach the agent to interact with or steer it
- **SSE-specific limitation**: SSE is one-way (server to client). A stop/cancel button creates ambiguity — closing the connection could mean cancel or just disconnect. Resume and cancel are mutually exclusive with SSE. Vercel's AI SDK docs confirm a "stop" bot is incompatible with resume functionality

### How Durable Sessions Work
- **Decoupling**: Agents write events directly to the session without worrying about client connection health; clients connect to the session and replay/resume without agent-side logic
- **Persistent connections**: All clients hold a continuously maintained connection to the session, providing constant visibility of activity — not just when a request is invoked
- **Shared resource**: The session is a shared resource that agents also have full visibility of — any client can route to and interact with the agent from any tab or device
- **Multi-agent support**: All agents write independently to the session, eliminating the need for a centralized orchestrator to proxy granular progress updates
- **Single subscription**: Clients subscribe only to the session and get full visibility of all agent activity plus activity from other clients

### Three Foundational Capabilities Enabled
- **Resilient delivery**: Streams survive disconnections — clients reconnect and pick up exactly where they left off (mobile handoffs, page refreshes, tab switches)
- **Continuity across surfaces**: Conversation sessions follow users across devices and tabs, fully in sync including live activity
- **Live control**: Bidirectional communication — users can steer, interrupt, or send follow-ups to agents while they work, from any device

### Implementation via Pub/Sub
- Durable sessions can be built on pub/sub primitives (e.g., Ably channels)
- Key channel properties needed: independent addressability, persistence (messages outlive connections), full resumability
- Ably AI Transport is a drop-in SDK that provides: automatic text chunk materialization into complete responses, automatic resumability, multiplexing for concurrent activity, multi-client bidirectional control, push notifications, shared data objects

### Demo Capabilities Shown
- Multi-tab sync out of the box with zero additional agent logic
- Page refresh preserves full session state automatically
- Network kill and automatic reconnect with seamless continuation
- Two agents working concurrently in the same session, fully synchronized
- Human agent handoff with full visibility of AI interaction history

## Related

- [[Live Control]] — the bidirectional interaction capability
- [[ServerSent Events]] — the default protocol that durable sessions replace
- [[ResumableStreams]] — the resumability problem durable sessions solve
- [[PubSub]] — the underlying messaging pattern
- [[Ably]] — platform providing the channel primitives
- [[Mike Christensen]] — presented the pattern at aiDotEngineer
- [[Agent Channels]] — related cron-based agent execution pattern
- [[Durable Streams]] — related but distinct: append-only event logs, not session management
- [[summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably]] — source
