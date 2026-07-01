---
title: "DeepSpeed Ulysses"
type: concept
tags: [training, memory-optimization, context-parallelism, microsoft, attention]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
DeepSpeed Ulysses is a context parallelism technique introduced by Microsoft that distributes multi-head attention computation across GPUs by assigning each GPU responsibility for a subset of attention heads over the full sequence length. Activations are communicated between GPUs as needed and aggregated to produce the final attention output.

## Key Information
- **Origin**: First introduced by [[Microsoft]] as part of the DeepSpeed framework
- **Mechanism**: Instead of computing all attention heads on every GPU, each GPU computes one attention head over the entire sequence, then results are aggregated
- **Memory reduction**: ~8× reduction in attention activation memory on 8 GPUs
- **Kernel compatibility**: Works with all versions of [[FlashAttention]] (1-4) for optimized attention computation
- **Limitation**: Even with Ulysses, fitting beyond 3 million tokens on a single 8×H100 node requires additional techniques like [[Activation Checkpointing]], [[Activation Offloading]], and [[Sequence Parallelism]]
- **Extended by**: [[Untitled Ulysses]] (U-Pipe) from Together AI, which further subdivides head computation into sequential chunks

## Related
- [[Context Parallelism]] — parent technique category
- [[Untitled Ulysses]] — Together AI's extension (U-Pipe)
- [[Microsoft]] — creator
- [[FlashAttention]] — compatible attention kernel
- [[DeepSpeed]] — framework containing Ulysses
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
