---
title: "DeterministicVsStochasticSampling"
type: concept
tags: [diffusion, sampling, generative-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Deterministic vs stochastic sampling refers to two families of diffusion sampling algorithms: stochastic algorithms add a small amount of new noise after each denoising step, while deterministic algorithms do not. Each has distinct tradeoffs in robustness, invertibility, and compatibility with distillation techniques.

## Key Information
- **Stochastic sampling**: Adds a small amount of new noise after each denoising step (less than the amount removed). More robust to error accumulation because new noise obscures the denoiser's mistakes
- **Deterministic sampling**: No noise added back. Creates a one-to-one mapping between initial noise and samples from the data distribution
- **Deterministic benefits**: Useful for invertibility (going from data to noise and back), and required as a teacher for many distillation techniques including consistency models
- **Stochastic benefits**: More robust — the denoiser is imperfect, and feeding its mistakes back can cause divergence; adding noise mitigates this
- **Not all algorithms use noise**: Many diffusion sampling algorithms skip the noise-addition step
- **Magical property**: Sander Dieleman notes he "still doesn't really believe" deterministic diffusion works, but it does

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — core technique
- [[ConsistencyModels]] — requires deterministic teacher
- [[ClassifierFreeGuidance]] — can be combined with either approach
