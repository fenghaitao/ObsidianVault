---
title: "Inductive Bias"
type: concept
tags: [deep-learning, architecture, machine-learning, computer-vision]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Inductive bias in machine learning refers to the built-in assumptions an architecture makes about the structure of data. In computer vision, CNNs have a strong inductive bias (translation invariance — a feature is the same regardless of position), while Vision Transformers have none, treating all patches as equally related until pretraining teaches the model spatial structure.

## Key Information
- CNNs have excellent inductive bias motivated by the human visual system: a filter activates the same way regardless of where a pattern appears in the image
- This translation invariance means "a person in an image is a person regardless of whether they're in the upper left or the bottom right"
- Vision Transformers have zero inductive bias — the same pattern in different positions can produce entirely different activations
- Swin Transformer added locality inductive bias through windowed attention, mimicking convolution
- Hera's key experiment: systematically strip inductive biases from a transformer and use MAE pretraining to learn them back from data
- The central finding: massive ViT-specific pretraining (MAE, DINO) can learn inductive biases from data that were previously baked into architecture
- Balance between pretraining and inherent inductive bias is how transformers ultimately win — pretraining scales better than architectural bias
- The architecture that scales well eventually beats the architecture that starts with better assumptions

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[Convolutional Neural Networks]] — architecture with strong inductive bias
- [[ViT (Vision Transformer)]] — architecture with no inductive bias
- [[MAE (Masked Autoencoder)]] — pretraining that learns inductive bias
- [[Hera]] — model that studied bias vs pretraining trade-off
- [[Swin Transformer]] — added locality bias to transformers
