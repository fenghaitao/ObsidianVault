---
title: "Swin Transformer"
type: entity
tags: [model, computer-vision, transformer, architecture, attention]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Swin Transformer is a vision transformer variant that replaces global attention with windowed local attention and shifting windows between layers, reducing complexity from O(n⁴) to O(n²) and adding a locality inductive bias similar to convolution.

## Key Information
- Uses windowed attention: tokens only attend within a fixed-size window rather than globally
- Shifts windows between consecutive layers so tokens can interact across window boundaries
- Reduces compute complexity to O(n²) when window size is independent of resolution
- Adds locality inductive bias following the convolutional network pattern
- Beaten by ConvNeXt on the standard ImageNet benchmark
- Ultimately surpassed by plain ViT once FlashAttention eliminated the speed advantage and MAE pretraining recovered the missing inductive biases

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[ViT (Vision Transformer)]] — the architecture it tried to improve
- [[ConvNeXt]] — modernized CNN that beat Swin
- [[Inductive Bias]] — locality bias added through windowing
- [[Convolutional Neural Networks]] — inspiration for locality bias
