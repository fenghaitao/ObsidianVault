---
title: "Server-Sent Events"
type: concept
tags: [http, streaming, protocol, web-standards, real-time]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably.md"]
last_updated: 2026-06-30
---

## Definition

Server-Sent Events (SSE) is an HTTP-based streaming protocol used in the event-sourced agent architecture for clients to consume event streams in real time. The events.iterate.com service supports both pull-based SSE (client connects and receives events) and live mode (`?live=true`) where the connection stays open for continuous streaming of new events.

## Key Information

- **Pull subscription via SSE**: Clients connect via HTTP GET with `Accept: text/event-stream` to receive a stream of events — the curl command `curl -N` enables streaming mode
- **Live mode**: Adding `?live=true` keeps the connection open indefinitely, sending new events as they are appended — inspired by the Durable Streams standard
- **Filtering**: Events can be filtered client-side by piping through tools like `sed` and `jq` for nicer formatting
- **Processor runtime**: The pull subscriptions processor runtime uses SSE under the hood to consume events and feed them into the reducer
- **Offset tracking**: SSE connections track the last consumed offset, enabling resume from where the client left off
- **Simple protocol**: SSE is a standard web protocol requiring no special libraries — plain HTTP with a specific content type

## Limitations for AI UX

- **Strictly one-way**: SSE is server-to-client only — there is no upstream channel for clients to signal the agent. A stop/cancel button creates ambiguity: closing the connection could mean cancel or just disconnect
- **Resume vs. cancel conflict**: Resume and cancel are mutually exclusive with SSE. When a client closes the connection, the agent can't tell if it should buffer events for resume or cancel the LLM to stop burning tokens. Vercel's AI SDK docs confirm a "stop" bot is incompatible with resume functionality
- **Private pipe**: The SSE connection is a private pipe between one client and one agent — other tabs/devices have no visibility of in-progress responses
- **Coupling to connection health**: The stream's health is tied to the end client's connection — if the connection drops, the stream is gone
- **Default in major frameworks**: Vercel's AI SDK and Timescale AI use SSE by default, making these limitations widespread

## Related

- [[Durable Streams]] — the event log served via SSE
- [[Push Subscriptions]] — the alternative server-push mechanism
- [[Stream Processor]] — the consumer of SSE streams
- [[Durable Sessions]] — architectural pattern that overcomes SSE limitations for AI UX
- [[Live Control]] — bidirectional capability SSE cannot support
- [[ResumableStreams]] — resumability problem exacerbated by SSE's one-way nature
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[summary-20260517 - Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably]] — source
- [[events.iterate.com]] — the implementation
