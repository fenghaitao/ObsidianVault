---
title: "OnDeviceAI"
type: concept
tags: [deployment, efficiency, mobile, edge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
On-Device AI refers to AI models designed and optimized to run locally on consumer hardware (phones, iPads, laptops) without requiring cloud API calls, addressing VRAM constraints as the primary limitation.

## Key Information
- Gemma 4's E2B and E4B models are specifically designed for on-device applications
- VRAM is the largest constraint on phones and laptops for running AI models
- Per-layer embeddings (PLE) stored in flash memory instead of VRAM is a key innovation
- Effective models have fewer operating parameters than total representational parameters (E2B: 2.3B effective, 5.1B representational)
- Supports text, vision, and audio input modalities
- Enables local inference without expensive API calls to remote servers

## Related
- [[Gemma4]] — E2B and E4B are on-device models
- [[EffectiveModels]] — design approach for on-device
- [[PerLayerEmbeddings]] — key enabling technique
- [[Ollama]] — local model runner
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
