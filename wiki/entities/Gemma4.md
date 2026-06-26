---
title: "Gemma4"
type: entity
tags: [model, google, deepmind, open-source, multimodal, gemma]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Gemma 4 is Google DeepMind's latest family of open-source models, released under Apache 2.0 license, featuring four sizes (31B dense, 26B MoE, E4B, E2B) with native multimodality and significant architectural innovations setting a new precedent for small model performance.

## Key Information
- **31B dense**: State-of-the-art multimodal model for advanced reasoning, ranked #3 on LM Arena global leaderboard, 256K context length, supports thinking, function calling, and structured JSON outputs
- **26B MoE**: First Gemma mixture of experts model, 128 total experts with 8 activated per forward pass (3.9B active parameters), one shared router expert always active
- **E4B (effective 4B)**: On-device model with 4B effective parameters, supports text/vision/audio input
- **E2B (effective 2B)**: On-device model with 2.3B effective parameters (5.1B representational), supports text/vision/audio input
- **Architecture**: 5:1 interleaved local-to-global attention layers (4:1 for E2B), grouped query attention, per-layer embeddings (PLE) in flash memory
- **Multimodality**: 550M parameter vision encoder (31B/26B), 150M parameter vision encoder (E2B/E4B), 305M parameter audio conformer (E2B/E4B)
- **License**: Apache 2.0
- **Availability**: Hugging Face, Kaggle, Ollama (self-host); AI Studio, Vertex AI (cloud-hosted for 31B/26B)

## Related
- [[CassidyHardin]] — presenter
- [[Gemma3]] — previous generation
- [[GoogleDeepMind]] — creator
- [[MixtureOfExperts]] — architecture used in 26B
- [[PerLayerEmbeddings]] — on-device optimization
- [[InterleavedLocalGlobalAttention]] — attention pattern
- [[GroupedQueryAttention]] — attention optimization
- [[MultimodalModels]] — native multimodality
- [[OnDeviceAI]] — target for E2B/E4B
- [[Apache2License]] — license
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
