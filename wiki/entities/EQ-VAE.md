---
title: "EQ-VAE"
type: entity
tags: [paper, autoencoder, latent-diffusion, visualization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
EQ-VAE is a research paper on improving the training of autoencoders for latent diffusion models. It introduced a visualization technique using PCA across latent channels mapped to RGB, revealing that latent representations preserve semantic content while abstracting only local texture.

## Key Information
- Paper focused on improving autoencoder training for latent diffusion
- Visualization technique: PCA across latent channels mapped to RGB
- Visualizations show that latents preserve semantic content (you can still tell what animal is in the image)
- Latents abstract local texture and fine-grained structure, not semantic content
- Demonstrates that learned compression is fundamentally different from codec compression (JPEG, H.265)
- Referenced by Sander Dieleman to illustrate what latent representations actually encode

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[Autoencoders]] — core technique
- [[LatentDiffusion]] — application context
- [[DiffusionModels]] — broader paradigm
