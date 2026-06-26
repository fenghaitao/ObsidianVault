---
title: "JAX"
type: entity
tags: [framework, machine-learning, google, deepmind, tpu]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
JAX is a machine learning framework developed by Google, designed with TPU parallelism and automatic model sharding in mind. It is the primary framework used by Google DeepMind for training large-scale diffusion models like Veo and NanoBanana.

## Key Information
- Primary ML framework at Google DeepMind for training large generative models
- Designed from the ground up for TPU parallelism with fast interconnects
- Provides automatic model sharding that minimizes communication between chips
- Allows researchers to specify sharding strategies declaratively rather than manually
- Particularly well-suited for model parallelism at scale (beyond data parallelism)
- Sander Dieleman has used it throughout his decade at Google (predates PyTorch)
- Compared to PyTorch in Q&A: JAX was conceived to make TPU usage as easy as possible, though PyTorch can also do model parallelism

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[GoogleDeepMind]] — primary user
- [[TPU]] — hardware JAX is optimized for
- [[PyTorch]] — alternative framework
- [[ModelParallelism]] — key capability
- [[Veo]] — model trained with JAX
- [[NanoBanana]] — model trained with JAX
