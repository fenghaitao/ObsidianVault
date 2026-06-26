---
title: "Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"
date: 2026-04-21
ingested: 2026-06-26
tags: [talk, google-deepmind, diffusion-models, generative-models, image-generation, video-generation, veo, nanobanana, latent-diffusion, guidance, distillation, data-curation, autoencoders]
---

## Core Thesis
Sander Dieleman, a research scientist at Google DeepMind on the generative media team (working on models like Veo and NanoBanana), delivers a behind-the-scenes technical talk covering the full pipeline of training large-scale diffusion models for image and video generation. The talk spans eight topics: data curation, representation (latent autoencoders), diffusion modeling mechanics, neural network architectures, training at scale, sampling (including classifier-free guidance), distillation (reducing sampling steps), and control signals (post-training conditioning).

## Key Topics
- **Data Curation**: Emphasized as critically important yet under-incentivized in research culture. Time spent improving data is often a better investment than tweaking model architecture. Details are proprietary and rarely published.
- **Latent Representation**: Rather than training directly on pixels (too large for high-res video), models use learned autoencoders to compress data into latent representations. The autoencoder (encoder-decoder) preserves spatial topology while reducing resolution ~8x, compensating with extra channels. This reduces tensor sizes by up to two orders of magnitude.
- **EQ-VAE**: A paper on improving autoencoder training; visualized latents via PCA show that latents preserve semantic content while abstracting only local texture and fine-grained structure.
- **Diffusion Mechanics**: Intuitive explanation using a 2D diagram. The denoiser predicts a clean image from a noisy one (ill-posed problem, so prediction is blurry/average). Sampling takes small steps toward the prediction, optionally adding a bit of new noise back to avoid error accumulation. The process iterates, with prediction regions shrinking until collapsing to a single point (a sample).
- **Spectral Auto-Regression**: Fourier analysis reveals images have power-law spectra. Adding noise obscures high frequencies first, then progressively lower frequencies. Diffusion effectively generates images coarse-to-fine (low frequencies first, then high frequencies), analogous to auto-regression but in frequency space.
- **Architecture**: Initially U-Nets (convolutional), now transformers (bidirectional attention, no causal mask). Transformers benefit from LLM scaling knowledge. For video, a hybrid approach exists: auto-regressive in time with diffusion per frame (e.g., Genie).
- **Training at Scale**: Data parallelism up to a point, then model parallelism (sharding across chips). Google DeepMind uses JAX for its automatic sharding and communication minimization, particularly optimized for TPUs.
- **Sampling & Guidance**: Classifier-free guidance trades diversity for quality by amplifying the difference between conditional and unconditional predictions. This "delta" is scaled up and used as the denoising direction. Guidance is so essential that modern models are never used without it. Varying guidance scale across noise levels (ramping up in the middle) yields best results.
- **Distillation (Consistency Models)**: Instead of making the model smaller, distillation reduces the number of sampling steps. Consistency models learn to predict the endpoint of the denoising trajectory directly, enabling few-step or single-step sampling. Multi-step consistency (e.g., 3 steps) often works better than single-step.
- **Control & Post-Training**: Beyond text prompts, models need conditioning on reference images/video, camera motion, event timing. These signals are often added in post-training since pre-training data lacks them. Post-training also includes preference tuning (RLHF/DPO).
- **Guidance works best with semantic gap**: Guidance is most effective when there's a semantic gap between the conditioning signal (e.g., text prompt) and what's being generated. Low-level signals (e.g., segmentation masks) benefit less from guidance.

## Entities
- [[SanderDieleman]] — Research scientist, Google DeepMind generative media team
- [[GoogleDeepMind]] — Parent organization
- [[Veo]] — Video generation model series from Google DeepMind
- [[NanoBanana]] — Image generation model from Google DeepMind
- [[JAX]] — ML framework used for model parallelism and TPU optimization
- [[TPU]] — Tensor Processing Unit, Google's AI accelerator
- [[Stable Diffusion]] — Reference latent diffusion model mentioned for autoencoder dimensions
- [[GLIDE]] — OpenAI's early pixel-space diffusion model at scale (2021)
- [[EQ-VAE]] — Paper on improving autoencoder training for latent diffusion
- [[ImageNet]] — Dataset used for Fourier analysis examples
- [[Genie1]] — Example of hybrid auto-regressive + diffusion video model
- [[Genie2]] — Example of hybrid auto-regressive + diffusion video model
- [[PyTorch]] — Alternative ML framework discussed in Q&A

## Concepts
- [[DiffusionModels]] — Core generative modeling paradigm for audio-visual data
- [[LatentDiffusion]] — Training diffusion models on compressed latent representations
- [[Autoencoders]] — Neural networks with encoder-decoder architecture for learned compression
- [[ClassifierFreeGuidance]] — Technique amplifying conditional vs unconditional prediction difference
- [[ConsistencyModels]] — Distillation approach reducing diffusion sampling steps
- [[SpectralAutoRegression]] — Diffusion as coarse-to-fine generation in frequency domain
- [[DataCurationForGenerativeModels]] — Critical importance of data quality for generative models
- [[RectifiedFlow]] — Training diffusion models to produce straighter sampling paths
- [[PostTrainingGenerativeModels]] — Adding conditioning signals and preference tuning after pre-training
- [[ModelParallelism]] — Sharding model across multiple chips for large-scale training
- [[DeterministicVsStochasticSampling]] — Tradeoffs between deterministic and stochastic diffusion sampling
- [[FourierAnalysisOfImages]] — Power-law spectra in natural images and implications for diffusion
- [[UNetArchitecture]] — Convolutional architecture originally used for diffusion denoisers
- [[TransformerArchitecture]] — Current architecture choice for diffusion denoisers
- [[GuidanceScale]] — Hyperparameter controlling diversity-quality tradeoff in diffusion sampling

## Related
- [[summary-20260418 - How Google DeepMind is researching the next Frontier of AI for Gemini — Raia Hadsell, VP of Research]] — related Google DeepMind research
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — related DeepMind products
- [[VEO 3.1 Light]] — specific Veo model variant
- [[NanoBananaPro]] — specific NanoBanana model variant
- [[Genie 3]] — world model from Google DeepMind
- [[ModelDistillation]] — related distillation concept (LLM context)
- [[Foundation Models]] — broader category
- [[FineTuning]] — related post-training concept
