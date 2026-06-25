---
title: "ServerSentEvents"
type: concept
tags: [streaming, http, protocol, fastapi]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260513 - Sebastián Ramirez What's New in FastAPI - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Server-Sent Events (SSE) is an HTTP-based protocol for streaming data from server to client. Browsers have native EventSource API support. FastAPI added `EventSourceResponse` class for streaming with automatic ping, ID, retry, and comment fields. Used for LLM token streaming and MCP communication.

## Related

- [[FastAPI]] — framework with SSE support
- [[SebastianRamirez]] — implemented SSE in FastAPI
