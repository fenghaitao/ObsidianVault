---
title: "KV Cache"
type: concept
tags: [llm, inference, optimization, gpu, attention, caching]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
KV Cache (Key-Value Cache) is a memory optimization used in autoregressive transformer models that stores previously computed key and value tensors from attention layers, avoiding recomputation for each new token. The cache can be dynamic (growing with sequence length) or static (pre-allocated at fixed size).

## Key Information
- Dynamic KV cache: grows with input size, more memory-efficient for variable-length inputs
- Static KV cache: pre-allocated at a fixed maximum size, uses more RAM upfront but enables further GPU optimizations
- Dynamic KV cache prevents CUDA graph capture because the graph shape changes with input length
- Switching from dynamic to static KV cache was a key step in optimizing Coqui 3 TTS from 0.8x to 5.8x real-time factor
- Static KV cache enables CUDA graph capture, which keeps all computation on the GPU without CPU-GPU coordination
- Trade-off: static cache uses more RAM but significantly improves inference speed
- Also relevant for KV cache compression techniques to reduce memory usage for long contexts

## Related
- [[CUDA Graph Capture]] — optimization enabled by static KV cache
- [[KV Cache Compression]] — techniques for reducing KV cache size
- [[Real-Time Factor]] — performance metric improved
- [[Coqui]] — TTS model optimized with static KV cache
- [[Ahead-of-Time Compilation]] — related optimization concept
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
