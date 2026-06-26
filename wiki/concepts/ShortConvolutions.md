---
title: "ShortConvolutions"
type: concept
tags: [architecture, convolution, latency, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Short convolutions are gated convolution blocks used in Liquid AI's LFM 2 architecture that provide significantly faster inference than alternative attention mechanisms, making them ideal for latency-sensitive edge model deployment.

## Key Information
- Core architectural innovation in LFM 2's hybrid design
- **Speed advantage**: Significantly faster than sliding window attention (Gemma 3), gated Delta Net (Gemma 2.5), gated linear attention, and GQA
- **Memory efficiency**: Uses less memory than alternatives during inference
- **GPU performance**: Maintains high throughput even at very high concurrency levels
- Discovered through on-device profiling on target hardware (AMD Ryzen, Samsung Galaxy S25 Ultra)
- Enables LFM 2 to be faster on both CPU and GPU compared to competing small model architectures

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[LFM]] — model using this architecture
- [[HybridArchitecture]] — broader architectural pattern
- [[OnDeviceProfiling]] — methodology that identified this advantage
- [[EdgeModels]] — deployment context
- [[GQA]] — paired with short convs in LFM 2
