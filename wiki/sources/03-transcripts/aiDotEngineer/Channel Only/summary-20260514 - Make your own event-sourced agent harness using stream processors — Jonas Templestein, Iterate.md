---
title: "summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate"
type: source
tags: [source, transcript, event-sourcing, agent-harness, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-29
---

## Core Summary

Jonas Templestein from Iterate presents a workshop on building an event-sourced agent harness using stream processors. The core idea: an agent is just an append-only event stream with a URL, where everything that can happen is serialized as events, making it fully debuggable and extensible. The system runs on events.iterate.com with a simple curl-based API, using SSE for streaming and plugins as stream processors.

## Key Points

- Agent harness built purely on event sourcing: every action is an immutable event in an append-only log, enabling full debuggability and replay.
- Each agent gets a URL (path-based hierarchy), speaks HTTP natively, and should be publicly routable on the edge.
- Extensibility via composable plugins: plugins are stream processors that consume and produce events, written in any language.
- No authentication in the workshop prototype (proof of concept); events.iterate.com provides the event store.
- Workshop format: live hackathon where participants curl events, build stream processors, and compose them into agents.
- Contrasts with traditional agent harnesses that have hidden side effects outside the event log.
- Risk of race conditions and infinite loops with distributed plugins, but these issues exist in most harnesses anyway.

## Related

- [[JonasTemplestein]] — speaker, works at Iterate
- [[Iterate]] — company
- [[EventSourcing]] — core architectural pattern
- [[AgentHarness]] — agent harness design
- [[StreamProcessing]] — stream processor plugins
- [[ServerSent Events]] — SSE for streaming agent events
- [[Pi]] — referenced as inspiration for agent extensibility
