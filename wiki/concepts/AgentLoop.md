---
title: "AgentLoop"
type: concept
tags: [agents, design, architecture, claude-code, ai-sdk]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
The agent loop is the core execution cycle of an autonomous agent, structured in three parts: gather context, take action, and verify work. This is the recommended design pattern for building agents with the Claude Agent SDK. In AI SDK v6, the `ToolLoopAgent` primitive encapsulates this loop, managing LLM calls, tool calls, and result feeding automatically. In Demand-Driven Context, the agent loop is extended with a failure-and-curation cycle.

## Key Information
- **Gather context**: The agent finds the information it needs — grepping files, searching emails, querying databases. Often underthought; creative search interface design is critical.
- **Take action**: The agent does its work using tools, bash, or code generation. Having the right action modalities for the task is essential.
- **Verify work**: The agent checks its output. Should happen everywhere, not just at the end. Deterministic verification (rules, heuristics) is preferred; sub-agent verification becomes more viable as models improve.
- A planning step can be inserted between gathering context and taking action, but adds latency
- The Agent SDK includes a to-do tool that agents use to maintain and check off tasks during the loop
- The number one meta-learning for designing an agent loop: read the transcripts over and over, figure out what the agent is doing and why, and help it
- Agents that have strong verification steps are the best candidates for becoming very general
- **Demand-Driven Context Extension**: The standard agent loop (gather → act → verify) is extended with: (4) fail and surface gaps → (5) request missing knowledge from domain expert → (6) curate new knowledge for reuse. This transforms the loop from a pure execution pattern into a knowledge-building pattern.
- **AI SDK v6 ToolLoopAgent**: The `ToolLoopAgent` encapsulates the agent loop into a reusable, object-oriented primitive. It manages the LLM ↔ tool call cycle, passes tool results back as messages, and provides lifecycle hooks (`prepareCall`, `prepareStep`) for injecting state and modifying behavior between steps. Tools access shared state via the agent runtime context. The loop continues until the agent produces a final text response.

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source (AI SDK v6 ToolLoopAgent)
- [[Verification in Agentic Loops]] — the verification step in detail
- [[ToolsVsBashVsCodeGen]] — the action modalities
- [[AgenticSearchInterface]] — designing the gather context step
- [[Hooks]] — mechanism for inserting verification
- [[Demand-Driven Context]] — methodology extending the agent loop
- [[Agent Failure as Discovery]] — the failure step in the extended loop
- [[Knowledge Curation]] — the curation step in the extended loop
- [[Tool Loop Agent]] — AI SDK v6's agent primitive implementing this pattern
- [[Prepare Call]] — lifecycle callback for agent setup
- [[Prepare Step]] — lifecycle callback for per-step adjustments
- [[Agent Runtime Context]] — state sharing across loop steps
- [[AISDK]] — the framework
