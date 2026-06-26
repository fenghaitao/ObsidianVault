---
title: "OnDeviceProfiling"
type: concept
tags: [optimization, hardware, architecture, edge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
On-device profiling is the practice of testing and optimizing model architectures by running them on actual target hardware (e.g., specific CPUs, phones) rather than relying on theoretical benchmarks, to find the right operators and architecture for real-world performance.

## Key Information
- Used by Liquid AI to optimize LFM 2 architecture
- **Target hardware**: AMD Ryzen Max Plus 395 (CPU) and Samsung Galaxy S25 Ultra (mobile)
- Enabled discovery that short convolutions are significantly faster than alternatives in practice
- Measures real inference speed, memory usage, and throughput rather than theoretical FLOPs
- Contrasts with purely theoretical architecture design approaches
- Critical for edge models where hardware constraints are the primary bottleneck

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[LFM]] — model optimized through this method
- [[ShortConvolutions]] — architectural choice validated by profiling
- [[EdgeModels]] — deployment context
- [[AMD]] — profiling target hardware
- [[Samsung]] — profiling target hardware
