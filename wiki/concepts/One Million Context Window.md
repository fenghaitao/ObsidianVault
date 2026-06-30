---
title: "One Million Context Window"
type: concept
tags: [ai, context-management, claude, anthropic, long-running-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
The 1 Million Context Window is a Claude feature that provides a 1 million token context, released as Generally Available (GA). It dramatically expands the amount of information an agent can hold in a single session, reducing the need for context resetting and enabling longer autonomous runs.

## Key Information
- **GA Release**: Shipped as Generally Available alongside Opus 4.6 and Sonnet 4.6
- **Impact on Harness Design**: With 1M context, single continuous sessions become viable — "maybe you can just run a lot within a single context window instead of necessarily needing new sessions all the time"
- **Combined with Server-Side Compaction**: The combination of 1M context + server-side compaction enables indefinite agent runs in a single session
- **Shift in Approach**: Earlier harnesses relied on fresh context windows per feature. 1M context changes the calculus — less need for session management complexity
- **Smart Zone / Dumb Zone**: Even with 1M context, models may perform differently at different context depths. The "smart zone" is approximately the first 100K tokens; beyond that, performance may degrade
- **Harness Evolution**: As context windows grow, harness components designed to work around context limitations become less necessary. "Things start shifting over time"
- **Comparison**: Previous context windows were more constrained (e.g., 200K for Claude 3.5 Sonnet). The jump to 1M is a qualitative change in what's possible

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Server-Side Compaction]] — complementary feature
- [[Context Management]] — broader category
- [[Context Anxiety]] — problem larger windows help mitigate
- [[Context Rot]] — still relevant even with large windows
- [[Smart Zone and Dumb Zone]] — performance variation within the window
- [[Harness Evolution]] — how larger windows change harness design
- [[Compaction]] — technique that works alongside large windows
- [[ClaudeCode]] — product with this capability
