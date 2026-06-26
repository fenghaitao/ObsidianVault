---
title: "Temporal Workflows"
type: concept
tags: [temporal, workflow, orchestration, durability, distributed-systems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Temporal Workflows are business logic orchestrations that compose Temporal Activities into durable, long-running processes. They are the "application main" — the code that defines the sequence of steps. When combined with Activities, workflows deliver automatic retries, state persistence, crash recovery, and horizontal scaling without the developer writing infrastructure code.

## Key Information
- **Deterministic orchestration**: Workflows define the business logic (the "happy path") as a sequence of activity calls
- **Event sourcing**: Every activity call and return is recorded as an event; if the process crashes, Temporal replays the event history and resumes from where it left off
- **State management**: Temporal tracks where execution is in the workflow via event sourcing; state is stored durably in the Temporal service
- **Cues built-in**: What looks like a single-process application (calling activities sequentially) is actually distributed over queues — each activity call and return goes through the Temporal service
- **Scaling**: Deploy more worker instances to scale horizontally; Temporal handles queue distribution
- **Long-running**: Workflows can run for hours, days, weeks, months, or years efficiently
- **Entity workflows / digital twins**: A common pattern where a workflow corresponds to a real-world entity (e.g., a loyalty customer) and receives signals over its lifetime
- **Human-in-the-loop**: Workflows can wait for human input by simply suspending; they release memory after a few seconds and reconstitute state when the human responds
- **Implementation**: In Python, workflows are classes with `@workflow.defn` decorator; they call activities via `workflow.execute_activity()`
- **Signals, updates, queries**: Additional abstractions on workflows for external interaction — signals for async input, updates for special signals with response, queries for state inspection

## Related
- [[Temporal]] — the platform
- [[TemporalActivities]] — the execution units orchestrated by workflows
- [[DynamicActivity]] — calling activities by name at runtime
- [[EventSourcing]] — the underlying mechanism
- [[HappyPathProgramming]] — the developer philosophy
- [[DurableAgenticLoop]] — applying workflows to agentic loops
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
