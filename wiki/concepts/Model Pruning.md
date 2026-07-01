---
title: "Model Pruning"
type: concept
tags: [optimization, models, inference, compression]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Model pruning is a technique for reducing model size by removing parts of the model (e.g., weights, attention heads, or in MOE models, entire experts), trading some quality for lower memory requirements and faster inference.

## Key Information
- Can be applied alongside quantization for further model compression
- In MOE (Mixture of Experts) models, pruning can reduce the number of active experts (e.g., from 8 to 2)
- Alex Cheema warns that aggressive pruning combined with heavy quantization produces misleading citizen science results — a pruned 1-bit model may appear to run a large model on consumer hardware but be functionally useless
- "You're better off just using a smaller model and not quantizing it" than heavily pruning and quantizing a large one
- EXO Labs plans to benchmark different pruning configurations alongside quantization levels to show the quality-vs-performance tradeoff
- Pruning is part of the full-stack optimization toolkit but must be evaluated holistically with quality metrics, not just tokens-per-second
- [[Pruna]] uses pruning alongside [[Quantization]] and step reduction to build [[Performance Models]], removing unimportant components from image and video models

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source (Pruna's use of pruning)
- [[Pruna]] — uses pruning for performance models
- [[Quantization]] — complementary compression technique
- [[Mixture of Experts]] — architecture where pruning of experts is applicable
- [[Citizen Science]] — context where misleading pruning claims appear
- [[FullStack CoDesign]] — methodology that includes pruning as one lever
