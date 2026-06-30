---
title: "Convolutional Neural Networks"
type: concept
tags: [deep-learning, computer-vision, architecture, cnn, image-processing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Convolutional Neural Networks (CNNs) are the classical deep learning architecture for vision, using learnable filters convolved across images to achieve translation invariance. They dominated computer vision for years until Vision Transformers surpassed them through massive pretraining.

## Key Information
- Have excellent inductive bias motivated by the human visual system: a filter activates the same way regardless of where a pattern appears
- Build hierarchical structures (ResNets, etc.) that progressively extract higher-level features
- Compute scales as O(n²) with resolution, unlike ViT's O(n⁴)
- ConvNeXt represents the peak of CNN evolution, incorporating transformer-inspired design patterns (layer norm, patchify, mixer/feed-forward block structure)
- ConvNeXt beat ViT and Swin on ImageNet but was ultimately not fast enough
- CNNs cannot benefit from MAE pretraining because convolution is invariant across patches, making patch dropout meaningless
- This pretraining disadvantage is a key reason transformers ultimately won — ViTs could learn inductive biases from data while CNNs were stuck with their baked-in biases
- Roboflow's RFDetR outperformed the best real-time instance segmentation models (all CNN-based at the time)

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[ViT (Vision Transformer)]] — the architecture that replaced CNNs
- [[ConvNeXt]] — modernized CNN that was the last major competitor
- [[Inductive Bias]] — CNNs' key structural advantage
- [[Patchify]] — ViT's alternative to convolution
- [[MAE (Masked Autoencoder)]] — pretraining CNNs cannot use
- [[RFDetR]] — model that outperformed CNN-based instance segmentation
