---
title: "HybridArchitecture"
type: concept
tags: [architecture, models, attention, convolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Hybrid architecture in language models refers to combining multiple attention or convolution mechanisms within a single model to balance speed, memory, and reasoning capability, particularly important for small edge models.

## Key Information
- **LFM 2**: Gated short convolutions + GQA (Grouped Query Attention)
- **Gemma 3 270M**: Sliding window attention + GQA
- **Gemma 2.5 0.8B**: Gated Delta Net + gated attention
- Hybrid designs enable faster inference on constrained hardware
- Short convolutions are significantly faster than sliding window attention, gated Delta Net, gated linear attention, and GQA
- Architecture choice directly impacts latency, memory usage, and throughput on target devices

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[ShortConvolutions]] — fastest hybrid component
- [[GQA]] — attention mechanism used in multiple hybrids
- [[SlidingWindowAttention]] — used in Gemma 3
- [[GatedDeltaNet]] — used in Gemma 2.5
- [[GatedLinearAttention]] — alternative compared against
- [[EdgeModels]] — deployment context
