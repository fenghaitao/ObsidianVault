---
title: "EmbeddingLayerEfficiency"
type: concept
tags: [architecture, models, optimization, parameters]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Embedding layer efficiency is the principle of minimizing the proportion of model parameters dedicated to the embedding layer to maximize effective parameters available for reasoning and knowledge capacity, particularly critical for small models with limited total parameters.

## Key Information
- **Gemma 3 270M**: Embedding layer is 63% of total parameters — mostly an embedding layer
- **Gemma 2.5 0.8B**: Embedding layer is 29% of total parameters
- **LFM 2**: Embedding layer is only ~10% of parameters, maximizing effective parameters
- Large embedding layers result from distillation from teacher models with huge vocabulary sizes
- Embedding parameters don't contribute to reasoning or knowledge capacity — they're overhead
- More efficient embedding means more parameters available for actual computation within the same memory footprint

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[LFM]] — efficient embedding design
- [[Gemma]] — inefficient embedding design
- [[ModelDistillation]] — technique causing large embedding layers
- [[EdgeModels]] — context where parameter efficiency is critical
