---
title: "Context Parallelism"
type: concept
tags: [training, memory-optimization, attention, parallelism, long-context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Context parallelism is a technique for distributing the attention computation of transformer models across multiple GPUs by partitioning the sequence dimension rather than replicating the full attention matrix on every device. Instead of each GPU computing multi-head attention over the entire sequence, different GPUs handle different attention heads over the full sequence, communicating activations as needed.

## Key Information
- **Core insight**: Attention is the dominant memory consumer in long-context training due to O(n²) pairwise interactions
- **How it works**: Each GPU computes attention for a subset of heads over the full sequence, then activations are aggregated across devices
- **Memory reduction**: Approximately linear scaling with number of GPUs (e.g., ~8× reduction on 8 GPUs)
- **Compatibility**: Works with optimized attention kernels like [[FlashAttention]] (1, 2, 3, 4)
- **Primary implementation**: [[DeepSpeed Ulysses]] by Microsoft is the most well-known context parallelism technique
- **Advanced variant**: [[Untitled Ulysses]] (U-Pipe) further subdivides head computation into time-sequenced chunks that reuse GPU buffers, pushing context to 5M tokens
- **GPU saturation insight**: Computing even one set of attention heads is often enough to saturate GPU compute within an iteration, enabling sequential chunk processing without significant throughput loss

## Related
- [[DeepSpeed Ulysses]] — primary implementation
- [[Untitled Ulysses]] — Together AI's chunked variant (U-Pipe)
- [[FlashAttention]] — compatible optimized attention kernel
- [[Long Context Training]] — application domain
- [[Quadratic Attention]] — the bottleneck context parallelism addresses
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
