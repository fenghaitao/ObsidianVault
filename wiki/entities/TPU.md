---
title: "TPU"
type: entity
tags: [hardware, google, accelerator, ai, deepmind]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
TPU (Tensor Processing Unit) is Google's custom AI accelerator chip, designed with fast interconnects for scaling across many chips. JAX was conceived specifically to make TPU programming and model parallelism as easy as possible.

## Key Information
- Google's custom AI accelerator hardware
- Features fast interconnects between chips, enabling efficient model parallelism
- Rarely used as a single chip; designed for scale-out across many units
- JAX was designed from the ground up with TPU parallelism in mind
- Used by Google DeepMind for training large-scale diffusion models (Veo, NanoBanana)
- Enables the model parallelism needed when models exceed single-chip memory

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[JAX]] — framework optimized for TPUs
- [[GoogleDeepMind]] — primary user
- [[ModelParallelism]] — key use case
- [[Nvidia]] — competitor in AI accelerators
