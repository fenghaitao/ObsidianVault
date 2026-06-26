---
title: "ClassifierFreeGuidance"
type: concept
tags: [diffusion, sampling, guidance, generative-models, image-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Classifier-free guidance is a sampling technique for diffusion models that trades sample diversity for quality by amplifying the difference between conditional and unconditional model predictions. It has become universally adopted in modern diffusion models and is never turned off.

## Key Information
- **Mechanism**: At each sampling step, make two predictions: one with conditioning (e.g., text prompt) and one without. Compute the delta between them, scale it up (guidance scale), and use the amplified direction for denoising
- **Effect**: Higher guidance scale → less diversity but much higher individual sample quality with respect to the prompt
- **Cost**: Requires two model evaluations per step (conditional + unconditional)
- **Universality**: After the GLIDE paper (OpenAI, 2021) demonstrated the dramatic improvement, guidance became standard and is never disabled
- **Modern models without guidance**: Sander Dieleman notes most people would be surprised how bad today's models are without guidance
- **Guidance scale scheduling**: Varying the scale across noise levels (ramping up in the middle, not using it at the very start or end) yields the best trade-off
- **Why it works**: There's a Bayesian reasoning interpretation; it effectively sharpens the conditional distribution
- **Semantic gap requirement**: Works best when there's a semantic gap between the conditioning signal and what's being generated (e.g., text→image). Less effective for low-level signals like segmentation masks
- **Visual artifacts**: Overly high guidance can cause oversaturated images
- **Applicability**: Can be applied to auto-regressive models too, but works exceptionally well for diffusion

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — core technique
- [[GuidanceScale]] — hyperparameter
- [[GLIDE]] — paper that demonstrated its importance
- [[DeterministicVsStochasticSampling]] — related sampling consideration
