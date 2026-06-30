---
title: "Heterogeneous Computing"
type: concept
tags: [hardware, inference, distributed-computing, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Heterogeneous computing for AI inference is the strategy of using different types of hardware for different parts of the inference workload, such as running prefill on a high-compute GPU and decode on a high-memory-bandwidth device, to optimize price-to-performance.

## Key Information
- Core strategy in EXO Labs' approach to local inference
- Based on the prefill vs decode distinction: prefill is compute-bound (needs FLOPs), decode is memory-bound (needs bandwidth)
- Practical example: run prefill on Nvidia Spark (4x more compute, 273 GB/s bandwidth) and decode on MacBook (546 GB/s bandwidth) for ~2x end-to-end speedup on large prompts
- Also applies to splitting different model layers across devices based on their compute/memory characteristics
- Already happening in data centers: Groq chips (high bandwidth) paired with Nvidia GPUs (high compute); Cerebras paired with AWS Trainium
- Current optimal local setup combines both: Mac Studio/Book for memory capacity + RTX 5090 or Spark for compute
- EXO aims to make this seamless — install the app, connect devices any way, and it figures out optimal distribution
- Today's challenge: no single consumer device has both high memory capacity and high memory bandwidth
- May evolve toward specialized chips for different parts of the stack as architectures stabilize

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Memory-Bound vs Compute-Bound]] — the technical basis for this strategy
- [[Memory Bandwidth]] — key hardware characteristic
- [[EXO]] — app that automates heterogeneous distribution
- [[Prefill-Decode Disaggregation]] — specific pattern within heterogeneous computing
- [[DGX Spark]] — compute-optimized hardware
- [[Apple]] — memory-capacity-optimized hardware
