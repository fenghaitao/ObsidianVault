---
title: "Modular Speech Pipeline"
type: concept
tags: [speech, architecture, tts, stt, on-device-ai, mlx, composability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
A Modular Speech Pipeline is an architecture for on-device speech systems where automatic speech recognition (ASR), language model (LLM), and text-to-speech (TTS) components are independently selectable and chainable. This allows custom speech experiences tailored to hardware budgets by choosing different models for each stage.

## Key Information
- Three-stage architecture: ASR → LLM → TTS, where each stage is independently configurable
- Users select which ASR model, which language model, and which TTS model to use
- Enables adjustment to hardware budget: lighter models for M1, heavier models for M5
- Implemented in MLX Audio by Prince Canuma (Neywa Labs)
- Supports both Python (faster iteration) and Swift (native experiences)
- Benefits: flexibility, hardware-adaptive, future-proof (swap individual components as models improve)
- Contrast with end-to-end speech-to-speech models which are less customizable
- Enables building custom speech experiences for every hardware tier from M1 to latest

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source
- [[MLX Audio]] — framework implementing this architecture
- [[Marvis]] — TTS component in the pipeline
- [[Cascaded Systems (Voice)]] — related concept
- [[OnDeviceAI]] — core concept
