---
title: "Prepare Call"
type: concept
tags: [ai-sdk, agents, lifecycle, callbacks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Prepare Call is an AI SDK v6 lifecycle callback that runs exactly once at the start of an agent invocation. It receives call options and can modify agent parameters (instructions, context, etc.) before the first step of the agent loop begins. It is the primary hook for injecting runtime state into the agent.

## Key Information
- **When It Runs**: Once, at the very beginning of an agent invocation — before any LLM calls or tool executions.
- **Signature**: Receives `{ callOptions }` and can return modified agent parameters.
- **Primary Uses**:
  - **Injecting sandbox into runtime context**: Takes the sandbox from call options and puts it into the agent runtime context so tools can access it.
  - **Loading file system memory**: Reads `memories.md` from the sandbox file system and injects its contents into the agent's instructions/system prompt.
  - **Dynamic instruction assembly**: Composes the final system prompt by combining static instructions with dynamically loaded content (e.g., "Here are your memories: ...").
- **Pattern**: Nico demonstrated loading memories from the sandbox, checking if they exist, and either prepending them to the instructions or noting "no memories yet."
- **Difference from Prepare Step**: Prepare Call runs once per agent invocation. Prepare Step runs before every individual step within the agent loop. Use Prepare Call for setup that should happen once; use Prepare Step for per-step adjustments.
- **Context Injection**: The critical pattern: `prepareCall` receives call options → injects values into context → tools access context in their execute functions.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Tool Loop Agent]] — the agent primitive
- [[Prepare Step]] — the per-step counterpart
- [[Agent Runtime Context]] — where values are injected
- [[Call Options Schema]] — where call options are defined
- [[File System Memory]] — memory loaded during prepare call
- [[AgentLoop]] — the execution cycle
