---
title: "RectifiedFlow"
type: concept
tags: [diffusion, sampling, training, generative-models, distillation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Rectified flow (re-flow) is a technique for training diffusion models to produce straighter denoising trajectories through input space. Straighter paths enable more accurate approximation with fewer sampling steps, complementing distillation approaches like consistency models.

## Key Information
- **Problem**: Standard diffusion models produce non-linear sampling trajectories; approximating them with finite steps introduces error
- **Solution**: Train models to produce straighter (more linear) paths from the start
- **Benefit**: Straighter paths mean fewer steps needed for accurate sampling
- **Relationship to distillation**: Complementary to consistency models; straighter paths make distillation more effective
- **Piecewise linear approximation**: Sampling approximates the true non-linear path with piecewise linear segments; straighter paths reduce approximation error
- **Trade-off**: More steps → better approximation of the true path, but diminishing returns beyond a point

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — core technique
- [[ConsistencyModels]] — complementary distillation approach
- [[DeterministicVsStochasticSampling]] — related sampling consideration
