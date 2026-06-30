---
title: "EffectiveModels"
type: concept
tags: [architecture, efficiency, on-device, parameters]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md"]
last_updated: 2026-06-26
---

## Definition
Effective Models are AI models where the number of parameters required to operate the model (effective parameters) is smaller than the total number of representational parameters, achieved through techniques like per-layer embeddings stored in flash memory.

## Key Information
- Gemma 4's E2B has 2.3 billion effective parameters with 5.1 billion representational parameters
- Gemma 4's E4B has 4 billion effective parameters
- Designed and optimized for best on-device performance on phones and laptops
- Made possible through Per-Layer Embeddings (PLE) stored in flash memory rather than VRAM
- Embedding dimension in PLE tables is only 256, significantly reduced from full model dimension
- Significantly outperform prior generations of Gemma small models

## Related
- [[Gemma4]] — E2B and E4B are effective models
- [[PerLayerEmbeddings]] — enabling technique
- [[OnDeviceAI]] — primary use case
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
