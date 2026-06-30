---
title: "Server-Side Compaction"
type: concept
tags: [ai, context-management, compaction, claude-code, anthropic, long-running-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Server-Side Compaction is a Claude Code feature where context window compaction (summarization and truncation of older conversation turns) happens on the server side rather than the client side, enabling agents to run indefinitely without hitting context limits on the client machine.

## Key Information
- **Indefinite Runs**: With server-side compaction, "these models can now just run indefinitely" — compaction happens on the server, removing client-side context constraints
- **Release Timing**: Shipped alongside Opus 4.6 and Sonnet 4.6, along with agent teams
- **Shift from Session Resetting**: Before server-side compaction, long-running harnesses relied on fresh context windows per feature. After this release, single continuous sessions became viable for very long runs
- **Enables Simplified Harnesses**: Server-side compaction, combined with Opus 4.6's improved context handling, allowed Anthropic to drop context resetting between sessions and run evaluator only at end of generation
- **Not a Complete Solution**: Compaction alone doesn't guarantee coherence — "lossy summaries really drift." Structured hand-offs and clean contexts remain important patterns
- **Relationship to Context Anxiety**: Server-side compaction reduces context anxiety by preventing the model from feeling it's approaching a hard limit
- **1M Context GA Complement**: Combined with 1 million token context window GA, server-side compaction makes very long single-session runs practical

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Compaction]] — the general technique
- [[Auto-compaction]] — automatic compaction mechanism
- [[One Million Context Window]] — complementary feature
- [[Context Anxiety]] — problem compaction helps mitigate
- [[Context Rot]] — related context degradation
- [[Context Management]] — broader category
- [[Harness Evolution]] — how compaction changed harness design
- [[ClaudeCode]] — product with this feature
