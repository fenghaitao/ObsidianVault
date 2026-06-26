---
title: "Veo"
type: entity
tags: [model, google, deepmind, video-generation, diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Veo is Google DeepMind's video generation model series, built using diffusion models trained on latent representations. Sander Dieleman works on Veo as part of the generative media team.

## Key Information
- Video generation model series from Google DeepMind
- Uses latent diffusion: video is compressed via a learned autoencoder before diffusion training
- Trained at scale using JAX with model parallelism across TPUs
- Supports conditioning beyond text prompts, including reference images/video, camera motion control, and event timing
- Post-training phase adds advanced conditioning signals and preference tuning
- Part of the generative media team's portfolio alongside NanoBanana
- Specific model variants include VEO 3.1 Light (720p, paid tier)

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[VEO 3.1 Light]] — specific model variant
- [[GoogleDeepMind]] — creator
- [[SanderDieleman]] — research scientist on the team
- [[NanoBanana]] — sibling image generation model
- [[DiffusionModels]] — underlying technique
- [[LatentDiffusion]] — training approach
- [[JAX]] — training framework
