---
title: "Happy Path Programming"
type: concept
tags: [temporal, developer-experience, durability, philosophy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
Happy Path Programming is Temporal's core philosophy: developers write only the success path of their business logic, and the platform handles all failure scenarios — retries, state management, crash recovery, and scaling. The developer doesn't write code for "what if the LLM is rate limited," "what if the downstream API is down," or "what if the application crashes."

## Key Information
- **Core promise**: "You as the developer get to program the happy path. You get to program your business logic."
- **What developers don't write**: Retry logic, queue management, state persistence, crash recovery, concurrency control, quorum algorithms
- **What Temporal handles**: Retries with configurable backoff, event sourcing for state, queue-based distribution, automatic crash recovery
- **Real-world impact**: A Temporal customer reported shifting from 25% business logic / 75% operations (with Kafka queues) to 75% business logic / 25% operations after adopting Temporal Cloud
- **AI agent application**: For agents, this means developers write the agentic loop (call LLM, invoke tools, loop back) and Temporal handles LLM rate limiting, tool API failures, and process crashes
- **Logical vs physical processes**: Developers think about processes as logical entities; Temporal maps them to physical processes, handling all the complexity of distribution
- **Freedom**: "It is so freeing to realize that I don't have to think about physical processes anymore"

## Related
- [[Temporal]] — the platform
- [[TemporalWorkflows]] — the business logic
- [[TemporalActivities]] — the execution units
- [[EventSourcing]] — the mechanism enabling this
- [[DurableAgenticLoop]] — applying happy path programming to agents
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
