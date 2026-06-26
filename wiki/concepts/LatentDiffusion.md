---
title: "LatentDiffusion"
type: concept
tags: [generative-models, diffusion, compression, autoencoders, image-generation, video-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Latent diffusion is a two-stage approach to generative modeling where data is first compressed into a latent representation using a learned autoencoder, and then a diffusion model is trained on these compressed latents rather than on raw pixels. This makes high-resolution image and video generation computationally feasible by reducing tensor sizes by up to two orders of magnitude.

## Key Information
- **Two-stage process**: (1) Train an autoencoder to compress data into latents, (2) Train a diffusion model on the latent representations
- **Compression ratio**: A 256x256x3 RGB image compresses to 32x32x4 latents (~48x reduction in Stable Diffusion)
- **Spatial topology preserved**: Latents maintain the same grid structure as pixels, just at coarser resolution with extra channels
- **Learned compression vs codecs**: Unlike JPEG/H.265, learned autoencoders preserve semantic structure and topological relationships, making generative modeling easier
- **What's compressed**: Local texture and fine-grained detail are abstracted; semantic content is preserved (visible in EQ-VAE PCA visualizations)
- **Video benefits even more**: The extra time dimension provides additional redundancy, enabling even greater compression
- **Memory feasibility**: Compression is the difference between fitting training data in memory and not being able to train at all
- **Decoder required**: After sampling in latent space, the decoder converts latents back to pixel space
- **Used by**: Stable Diffusion, Veo, NanoBanana, and most modern image/video generation models

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — generative modeling paradigm
- [[Autoencoders]] — compression mechanism
- [[EQ-VAE]] — paper on improving autoencoder training
- [[Stable Diffusion]] — canonical example
- [[Veo]] — video latent diffusion model
- [[NanoBanana]] — image latent diffusion model
