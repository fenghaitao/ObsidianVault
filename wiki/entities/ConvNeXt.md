---
title: "ConvNeXt"
type: entity
tags: [model, computer-vision, cnn, architecture, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
ConvNeXt is a modernized convolutional neural network that applies transformer-inspired design patterns (layer norm, patchify, mixer/feed-forward block structure) to a CNN, beating both ViT and Swin on the standard ImageNet benchmark.

## Key Information
- Takes learnings from vision transformers and applies them to a convolutional network
- Uses a 4×4 patchify operation (vs ViT's 16×16) for finer initial processing
- Replaces transformer self-attention with convolution as the spatial mixer, following the same mixer → feed-forward → mixer → feed-forward pattern
- Borrows hierarchical structure from classical CNNs
- Incorporates layer norm and other transformer innovations
- Beat ViT and Swin on ImageNet but was not fast enough for practical deployment
- Motivated Hera's approach of stripping inductive biases to find what was actually useful

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[ViT (Vision Transformer)]] — the architecture it competed against
- [[Swin Transformer]] — also beaten by ConvNeXt
- [[Convolutional Neural Networks]] — underlying architecture family
- [[Hera]] — Meta's follow-up that stripped biases
- [[ImageNet]] — benchmark used for comparison
- [[Inductive Bias]] — key differentiator between CNNs and transformers
