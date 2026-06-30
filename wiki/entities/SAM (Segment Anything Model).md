---
title: "SAM (Segment Anything Model)"
type: entity
tags: [model, computer-vision, foundation-model, segmentation, meta]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
SAM (Segment Anything Model) is a series of vision foundation models for image segmentation whose architectural evolution traces the broader vision architecture war: ViT+MAE → tiny ViT hybrid → Hera+MAE → massive pretrained ViT.

## Key Information
- SAM 1: Used a ViT backbone trained with MAE
- Mobile SAM: Replaced the ViT backbone with a specialized convolutional-transformer hybrid called tiny ViT, attempting to find a better architecture
- SAM 2: Used Hera with MAE pretraining as the backbone
- SAM 3: Abandoned architecture ablation entirely, using a massively pretrained ViT backbone — 800M parameters, 300ms on a T4 GPU
- The SAM series mirrors the broader trend: attempts to improve on ViT eventually gave way to just using a bigger, better-pretrained ViT
- SAM 3 is extremely powerful but has no deployment flexibility — too large and slow for edge devices where vision is historically deployed
- Roboflow's RFDetR achieves up to 40x speedup at same accuracy versus fine-tuning SAM 3

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[ViT (Vision Transformer)]] — backbone architecture
- [[MAE (Masked Autoencoder)]] — pretraining method used
- [[Hera]] — backbone used in SAM 2
- [[RFDetR]] — deployment-optimized alternative from Roboflow
- [[Foundation Models]] — model class
- [[DINOv3]] — related self-supervised pretraining
