---
title: "Dynamic Activity"
type: concept
tags: [temporal, activity, dynamic, runtime, agentic-loop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md"]
last_updated: 2026-06-26
---

## Definition
A Dynamic Activity in Temporal is an activity handler configured with `dynamic=True` that can pick up any activity call from a queue regardless of its name. This enables generic agentic loops where the tool set can be swapped without changing the orchestration code — the activity handler looks up the tool function by name at runtime.

## Key Information
- **Dynamic dispatch**: The activity handler receives the activity name as a parameter and looks up the corresponding function at runtime
- **No static registration**: Unlike regular activities, dynamic activities don't need to be registered with a specific name in the worker
- **Generic agentic loops**: Enables a single workflow to work with any set of tools — just swap the tools module without changing the agentic loop code
- **Implementation**: In Python, use `@activity.defn(dynamic=True)`; the handler receives the activity name and arguments, then dispatches to the appropriate function
- **Tool lookup**: Typically implemented as a dictionary mapping tool names to handler functions, loaded at application startup
- **Limitation in demo**: Cornelia's demo required restarting the Python process to swap tool modules, but a full registry with dynamic loading is possible

## Related
- [[TemporalActivities]] — parent concept
- [[TemporalWorkflows]] — the orchestrations using dynamic activities
- [[AgenticLoop]] — the pattern enabled by dynamic activities
- [[DurableAgenticLoop]] — the combination with durability
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
