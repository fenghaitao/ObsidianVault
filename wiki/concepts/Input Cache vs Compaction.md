---
title: "Input Cache vs Compaction"
type: concept
tags: [context-management, llm, caching, performance, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Input Cache vs Compaction describes a fundamental tradeoff in agent context management: compacting (removing old messages to stay within context limits) invalidates the LLM's input cache, potentially increasing latency and cost more than the tokens saved. With modern million-token context windows, avoiding compaction in favor of caching and sub-agent delegation may be the better strategy.

## Key Information
- **The Tradeoff**: Removing messages from context (compaction) changes the prefix that the LLM uses for KV-cache lookups. Every compaction invalidates the input cache, forcing the model to recompute attention for all tokens — this can cost more in latency and compute than the tokens saved.
- **Nico's Experience**: His coding agent ran for 104 minutes, used 316 tool calls, changed 29 files, and used only 32% of GPT-4's context window — with zero compaction. His cache token read ratio was 95%.
- **Historical Context**: When token windows were 400K (Opus, GPT-5-3 Codex), compaction was more necessary because hitting 40% of context happened quickly. With million-token windows, this is less of an issue.
- **Alternative Strategies**:
  1. **Sub-agents**: Delegate independent work to sub-agents that return ~500 token summaries, keeping the main thread's context small without compaction.
  2. **Handoff tool**: Agent calls a handoff tool that generates context for a fresh thread, then starts a new session — similar to Amp Code's approach.
  3. **Sub-agent territory**: Push as much work as possible into sub-agents to avoid lossy LLM summarization.
- **The Compaction Danger**: Nico cites the infamous case of a Meta AI head who asked her agent to archive emails — auto-compaction removed her initial "don't do this" instruction, and the agent deleted her entire inbox. Compaction is lossy and can remove critical instructions.
- **Cache Read Ratio as Metric**: Nico tracks cache token read ratio (95% in his agent) as a key performance metric — higher is better for speed, cost, and reliability.
- **Vercel Scale**: Nico's agent processed 3.8 billion tokens with a 91% cache read ratio across 23 users at Vercel, responsible for ~350 PRs.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[Compacting]] — the technique being evaluated
- [[Context Management]] — broader context handling
- [[SubAgents]] — preferred alternative to compaction
- [[Prepare Step]] — where compaction would be implemented
- [[AgentLoop]] — the execution cycle
- [[Context Budget]] — related concept
- [[ContextRot]] — problem compaction tries to solve
- [[TokenBudget]] — related constraint
