---
title: "Hera"
type: entity
tags: [model, computer-vision, transformer, meta, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Hera is a vision transformer model developed by Meta that takes a strong inductively biased transformer and strips out biases one at a time, using MAE pretraining to learn the biases instead — demonstrating the balance between pretraining and inherent inductive bias.

## Key Information
- Developed by Meta
- Starts with a well-inductively-biased transformer and systematically removes biases
- Gets speedups because specialized hardware for inductive biases is no longer needed
- Uses MAE (Masked Autoencoder) pretraining to recover the missing inductive biases from data
- Initially showed speedup for same accuracy versus ViT, but only when FlashAttention was not measured
- With FlashAttention enabled, the speed advantage disappeared — plain ViT was competitive again
- Used as the backbone for SAM 2 before SAM 3 abandoned architecture ablation entirely
- Illustrates the key insight: massive pretraining can substitute for architectural inductive bias

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[Meta]] — developed Hera
- [[ViT (Vision Transformer)]] — competing architecture
- [[MAE (Masked Autoencoder)]] — pretraining technique used
- [[ConvNeXt]] — inspired the bias-stripping approach
- [[FlashAttention]] — eliminated Hera's speed advantage
- [[SAM (Segment Anything Model)]] — SAM 2 used Hera backbone
- [[Inductive Bias]] — central concept being studied
