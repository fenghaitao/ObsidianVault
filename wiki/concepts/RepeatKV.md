---
title: "RepeatKV"
type: concept
tags: [optimization, inference, attention, kv-cache, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Repeat-KV is an inference optimization where key and value heads are trained in small slices and then repeated (e.g., 4 times) during inference, reducing memory usage of the KV cache without significant accuracy degradation.

## Key Information
- Only small slivers of K and V heads are trained; during inference, these are repeated to cover the full number of attention heads
- Reduces memory footprint of the KV cache substantially with minimal accuracy loss
- Related to Multi-Query Attention and Grouped Query Attention, which also reduce KV head count
- Found in LLaMA-style architectures and newer model implementations
- Typical repetition factor is 4 (trained K/V slice repeated 4 times)

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[SelfAttentionMechanism]] — the attention mechanism being optimized
- [[GroupedQueryAttention]] — related KV-sharing attention variant
- [[MultiQueryAttention]] — extreme variant with single shared KV
