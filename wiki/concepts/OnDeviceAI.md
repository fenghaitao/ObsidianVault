---
title: "OnDeviceAI"
type: concept
tags: [deployment, efficiency, mobile, edge]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
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
- MLX (Apple's framework for Apple Silicon) enables 40 tokens/second on iPhone with 4-bit quantized models
- Model size (1-3 GB) remains the biggest barrier to on-device AI adoption
- Quantization range for usable on-device quality: 4-bit (minimum) to 8-bit (for very small models)
- Gemma 4 demos show full agentic capabilities on-device: skill selection, coding, SVG generation — all in airplane mode
- 10 parallel Gemma instances running on a laptop at 100 tokens/sec via llama.cpp
- Community has put llama.cpp on Nintendo Switch to run Gemma models on-device
- Android Studio supports offline agent mode with Gemma via llama.cpp/vLLM

## Related
- [[Gemma4]] — E2B and E4B are on-device models
- [[EffectiveModels]] — design approach for on-device
- [[PerLayerEmbeddings]] — key enabling technique
- [[OnDeviceAgentic]] — agentic capabilities on-device
- [[Ollama]] — local model runner
- [[MLX]] — Apple framework for on-device inference
- [[LlamaCpp]] — inference framework for on-device demos
- [[Locally AI]] — iOS app for on-device models
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[summary-20260420 - Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind]] — source
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (local models winning for normies)
- [[Local Models for Agents]] — Kitze's prediction that local models win for mainstream
- [[Apple]] — may win with local Siri
- [[Siri]] — potential local agent
- [[Google Pixel]] — already demonstrating local agent capabilities
