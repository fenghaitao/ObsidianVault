---
title: "MultiQueryAttention"
type: concept
tags: [architecture, attention, optimization, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Multi-Query Attention (MQA) is an extreme attention optimization where all query heads share a single key and value head, dramatically reducing KV cache memory at the cost of some model quality compared to standard multi-head attention.

## Key Information
- All query heads share one K and one V head, minimizing memory usage
- The extreme end of the KV-sharing spectrum: standard MHA → Grouped Query Attention → Multi-Query Attention (single shared KV)
- Significant memory savings for inference since KV cache size is the dominant memory consumer
- Trade-off: some accuracy degradation compared to full multi-head attention or GQA
- Related to Repeat-KV, which repeats small trained KV slices to achieve similar memory savings

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[GroupedQueryAttention]] — intermediate approach sharing KV across groups of queries
- [[RepeatKV]] — alternative inference optimization reusing KV slices
- [[SelfAttentionMechanism]] — the standard multi-head variant
