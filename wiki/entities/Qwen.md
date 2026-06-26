---
title: "Qwen"
type: entity
tags: [model, alibaba, open-source, small-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md"]
last_updated: 2026-06-26
---

## Definition
Qwen is Alibaba's family of open-source language models. Qwen 3.5 0.8B is cited as an example of a small model that is a scaled-down version of larger models, exhibiting high doom loop rates (over 50%) in reasoning mode.

## Key Information
- Qwen 3.5 0.8B in reasoning mode shows over 50% doom loop rates on complex tasks
- Described as a "scaled-down version of bigger models" rather than being purpose-built for edge deployment
- Contrasts with Liquid AI's approach of treating edge models as a distinct category
- Popular base model for RL and fine-tuning work in the industry

- Qwen 3.6+ is available for free via OpenRouter and can be used as a cost-effective agent in Paperclip for simpler tasks
- Qwen models are available to run on-device via Locally AI with MLX on iPhone

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[LFM]] — contrasting edge-first approach
- [[DoomLoop]] — problem particularly severe in this model
- [[ReinforcementLearningWithLLMs]] — commonly applied to Qwen models
- [[Paperclip]] — agent orchestrator using Qwen via OpenRouter for BYO-agent
- [[OpenRouter]] — provides access to free Qwen models
- [[Locally AI]] — iOS app supporting Qwen on-device
