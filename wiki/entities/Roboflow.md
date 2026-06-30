---
title: "Roboflow"
type: entity
tags: [company, computer-vision, deep-learning, deployment, edge-ai, mlx]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Roboflow is a computer vision company focused on making vision foundation models deployable on resource-constrained edge devices by combining neural architecture search with pre-trained ViT backbones. Their RFDetector model is used in MLX VLM for real-time on-device object detection on Apple Silicon.

## Key Information
- Research lead: Isaac Robinson
- Published RF100VL, a dataset measuring how well foundation models transfer to downstream object detection tasks
- Developed RFDetR, which uses neural architecture search on a single foundation model to generate an entire family of deployment-optimized models
- RFDetR achieves ~40x speedup at same accuracy versus fine-tuning SAM 3, and ~15x speedup with meaningful accuracy improvement
- Addresses the deployment flexibility problem: foundation models like SAM 3 (800M params, 300ms on T4 GPU) are too large for edge devices
- Approach combines massive ViT-specific pretraining, LLM infrastructure speedups, and pretraining-compatible neural architecture search
- Outperformed the best real-time instance segmentation models at time of RFDetR publication
- RFDetector model used in MLX VLM demo for real-time on-device object detection on Mac

## Related
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source (RFDetector in MLX VLM)
- [[Isaac Robinson]] — research lead
- [[RFDetR]] — deployment-optimized detection model
- [[RF100VL]] — transfer learning dataset
- [[MLX VLM]] — framework using Roboflow models
- [[ViT (Vision Transformer)]] — backbone architecture
- [[Neural Architecture Search]] — key deployment technique
- [[SAM (Segment Anything Model)]] — compared foundation model
