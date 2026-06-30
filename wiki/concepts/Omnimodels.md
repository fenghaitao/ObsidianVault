---
title: "Omnimodels"
type: concept
tags: [model, multimodal, vision, audio, text, on-device-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Omnimodels are AI models that accept multiple input modalities — image, audio, and text — either individually or in any combination. Unlike traditional multimodal models that may only handle text+image, omnimodels natively support vision, audio, and text as inputs.

## Key Information
- Accept image, audio, and text as input or any combination of the three
- Key examples: Gemma 4 "e" variants (E2B, E4B), Qwen 3 Omni (~30B parameters)
- Enable richer on-device interactions: point camera, speak commands, get text/voice responses
- Gemma 4 E2B/E4B are Google DeepMind's omnimodel variants, available day-zero on MLX
- Qwen 3 Omni is a larger omnimodel (~30B params) from Alibaba, also runnable on-device
- Enable accessibility use cases: blind users can speak + use camera to understand surroundings
- Run on Apple Silicon via MLX (Mac, iPhone, iPad)
- Key enabler for on-device voice agents that can see, hear, and respond

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[Gemma 4]] — "e" variants are omnimodels
- [[Qwen]] — Qwen 3 Omni is an omnimodel
- [[MLX]] — framework for running omnimodels on-device
- [[OnDeviceAI]] — core concept
- [[Accessibility AI]] — key use case for omnimodels
