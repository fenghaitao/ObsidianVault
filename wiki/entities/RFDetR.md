---
title: "RFDetR"
type: entity
tags: [model, computer-vision, object-detection, deployment, neural-architecture-search]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
RFDetR is a Roboflow model that uses neural architecture search on a single vision foundation model to generate a family of deployment-optimized models, resolving the deployment flexibility problem of large foundation models like SAM 3.

## Key Information
- Developed by Roboflow under Isaac Robinson
- Uses neural architecture search to modify a single foundation model into a family of high-performance models in one pass
- Introduces flexible knobs that are drop-in compatible with existing foundation model infrastructure
- Mixes and matches knobs based on target data and target hardware
- Achieves ~40x speedup at same accuracy versus fine-tuning SAM 3
- Achieves ~15x speedup with meaningful accuracy improvement
- At publication, outperformed the best real-time instance segmentation models
- All models in the family use the same underlying foundation model, just optimized differently
- Combines massive ViT-specific pretraining, LLM infrastructure speedups, and pretraining-compatible neural architecture search

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[Roboflow]] — developer
- [[Isaac Robinson]] — research lead
- [[RF100VL]] — evaluation dataset
- [[SAM (Segment Anything Model)]] — baseline compared against
- [[Neural Architecture Search]] — core technique
- [[ViT (Vision Transformer)]] — backbone architecture
- [[Foundation Models]] — model class being optimized for deployment
