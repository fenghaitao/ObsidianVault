---
title: "LFM"
type: entity
tags: [model, small-model, edge, liquid-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Liquid Foundation Models (LFM) are a family of small AI models developed by Liquid AI, ranging from 350M to 24B parameters, designed for on-device edge deployment across text, vision, and audio.

## Key Information
- **LFM 2 architecture**: Hybrid design with gated short convolutions and GQA (Grouped Query Attention)
- **Embedding efficiency**: Only ~10% of parameters in embedding layer, maximizing effective parameters for reasoning
- **LFM 2.5 350M**: Text model pre-trained on 28 trillion tokens (far beyond Chinchilla scaling laws)
- **VLM 450M**: Vision-language model for multimodal edge tasks
- **On-device profiling**: Architecture optimized via profiling on AMD Ryzen Max Plus 395 and Samsung Galaxy S25 Ultra
- **Performance**: Significantly faster inference and lower memory usage than Gemma 3 and Gemma 2.5 alternatives
- **Specialization**: Optimized for data extraction and tool use, not general-purpose chat
- **Doom loop reduction**: Achieved near-zero doom loop rates through DPO + RL pipeline
- Available on Hugging Face

## Related
- [[LiquidAI]] — developer company
- [[MaximeLabonne]] — Head of Pre-training
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[EdgeModels]] — deployment category
- [[ShortConvolutions]] — key architectural innovation
- [[GQA]] — attention mechanism used
- [[DoomLoop]] — problem addressed in training pipeline
