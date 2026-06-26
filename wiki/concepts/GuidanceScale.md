---
title: "GuidanceScale"
type: concept
tags: [diffusion, sampling, hyperparameter, generative-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Guidance scale is a hyperparameter in classifier-free guidance that controls the trade-off between sample diversity and quality. Higher values amplify the difference between conditional and unconditional predictions, producing higher-quality but less diverse samples. It can be varied across noise levels for optimal results.

## Key Information
- **Range**: Higher values → less diversity, higher individual sample quality with respect to the prompt
- **Mechanism**: Multiplies the delta between conditional and unconditional predictions before using it as the denoising direction
- **Visual effects**: Overly high guidance can cause oversaturated images
- **Scheduling**: Varying the scale across the sampling procedure (ramping up in the middle, not using at the very start or end) yields the best trade-off
- **Universality**: Modern diffusion models always use guidance; it's never turned off
- **Frequency-dependent effects**: Different noise levels correspond to different frequency scales, so varying guidance across levels produces different visual effects

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[ClassifierFreeGuidance]] — technique that uses this parameter
- [[DiffusionModels]] — core technique
- [[GLIDE]] — paper that studied guidance scale effects
