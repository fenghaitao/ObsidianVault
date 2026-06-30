---
title: "Agent Runtime Context"
type: concept
tags: [ai-sdk, agents, state-management, tools, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Agent Runtime Context is an AI SDK v6 pattern for sharing arbitrary state (data, variables, functions) across all tool executions within a single agent run. It is analogous to React Context — a provider makes values available, and any nested component (tool) can access them — but operates within the agent runtime across steps rather than a component tree.

## Key Information
- **Mechanism**: In the `prepareCall` function (runs once per agent invocation), values are injected into a context object. Tools access this context via the second argument of their `execute` function.
- **Primary Use Case**: Making the sandbox instance available to all tools. The sandbox is passed as a call option, injected into context in `prepareCall`, and then accessed by the bash tool's `execute` function to run commands.
- **Access Pattern**: Tools receive `(input, { context })` in their execute function. The context contains whatever was injected during `prepareCall`.
- **Upcoming AI SDK v7 Feature**: Context will be typed — tools can declare what context they require, and the agent definition will throw a TypeScript error if required context is not provided. Nico described this as "directly a result of me pestering Lars for 3 months."
- **Scope**: Context is shared across all steps of a single agent run, not across separate agent invocations. Each invocation starts fresh.
- **Difference from Agent Context (LLM Context)**: This is "runtime context" (state sharing for tools), not to be confused with LLM context (the message history sent to the model). Nico acknowledged the term is "loaded" but chose it because of the React Context analogy.
- **Why Not Global State**: The functional approach (context injected fresh each time) makes reasoning easier — each invocation starts with a clean slate, avoiding stale state bugs common with global singletons.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Tool Loop Agent]] — the agent primitive using this pattern
- [[Call Options Schema]] — how values enter the context
- [[Prepare Call]] — where context is populated
- [[BashTool]] — primary consumer of sandbox context
- [[AgentLoop]] — the execution cycle where context is shared
