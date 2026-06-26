---
title: "AgentLoop"
type: concept
tags: [agents, design, architecture, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
The agent loop is the core execution cycle of an autonomous agent, structured in three parts: gather context, take action, and verify work. This is the recommended design pattern for building agents with the Claude Agent SDK.

## Key Information
- **Gather context**: The agent finds the information it needs — grepping files, searching emails, querying databases. Often underthought; creative search interface design is critical.
- **Take action**: The agent does its work using tools, bash, or code generation. Having the right action modalities for the task is essential.
- **Verify work**: The agent checks its output. Should happen everywhere, not just at the end. Deterministic verification (rules, heuristics) is preferred; sub-agent verification becomes more viable as models improve.
- A planning step can be inserted between gathering context and taking action, but adds latency
- The Agent SDK includes a to-do tool that agents use to maintain and check off tasks during the loop
- The number one meta-learning for designing an agent loop: read the transcripts over and over, figure out what the agent is doing and why, and help it
- Agents that have strong verification steps are the best candidates for becoming very general

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[Verification in Agentic Loops]] — the verification step in detail
- [[ToolsVsBashVsCodeGen]] — the action modalities
- [[AgenticSearchInterface]] — designing the gather context step
- [[Hooks]] — mechanism for inserting verification
