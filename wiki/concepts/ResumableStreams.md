---
title: "Resumable Streams"
type: concept
category: methodology
tags: [streaming, agents, workflow, durability, reconnection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

# Resumable Streams

## Definition

Resumable streams are output streams in a workflow-based system that are decoupled from the API handler that initiated them. They persist independently of the HTTP connection, allowing clients to disconnect and later reconnect to the same stream at any point using a workflow ID, optionally resuming from a specific chunk offset.

## Key Information

- **How it works**:
  - The workflow creates a stream (e.g., in Redis in production, or a file locally) associated with its workflow ID
  - Any step can write to the stream using `getWritable()`
  - Clients can read from the stream via `getRun(id)` and access the readable stream
  - Reconnection uses a different API endpoint (e.g., `/chat/[id]/stream`) that returns the existing stream without re-executing the agent
- **Key benefit**: If a user loses connection to the API handler, the stream still exists and can be reconnected -- enabling durable, multi-session agent interactions
- **Implementation detail**: The `startIndex` parameter allows resuming from a specific chunk, so clients don't need to re-receive already-consumed data
- **Transport layer**: Requires client-side middleware to check for an existing run ID and route to the reconnection endpoint instead of starting a new chat

## SSE Limitation: Resume vs. Cancel Conflict

When using SSE for AI streaming, resume and cancel are mutually exclusive. SSE is strictly one-way (server to client), so the only way for a client to signal intent is to close the connection. The agent cannot distinguish between "user wants to cancel" and "connection dropped, buffer events for resume." Vercel's AI SDK docs confirm a "stop" bot is incompatible with resume functionality when using SSE. This makes SSE-based systems unable to simultaneously support both a stop button and resumable streams.

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[AgentObservability]]
- [[Durable Sessions]] — architectural pattern that solves the resume/cancel conflict
- [[ServerSent Events]] — the protocol with the one-way limitation
- [[Live Control]] — bidirectional capability needed for proper cancel support
- [[Ably]] — platform providing resumable channel infrastructure
- [[summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably]] — source
