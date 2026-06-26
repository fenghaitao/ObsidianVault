---
title: "Durable Agents"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

# Durable Agents

## Definition

Durable agents are AI agents built on workflow infrastructure that provides durability, resumability, observability, and production reliability. They leverage the workflow pattern to ensure agent state persists across serverless function invocations, enabling long-running agents that can survive failures, pauses, and reconnections.

## Key Information

- **Core Properties**:
  - **Durability**: Agent state and step results are cached; failed steps can be retried without losing progress
  - **Resumability**: Agents can `sleep` for arbitrary durations (days, weeks) and resume from the exact point of suspension
  - **Observability**: Every LLM call and tool call is tracked as a step with inputs, outputs, and events
  - **Stream decoupling**: Agent output streams are independent of the API handler; clients can reconnect at any point
- **Implementation**: In the Workflow DevKit, the `DurableAgent` class wraps the AI SDK's `Agent` with `use step` markers on LLM calls under the hood
- **Use Cases**:
  - Long-running coding agents that may run for hours
  - Cron-like agents that wake up daily to perform tasks
  - Multi-session agents where users disconnect and reconnect
  - Agents requiring human approval at specific steps
- **Production behavior**: Each step (LLM call, tool call) runs in its own serverless instance; the orchestration layer is only invoked briefly to coordinate
- **Temporal approach**: Temporal achieves durability through event sourcing — every LLM call and tool invocation is recorded as an event. If the process crashes, Temporal replays the event history and resumes from where it left off without re-burning tokens. The OpenAI Agents SDK integration makes the `Runner` class abstract so Temporal can provide a durable implementation.
- **Real-world Temporal usage**: Every Snapchat, Airbnb booking, Pizza Hut/Taco Bell order, OpenAI Codex, OpenAI image gen, and Lovable all run on Temporal for durability

## Related

- [[WorkflowDevKit]]
- [[WorkflowPattern]]
- [[ResumableStreams]]
- [[HumanInTheLoopWorkflows]]
- [[StepCaching]]
- [[AgentObservability]]
- [[AISDK]]
- [[Temporal]]
- [[DurableAgenticLoop]]
- [[EventSourcing]]
- [[HappyPathProgramming]]
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
