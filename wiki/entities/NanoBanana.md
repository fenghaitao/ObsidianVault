---
title: "NanoBanana"
type: entity
tags: [model, google, deepmind, image-generation, diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
NanoBanana is Google DeepMind's image generation model, built using diffusion models. Sander Dieleman works on NanoBanana as part of the generative media team at Google DeepMind.

## Key Information
- Image generation model from Google DeepMind
- Uses latent diffusion: images are compressed via a learned autoencoder before diffusion training
- Trained at scale using JAX with model parallelism across TPUs
- Part of the generative media team's portfolio alongside Veo (video generation)
- Specific variants include NanoBananaPro and Nano Banana 2
- Uses classifier-free guidance for quality-diversity tradeoff
- Supports conditioning beyond text prompts

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[NanoBananaPro]] — specific model variant
- [[Nano Banana 2]] — newer model variant
- [[GoogleDeepMind]] — creator
- [[SanderDieleman]] — research scientist on the team
- [[Veo]] — sibling video generation model
- [[DiffusionModels]] — underlying technique
- [[LatentDiffusion]] — training approach
