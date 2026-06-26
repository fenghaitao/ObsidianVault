---
title: "Resumable Streams"
type: concept
category: methodology
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

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[AgentObservability]]
