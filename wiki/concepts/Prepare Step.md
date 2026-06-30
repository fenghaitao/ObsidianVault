---
title: "Prepare Step"
type: concept
tags: [ai-sdk, agents, lifecycle, callbacks, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Prepare Step is an AI SDK v6 lifecycle callback that runs before every individual step within the agent loop. It receives the current state (messages, context, model, step number, step data) and can return modified parameters for that step, enabling dynamic context manipulation mid-run.

## Key Information
- **When It Runs**: Before every step in the agent loop — every LLM call, every tool execution decision.
- **What It Receives**: Messages (current message state), context, model being used, step number, and step data (what has happened so far).
- **What It Can Return**: Any of the top-level parameters — modified messages, different model, altered context.
- **Primary Use Case — Sliding Window Context Filtering**: `if (stepNumber >= 20) { return { messages: messages.slice(-5) } }` — only keep the most recent 5 messages after step 20. This implements a sliding context window that activates after a threshold.
- **Why Functional**: The prepare step is a pure function that starts fresh at every invocation. It receives the aggregated message state, computes a return value, but does not mutate or persist state. This makes it easy to reason about — no stale state bugs.
- **Advanced Pattern — Context Pruning**: Developers can strip specific tool calls, filter by message role, or remove certain part types based on step conditions.
- **Relationship to Context Engineering**: This is the AI SDK's mechanism for context manipulation between steps. Nico contrasted this with more complex approaches like message mapping in the route handler, noting that prepare step runs at the right abstraction level (within the agent loop, not at the HTTP boundary).
- **Cache Consideration**: Nico warns that aggressive message filtering (compaction) invalidates the LLM input cache. His preference: avoid compaction, use sub-agents instead.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Tool Loop Agent]] — the agent primitive
- [[Prepare Call]] — the once-per-invocation counterpart
- [[AgentLoop]] — the execution cycle where steps occur
- [[Context Management]] — broader context handling
- [[Input Cache vs Compaction]] — tradeoff relevant to prepare step strategies
- [[Compacting]] — the technique prepare step can implement
- [[SubAgents]] — preferred alternative to aggressive compaction
