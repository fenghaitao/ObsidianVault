---
title: "Qwen"
type: entity
tags: [model, alibaba, open-source, small-model, omnimodel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Qwen is Alibaba's family of open-source language models. Qwen 3.5 0.8B is cited as an example of a small model that is a scaled-down version of larger models, exhibiting high doom loop rates (over 50%) in reasoning mode. Qwen 3 Omni is an omnimodel (~30B parameters) that accepts image, audio, and text inputs and can run on-device.

## Key Information
- Qwen 3.5 0.8B in reasoning mode shows over 50% doom loop rates on complex tasks
- Described as a "scaled-down version of bigger models" rather than being purpose-built for edge deployment
- Contrasts with Liquid AI's approach of treating edge models as a distinct category
- Popular base model for RL and fine-tuning work in the industry
- Qwen 3 Omni: ~30 billion parameter omnimodel accepting image, audio, and text inputs — can run on-device
- Qwen 3.6+ is available for free via OpenRouter and can be used as a cost-effective agent in Paperclip for simpler tasks
- Qwen models are available to run on-device via Locally AI with MLX on iPhone
- **BullshitBench performance**: Qwen models perform relatively well on nonsense detection — "not too bad" — ranking among the better performers after Claude/Sonnet models

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
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (BullshitBench decent performer)
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source (Qwen 3 Omni)
- [[BullshitBench]] — benchmark where Qwen performs well
- [[Nonsense Detection]] — capability where Qwen is above average
- [[Omnimodels]] — Qwen 3 Omni is an omnimodel
- [[MLX]] — framework for running Qwen on-device
