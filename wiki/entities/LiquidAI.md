---
title: "LiquidAI"
type: entity
tags: [company, ai, edge-models, pre-training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Liquid AI is an AI company focused on building edge models for on-device deployment, developing the Liquid Foundation Models (LFM) family across text, vision, and audio modalities.

## Key Information
- Focuses on edge models for phones, cars, and other memory-constrained devices
- Develops models from 350M to 24B parameters
- Released LFM 2.5 350M (text) and VLM 450M (vision-language model)
- Uses on-device profiling on target hardware (AMD Ryzen, Samsung Galaxy) for architecture optimization
- Employs a full training pipeline: pre-training (28T tokens), SFT, preference alignment (DPO), and RL
- Treats edge models as a distinct category requiring specialized optimization, not scaled-down large models
- Working on LFM 3 with "a ton of crazy experiments"
- Models available on Hugging Face

## Related
- [[MaximeLabonne]] — Head of Pre-training
- [[LFM]] — Liquid Foundation Models product line
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[EdgeModels]] — core product category
- [[HuggingFace]] — distribution platform
