---
title: "GroupedQueryAttention"
type: concept
tags: [architecture, attention, efficiency, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Grouped Query Attention (GQA) is an attention optimization where multiple query heads share the same key and value heads, reducing memory and computational cost while maintaining performance.

## Key Information
- In Gemma 4's local layers: 2 queries share the same key and value heads
- In Gemma 4's global layers: 8 queries share the same key and value heads
- To compensate for reduced KV heads in global layers, the key-value head length is doubled to 512 (vs. 256 in local layers)
- Provides significant performance improvements without massive memory cost increases
- Applied across all Gemma 4 model sizes with the 8:1 ratio for global layers

## Related
- [[Gemma4]] — uses GQA across all models
- [[InterleavedLocalGlobalAttention]] — complementary attention pattern
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[MultiQueryAttention]] — extreme variant with single shared KV
- [[RepeatKV]] — related inference optimization repeating KV slices
- [[SelfAttentionMechanism]] — standard multi-head attention
