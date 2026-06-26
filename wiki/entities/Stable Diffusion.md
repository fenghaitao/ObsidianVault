---
title: "Stable Diffusion"
type: entity
tags: [model, image-generation, diffusion, open-source, latent-diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Stable Diffusion is a latent diffusion model for image generation, referenced by Sander Dieleman as a concrete example of autoencoder dimensions in latent diffusion. Its autoencoder compresses 256x256 RGB images to 32x32 latent grids with extra channels.

## Key Information
- Latent diffusion model: trains a diffusion model on compressed latent representations rather than pixels
- Autoencoder compresses 256x256x3 RGB images to 32x32x4 latent representations (~48x compression)
- Preserves spatial topology while reducing resolution, compensating with extra channels
- U-Net based architecture (earlier generation of diffusion models)
- Referenced as a canonical example of the two-stage latent diffusion approach
- Demonstrates the key insight that latent compression makes high-resolution generation feasible

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[LatentDiffusion]] — core technique
- [[Autoencoders]] — compression mechanism
- [[DiffusionModels]] — underlying paradigm
- [[UNetArchitecture]] — neural network architecture used
- [[Stability AI]] — original developing organization
