---
title: "MLX"
type: entity
tags: [framework, apple, inference, apple-silicon, on-device]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition

MLX is an array framework made by Apple, optimized for Apple Silicon chips (M1 through M5) found in iPhones, iPads, and Macs. Analogous to PyTorch or TensorFlow but purpose-built for Apple hardware. It enables efficient on-device inference and has grown to 1.5M+ downloads with 4,000+ models ported.

## Key Information

- Developed by Apple and optimized specifically for Apple Silicon (M-series chips)
- 1.5M+ downloads, 4,000+ models ported to the MLX ecosystem
- Works with frontier labs for day-zero support of open source models (e.g., Gemma 4)
- Uses GPU for inference, not the Neural Engine (Core ML is needed for Neural Engine)
- Enables running LLMs on-device at high speed (e.g., Gemma 4 at 40 tokens/second on iPhone)
- Large models (hundreds of billions of params) can run on M1 MacBooks via community optimizations
- Turbo Quant enables 4x KV cache reduction and up to 1M context on-device
- Growing ecosystem includes:
  - MLX VLM — for vision-language models (by Prince Canuma)
  - MLX Audio — for speech-to-text, text-to-speech (Marvis), speech-to-speech
  - MLX Video — for video generation
  - MLX Swift LM — for iOS/macOS app integration
- Supports omni models, text-to-speech, and speech-to-speech
- Models sourced from the MLX community on Hugging Face (4,000+ models available)
- Powers LM Studio as a primary inference engine; also powers Liquid AI models
- Enables on-device robotics: Prince Canuma powers a Richie Mini robot with MLX

## Related

- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[Prince Canuma]] — major MLX ecosystem contributor
- [[Neywa Labs]] — company building MLX ecosystem tools
- [[MLX VLM]] — vision framework
- [[MLX Audio]] — audio framework
- [[MLX Video]] — video generation framework
- [[MLX Swift LM]] — iOS/macOS integration library
- [[Marvis]] — TTS model on MLX
- [[Turbo Quant]] — KV cache optimization for MLX
- [[Locally AI]] — app built with MLX
- [[LM Studio]] — supports MLX as an inference engine
- [[Core ML]] — Apple's Neural Engine framework (separate from MLX)
- [[OnDeviceAI]] — core concept enabled by MLX
- [[HuggingFace]] — source for MLX community models
- [[Richie Mini]] — robot powered by MLX
