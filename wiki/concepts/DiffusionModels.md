---
title: "DiffusionModels"
type: concept
tags: [generative-models, image-generation, video-generation, denoising, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Diffusion models are a generative modeling paradigm that works by defining a corruption process (gradually adding Gaussian noise to data) and learning a denoiser to reverse it. Sampling proceeds iteratively: start from pure noise, denoise slightly, optionally add a bit of noise back, and repeat until a clean sample emerges. They are the dominant approach for audio-visual data generation, in contrast to auto-regression which dominates language modeling.

## Key Information
- **Corruption process**: Gradually add Gaussian noise to data; high frequencies are obscured first, then progressively lower frequencies
- **Denoiser**: Neural network trained to predict the clean version given a noisy observation; predictions are blurry because the problem is ill-posed (many clean images could produce the same noisy observation)
- **Sampling**: Start from pure noise, take small denoising steps (not jumps to the blurry prediction), optionally add a small amount of new noise back to avoid error accumulation
- **Why it works for images/video**: Natural images have power-law spectra (more energy in low frequencies). Adding noise obscures high frequencies first, so diffusion naturally generates coarse-to-fine
- **Spectral auto-regression**: Diffusion effectively generates images from low frequencies to high frequencies, analogous to auto-regression but in frequency space
- **Stochastic vs deterministic**: Some sampling algorithms add noise back (stochastic, more robust), others don't (deterministic, useful for distillation and invertibility)
- **Guidance**: Classifier-free guidance is universally used to trade diversity for quality by amplifying the difference between conditional and unconditional predictions
- **Architecture evolution**: Started with U-Nets (convolutional), now primarily uses transformers with bidirectional attention (no causal mask)
- **Distillation**: Consistency models can reduce sampling steps by learning to predict the trajectory endpoint directly

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[LatentDiffusion]] — training on compressed representations
- [[ClassifierFreeGuidance]] — key sampling technique
- [[ConsistencyModels]] — distillation approach
- [[SpectralAutoRegression]] — frequency-domain interpretation
- [[UNetArchitecture]] — earlier architecture
- [[TransformerArchitecture]] — current architecture
- [[Autoencoders]] — for latent compression
- [[RectifiedFlow]] — straighter sampling paths
- [[DeterministicVsStochasticSampling]] — sampling algorithm tradeoffs
- [[Veo]] — video diffusion model
- [[NanoBanana]] — image diffusion model
- [[Stable Diffusion]] — open-source latent diffusion model
- [[GLIDE]] — early pixel-space diffusion model
