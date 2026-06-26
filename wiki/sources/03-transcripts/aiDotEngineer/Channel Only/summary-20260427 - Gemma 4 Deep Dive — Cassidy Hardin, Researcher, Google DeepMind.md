---
title: "Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md"
date: 2026-04-27
ingested: 2026-06-26
---

## Core Thesis
Gemma 4 is Google DeepMind's latest open-source model family that sets a new precedent for small model performance through architectural innovations (interleaved local/global attention, grouped query attention, mixture of experts, per-layer embeddings) and native multimodality (vision, text, audio), all released under the Apache 2.0 license for broader developer accessibility.

## Key Points
- **Four model sizes**: 31B dense (advanced reasoning, ranked #3 on LM Arena), 26B MoE (first Gemma MoE, 3.9B active params), effective 4B, effective 2B (on-device with audio support)
- **Architecture innovations**: 5:1 interleaving of local-to-global attention layers with sliding windows (512-1024 tokens); grouped query attention (2:1 local, 8:1 global with doubled KV head length); per-layer embeddings (PLE) stored in flash memory for on-device efficiency
- **MoE architecture**: One shared router expert (3x size) always active, 128 total experts with 8 activated per forward pass
- **Multimodality**: Native vision (variable aspect ratios and resolutions with 5 soft token budgets), audio (305M parameter conformer with mel spectrogram tokenizer) in E2B/E4B
- **License**: Apache 2.0 for easier developer integration from testing to deployment
- **Availability**: Self-host via Hugging Face, Kaggle, Ollama; cloud-hosted via AI Studio and Vertex AI

## Entities
- [[CassidyHardin]] — Researcher at Google DeepMind, presenter
- [[Gemma4]] — Latest open-source model family from Google DeepMind
- [[Gemma3]] — Previous generation Gemma models
- [[GoogleDeepMind]] — Google's AI research division
- [[HuggingFace]] — Model hosting platform
- [[Kaggle]] — Data science and model hosting platform
- [[Ollama]] — Local model runner
- [[AIStudio]] — Google's AI prototyping platform
- [[VertexAI]] — Google Cloud's AI platform

## Concepts
- [[MixtureOfExperts]] — Architecture with shared router expert and 128 total experts
- [[PerLayerEmbeddings]] — Per-layer embedding tables stored in flash memory for on-device efficiency
- [[InterleavedLocalGlobalAttention]] — 5:1 ratio of local to global attention layers
- [[GroupedQueryAttention]] — Grouping queries to share key/value heads for efficiency
- [[VariableAspectRatios]] — Support for different image aspect ratios with spatial positional encoding
- [[VariableResolution]] — User-selectable resolution and soft token budget for images
- [[MultimodalModels]] — Natively multimodal models handling vision, text, and audio
- [[OnDeviceAI]] — Models designed to run locally on phones, iPads, and laptops
- [[Apache2License]] — Permissive open-source license adopted by Gemma 4
- [[EffectiveModels]] — Models with fewer operating parameters than total representational parameters
- [[SlidingWindowAttention]] — Local attention layers attending to limited preceding tokens
- [[Conformer]] — Audio encoder architecture combining transformers with convolutional layers
- [[AudioTokenizer]] — Processes raw audio through mel spectrogram into soft tokens
- [[AgenticWorkflows]] — Autonomous task execution supported by larger Gemma models
- [[OpenSourceModels]] — Publicly available model weights enabling self-hosting and customization

## Related
- [[summary-20260105 - Welcome to AIE CODE - Jed Borovik, Google DeepMind]] — earlier Google DeepMind presentation
