---
title: "InterleavedLocalGlobalAttention"
type: concept
tags: [architecture, attention, efficiency, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Interleaved Local-Global Attention is an attention pattern that alternates between local layers (attending to a sliding window of preceding tokens) and global layers (attending to all preceding tokens), with the last layer always being global.

## Key Information
- Gemma 4 uses a 5:1 ratio of local to global layers (4:1 for E2B)
- Local layers use a sliding window of 512 tokens (E2B/E4B) or 1,024 tokens (31B/26B)
- Global layers attend to all preceding tokens and remain memory-intensive
- The last layer is always a global layer to ensure full context access
- Provides significant efficiency improvements while passing information through to subsequent layers
- Combined with grouped query attention to further reduce global layer cost

## Related
- [[Gemma4]] — uses this attention pattern
- [[SlidingWindowAttention]] — mechanism used in local layers
- [[GroupedQueryAttention]] — complementary optimization
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
