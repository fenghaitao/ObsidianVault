---
title: "Dynamic Workers"
type: concept
tags: [event-sourcing, deployment, cloudflare-workers, serverless, code-as-events]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Dynamic Workers are a deployment mechanism for stream processors where the processor's source code is appended as an event to the event stream. The streaming service detects this event, spins up a worker (Cloudflare Worker in the Iterate implementation), and runs that processor against all subsequent events on the stream. This means agent behavior can be created, modified, and deployed purely through events — no separate deployment pipeline needed.

## Key Information

- **Event-driven deployment**: Appending an event of type `dynamic_worker_configured` with a script field containing JavaScript source code causes the service to deploy a new processor on that stream
- **Script content**: The script string contains a reducer function and an after-append hook — the same structure as locally-run processors
- **Self-modifying agents**: An AI agent can give itself new functionality by calling append with different JavaScript — enabling agents to extend themselves
- **Runtime**: Implemented using Cloudflare Workers for sandboxed JavaScript execution
- **Limitation**: Cannot have NPM dependencies — code must be self-contained or pre-bundled into the string
- **Bundling solution**: A future enhancement could add an unbundled dynamic worker event type (with package.json and script fields), where a separate processor handles bundling and creates the fat event with all dependencies inlined
- **Secret management**: API keys and secrets must be stored outside the stream (e.g., in environment variables) and substituted at runtime — to avoid exposing credentials in the event log
- **Horizontal scalability**: Dynamic workers are horizontally scalable by nature — the platform spins up workers as needed
- **Development workflow**: Develop locally with SSE pull subscriptions → once the processor is stable, deploy via dynamic worker event or as a standalone web service with push subscriptions
- **Security concern**: The current proof-of-concept has no authentication — all event streams are publicly visible and writable

## Related

- [[Stream Processor]] — the programming model deployed by dynamic workers
- [[Durable Streams]] — the event log where dynamic worker events are appended
- [[Cloudflare Workers]] — the runtime for dynamic workers
- [[Agent Harness]] — the system being built
- [[Agent Extensibility]] — the broader extensibility goal
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
- [[events.iterate.com]] — the implementation
