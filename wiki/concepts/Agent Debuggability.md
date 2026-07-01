---
title: "Agent Debuggability"
type: concept
tags: [event-sourcing, debugging, observability, agents, audit]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition

Agent Debuggability is the property that every action, state change, error, and decision in an agent system is recorded as an immutable event, making the entire system trivially debuggable and auditable. Jonas Templestein argues that existing agent harnesses "skirt around being event sourced" without fully committing — always having some side effect that can only be seen in third-party traces.

## Key Information

- **Full commitment**: Unlike partial event logging (where some side effects bypass the event log), pure event sourcing records everything — every LLM chunk, every tool call, every error, every pause
- **Trivial debugging**: "If you just say everything that could possibly happen is in there, it would be really easy to debug"
- **Error as events**: Even errors in posted events are recorded as error events in the stream — nothing is lost or hidden
- **Audit trail**: The append-only, immutable event log provides a complete, replayable history of everything the agent did
- **Offset tracking**: Each event has an auto-incrementing offset, providing a total order for replay and debugging
- **Current gap**: Most agent systems have some operations that aren't event-sourced — "there's always something that has a side effect that you later can tell, and then you can only see it in the hotel traces or something"
- **One abstraction**: "I'm kind of like a one abstraction kind of guy" — everything should be an event, including partial streaming responses, to avoid separate debugging surfaces

## Related

- [[EventSourcing]] — the architecture enabling debuggability
- [[Durable Streams]] — the event log providing the audit trail
- [[AgentObservability]] — the broader observability concern
- [[Stream Processor]] — the pattern that processes debuggable events
- [[summary-20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate]] — source
