---
title: "AgentSmell"
type: concept
tags: [evaluation, coding-agents, metrics, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Agent smell is a concept for sanity-checking coding agent performance through surface-level metrics: how many times does it call a tool, how many times does it retry, how long does it take. It is a lightweight evaluation approach that complements more rigorous end-to-end and point-in-time testing.

## Key Information
- Coined or popularized by Jared Zoneraich as a way to evaluate agents built on flexible while-loop architectures
- Surface-level metrics: tool call count, retry count, duration
- Not a rigorous evaluation method, but useful for sanity checking and catching regressions
- Complements other eval approaches: end-to-end tests (does it fix the problem?), point-in-time snapshots (should it call this tool at this point?), and backtests (rerun historical data)
- Particularly relevant because simple while-loop architectures are harder to evaluate than deterministic DAGs
- Zoneraich's recommended eval hierarchy: start with backtests (capture historical data, rerun), then point-in-time tests, then end-to-end tests
- Can be implemented as a batch runner that runs headless agents through columns of data and collects statistics

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[DAGvsLoopArchitecture]] — the architecture that makes agent smell necessary
- [[EvalEngineering]] — broader evaluation discipline
- [[HeadlessCodingAgent]] — how agent smell tests are run
