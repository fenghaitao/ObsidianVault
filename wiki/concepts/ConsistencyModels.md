---
title: "ConsistencyModels"
type: concept
tags: [diffusion, distillation, sampling, generative-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Consistency models are a distillation technique for diffusion models that reduces the number of sampling steps by learning to predict the endpoint of the denoising trajectory directly, rather than predicting the tangent direction at each point. Unlike traditional distillation (which makes models smaller), diffusion distillation focuses on reducing sampling steps.

## Key Information
- **Goal**: Reduce the number of sampling steps required, not model size
- **Core idea**: Instead of predicting which direction to move at each point on the denoising trajectory, predict where the trajectory will end (the clean sample)
- **Single-step limitation**: One-step consistency sampling usually doesn't work well because it asks the network to do in one pass what previously took ~50 passes
- **Multi-step compromise**: Using consistency modeling for intervals of the sampling path (e.g., 3 steps instead of 50) often yields better results than single-step
- **Deterministic requirement**: Consistency model distillation typically requires a deterministic teacher (deterministic sampling algorithm)
- **Trajectory perspective**: Diffusion sampling traces a non-linear path through input space; the model predicts tangents to this path. Consistency models predict the path endpoint
- **Related to rectified flow**: Training models to produce straighter paths from the start makes consistency distillation more effective

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — parent technique
- [[RectifiedFlow]] — complementary approach for straighter paths
- [[DeterministicVsStochasticSampling]] — prerequisite for consistency distillation
- [[ModelDistillation]] — related concept in LLM context
