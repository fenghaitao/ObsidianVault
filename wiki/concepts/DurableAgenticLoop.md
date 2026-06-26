---
title: "Durable Agentic Loop"
type: concept
tags: [agents, temporal, durability, agentic-loop, production]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
A Durable Agentic Loop is the combination of an LLM-driven agentic loop with Temporal's workflow and activity infrastructure, making the agent durable. Every LLM call and tool invocation is recorded as an event; if the process crashes, the agent resumes from where it left off without re-burning tokens or re-executing completed tool calls.

## Key Information
- **Core mechanism**: The agentic loop is implemented as a Temporal Workflow; LLM calls and tool invocations are Temporal Activities
- **Crash recovery**: If the worker process crashes mid-execution, Temporal replays the event history and resumes from the exact point of failure — no tokens re-burned
- **Network failure recovery**: Temporal retries failed LLM calls and tool invocations with configurable retry policies (exponential backoff, max retries)
- **Visibility**: Every step (LLM call, tool call) is visible in the Temporal UI with inputs, outputs, and timing
- **Scaling**: Multiple workers can pull from the same queues, enabling horizontal scaling of agent execution
- **Integration approach**: OpenAI made the `Runner` class abstract in the Agents SDK; Temporal provides a durable `Runner` implementation
- **LLM durability**: The integration plugin configures retry policies specifically for LLM calls, making them durable without the developer writing a separate activity for each LLM invocation
- **Tool durability**: Tools implemented as Temporal Activities automatically get retries and result caching via the `activity_as_tool()` helper
- **Demo proof**: Cornelia killed the worker process mid-execution, restarted it, and the agent resumed from where it left off — the Temporal UI showed the stuck state and subsequent recovery

## Related
- [[AgenticLoop]] — the core pattern
- [[TemporalWorkflows]] — the workflow infrastructure
- [[TemporalActivities]] — the activity infrastructure
- [[DynamicActivity]] — enabling generic tool sets
- [[DurableAgents]] — the broader concept
- [[EventSourcing]] — the underlying mechanism
- [[HappyPathProgramming]] — the developer philosophy
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
