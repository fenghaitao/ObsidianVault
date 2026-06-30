---
title: "Memory Bandwidth"
type: concept
tags: [hardware, inference, performance, bottleneck]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Memory bandwidth is the rate at which data can be read from or written to memory, measured in GB/s. For memory-bound AI inference (especially the decode phase), memory bandwidth is the primary determinant of tokens-per-second performance.

## Key Information
- One of three critical metrics for local inference alongside memory capacity and energy per byte
- Determines how fast model weights and KV caches can be loaded during auto-regressive token generation
- Consumer hardware comparison: Mac Studio (~800 GB/s unified memory), RTX 5090 (~1.5 TB/s GDDR7), Nvidia Spark (273 GB/s), MacBook M4 Max (546 GB/s)
- Higher memory bandwidth enables faster decode but typically comes with less total memory capacity (GPU VRAM vs unified memory)
- The ratio of memory capacity to memory bandwidth matters: high ratios (Mac Studio) are good for large models but slower; low ratios (RTX) are fast but can't fit large models
- This tradeoff drives the case for heterogeneous computing: use high-bandwidth hardware for latency-sensitive decode, high-capacity hardware for fitting large models
- Dense models benefit more from high bandwidth; sparse MOE models benefit more from high capacity

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Memory-Bound vs Compute-Bound]] — the context for why bandwidth matters
- [[Heterogeneous Computing]] — strategy for balancing bandwidth and capacity
- [[Intelligence Per Joule]] — metric that incorporates bandwidth efficiency
- [[Apple]] — unified memory architecture with high capacity, moderate bandwidth
- [[Nvidia]] — GDDR memory with high bandwidth, lower capacity
