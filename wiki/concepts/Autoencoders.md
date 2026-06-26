---
title: "Autoencoders"
type: concept
tags: [deep-learning, compression, representation-learning, generative-models, latent-diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Autoencoders are neural networks consisting of an encoder and a decoder, trained to reproduce their input through a bottleneck. In the context of generative models, they learn compressed latent representations that preserve semantic content and spatial topology while reducing dimensionality, enabling efficient training of downstream diffusion or auto-regressive models.

## Key Information
- **Architecture**: Encoder compresses input into a bottleneck (latent representation), decoder reconstructs the original input from the latent
- **Training objective**: Reproduce the input as faithfully as possible (reconstruction loss)
- **Bottleneck forces compression**: The narrow middle layer forces the network to learn efficient representations
- **Spatial topology preserved**: Unlike codec compression (JPEG, H.265), learned autoencoders maintain grid structure, which is essential for downstream neural network architectures with spatial inductive biases
- **What's preserved vs lost**: Semantic content is preserved (you can tell what's in the image from latents); local texture and fine-grained structure are abstracted
- **Lossy compression**: Total tensor size is much smaller than original, but some information is inevitably lost
- **Visualization (EQ-VAE)**: PCA across latent channels mapped to RGB reveals that latents still show recognizable content
- **Key enabler**: Makes high-resolution image and video generation feasible by reducing memory requirements by up to 100x

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[LatentDiffusion]] — primary application
- [[EQ-VAE]] — paper on improving autoencoder training
- [[DiffusionModels]] — downstream generative model
- [[Stable Diffusion]] — uses autoencoder for latent compression
