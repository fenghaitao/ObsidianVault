---
title: "PerLayerEmbeddings"
type: concept
tags: [architecture, on-device, efficiency, embeddings]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Per-Layer Embeddings (PLE) is an architectural technique where each transformer layer has its own dedicated embedding table, stored in flash memory rather than VRAM, enabling significant on-device inference improvements without expensive memory costs.

## Key Information
- Each layer has a dedicated embedding table with embedding dimension of 256 (significantly reduced from full model dimension)
- Stored in flash memory instead of VRAM, avoiding the primary memory constraint on phones and laptops
- At the end of each decoder block, the per-layer embedding is looked up (256-dim) and projected up to the full embedding size
- As tokens progress through layers, their embedding representations evolve sequentially
- E2B has 35 layers, E4B has 42 layers
- Enables effective models (E2B, E4B) to significantly outperform prior Gemma small models

## Related
- [[Gemma4]] — uses PLE in effective models
- [[EffectiveModels]] — enabled by PLE
- [[OnDeviceAI]] — primary use case
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
