---
title: "Event Sourcing"
type: concept
tags: [temporal, architecture, state-management, durability, distributed-systems, stream-processors, agent-harness]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate.md"]
last_updated: 2026-06-30
---

## Definition
Event Sourcing is the underlying mechanism of Temporal: every state change in a workflow execution is recorded as an immutable event. When a process crashes and restarts, Temporal replays the event history to reconstitute the exact state of the application, allowing it to resume from where it left off without re-executing completed work.

## Key Information
- **Mechanism**: Every activity call, activity return, and workflow state change is recorded as an event in the Temporal service
- **Crash recovery**: On restart, Temporal replays the event history; completed activities return their cached results without re-executing
- **No tokens re-burned**: For AI agents, this means LLM calls that already completed are not re-executed — their results are replayed from the event history
- **State reconstitution**: Even though the process was killed and nothing remained in memory, Temporal can fully reconstruct the application state from the event log
- **Not just event-driven**: Temporal provides event sourcing as a service — developers don't implement the event store or replay logic
- **Durable storage**: Events are stored in the Temporal service (backed by relational databases or Cassandra for self-hosted, or Temporal Cloud's managed persistence)
- **Local dev**: The local Temporal server can use SQLite for persistence, or run in-memory (losing state on restart)

## Related
- [[Temporal]] — the platform implementing event sourcing
- [[TemporalWorkflows]] — the orchestrations recorded as events
- [[TemporalActivities]] — the execution units whose results are cached
- [[DurableAgenticLoop]] — the application to AI agents
- [[HappyPathProgramming]] — the developer experience enabled by event sourcing
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
