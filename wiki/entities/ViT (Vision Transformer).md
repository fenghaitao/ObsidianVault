---
title: "ViT (Vision Transformer)"
type: entity
tags: [model, computer-vision, transformer, deep-learning, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
The Vision Transformer (ViT) is a transformer architecture adapted for images by splitting an image into patches (originally 16×16), adding learned positional encodings, and processing them as a set of tokens through standard transformer blocks — with no built-in spatial inductive bias.

## Key Information
- Splits image into patches (16×16 in the original), treating each patch as a token
- Adds learned positional encodings to inject location information
- Has no inductive bias: the same pattern in the upper left and bottom right can produce different activations
- Compute scales as O(n⁴) with resolution (n/16 patches per side, n² total patches, n² attention)
- Won the vision architecture war despite theoretical disadvantages because of:
  - Massive ViT-specific pretraining (MAE, DINOv2/DINOv3) that learns inductive biases from data
  - LLM infrastructure speedups (FlashAttention) that eliminate the speed advantage of more efficient architectures
- Self-supervised pretrained ViTs (DINOv3) produce semantically rich feature maps that approach supervised performance via linear probe
- Forms the backbone of SAM (Segment Anything Model) series
- MAE pretraining only works with ViTs, not CNNs — a unique advantage
- Combined with neural architecture search (RFDetR) enables deployment flexibility on edge devices

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[TransformerArchitecture]] — underlying architecture
- [[Patchify]] — image preprocessing step
- [[Inductive Bias]] — key concept ViT lacks
- [[MAE (Masked Autoencoder)]] — ViT-specific pretraining
- [[DINOv3]] — self-supervised pretrained ViT
- [[SAM (Segment Anything Model)]] — uses ViT backbone
- [[Swin Transformer]] — competitor adding locality bias
- [[ConvNeXt]] — CNN competitor
- [[Convolutional Neural Networks]] — classical alternative
- [[FlashAttention]] — speedup from LLM world
