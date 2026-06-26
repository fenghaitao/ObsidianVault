---
title: "Temporal Activities"
type: concept
tags: [temporal, activity, durability, retry, distributed-systems]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Temporal Activities are chunks of work — typically external API calls or heavy computation — wrapped with decorators that give them special durability behavior. When an activity is called from a workflow, Temporal automatically provides retries, records the result, and can replay the result without re-executing if recovery is needed.

## Key Information
- **Purpose**: Encapsulate work that might fail (external calls) or work you don't want to redo if something goes wrong
- **Decorator-based**: In Python, functions are wrapped with `@activity.defn`; in TypeScript, the SDK automatically detects activities
- **Automatic retries**: Developers configure retry policies (exponential backoff, max retries, max interval) and Temporal handles the rest
- **Result recording**: Temporal records the result of every successful activity call; on replay, it returns the cached result without re-executing
- **Idempotency**: Activities should ideally be idempotent because Temporal may retry without knowing whether the first invocation succeeded; Temporal does not enforce this but educates developers
- **Standalone activities**: Temporal is releasing standalone activities that can be used without workflows for some durability benefits
- **Dynamic activities**: Activities can be called by name at runtime (`dynamic=True`), enabling generic agentic loops that work with any set of tools
- **Queue-based execution**: Activities are pulled from queues by workers; workers are multi-threaded (typically hundreds of threads)
- **Latency**: Activity calls add tens of milliseconds of overhead for communication with the Temporal server

## Related
- [[Temporal]] — the platform
- [[TemporalWorkflows]] — the orchestrations that compose activities
- [[DynamicActivity]] — calling activities by name at runtime
- [[EventSourcing]] — the mechanism for recording activity results
- [[HappyPathProgramming]] — the developer philosophy
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
