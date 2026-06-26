---
title: "Gemma"
type: entity
tags: [model, google, small-model, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Gemma is Google's family of small language models, including Gemma 3 270M and Gemma 2.5 0.8B, which use hybrid architectures but have disproportionately large embedding layers due to distillation from large teacher models.

## Key Information
- **Architecture**: Gemma 3 270M uses sliding window attention + GQA hybrid; Gemma 2.5 0.8B uses gated Delta Net + gated attention
- Large embedding layers result from distillation from teacher models with huge vocabulary sizes
- The large embedding proportion means fewer effective parameters available for reasoning and knowledge
- Serves as a comparison point for LFM 2's more efficient architecture (~10% embedding)
- **Known Bugs**: Had activation function issues (needed approximate GELU not exact GELU), tokenization problems, and double BOS token issues — all fixed by Daniel Han and the Unsloth team

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[DanielHan]] — identified and fixed Gemma bugs
- [[Unsloth]] — tool with automated Gemma bug fixes
- [[LFM]] — compared architecture
- [[ModelDistillation]] — technique causing large embedding layers
- [[EmbeddingLayerEfficiency]] — key architectural concern
- [[SlidingWindowAttention]] — used in Gemma 3
- [[GatedDeltaNet]] — used in Gemma 2.5
- [[GQA]] — attention mechanism used in Gemma 3
- [[DoubleBOSTokens]] — bug affecting Gemma fine-tuning
