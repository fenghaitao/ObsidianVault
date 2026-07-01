---
title: "Live Control"
type: concept
tags: [ai-ux, agents, bidirectional, real-time, streaming, interaction-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

## Definition

Live Control is the capability for users to communicate with and steer AI agents while they are actively working — going beyond the simple sequential request-response pattern. It requires bidirectional communication channels where clients can see what the agent is doing (visibility) and send messages, follow-ups, or interrupts to the agent mid-execution (control), from any device or surface.

## Key Information

### Why It Matters
- The best AI products (e.g., Claude Code) let users see what the agent is doing and send follow-up messages to steer or redirect it mid-work
- Without live control, users are locked into a fire-and-forget pattern — they must wait for the agent to complete before providing any further input
- Enables richer interaction models: interrupt, redirect, ask the agent to do something else, provide additional context mid-task

### Why Direct HTTP Streaming Fails at Live Control
- **SSE is one-way**: Server-Sent Events are strictly server-to-client — there is no upstream channel for the client to signal the agent
- **Cancel vs. resume ambiguity**: The only way to "stop" with SSE is to close the connection, but this creates ambiguity — is it a cancellation (stop burning tokens) or just a disconnection (buffer events for resume)?
- **Vercel AI SDK limitation**: The docs explicitly state a "stop" bot is incompatible with resume functionality when using SSE
- **WebSockets alone aren't enough**: Even with bidirectional transport, multi-device scenarios break — only the originating client has the upstream channel to the agent

### How Durable Sessions Enable Live Control
- All clients hold a persistent connection to a shared session that is always active — not just during request invocation
- The session is a shared resource that agents also have full visibility of
- Any client can route to and interact with the agent from any tab or device
- Supports concurrent multi-agent activity with full visibility from any client
- Enables human handoff: adding a human participant to the session with full interaction history visibility

## Related

- [[Durable Sessions]] — the architectural pattern that enables live control at scale
- [[ServerSent Events]] — the one-way protocol that prevents live control
- [[ResumableStreams]] — the related resumability problem
- [[Ably]] — platform providing bidirectional control infrastructure
- [[Mike Christensen]] — presented the concept at aiDotEngineer
- [[AgentHuman Collaboration]] — broader collaboration paradigm
- [[summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably]] — source
