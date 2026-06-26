---
title: "TransformerArchitecture"
type: concept
tags: [deep-learning, architecture, attention, diffusion, generative-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Transformer architecture, in the context of diffusion models, refers to using transformer neural networks (with bidirectional self-attention, no causal mask) as the denoiser backbone, replacing earlier U-Net convolutional architectures. The LLM community's extensive scaling knowledge makes transformers a practical choice for diffusion models.

## Key Information
- **Bidirectional attention**: Unlike LLM transformers, diffusion transformers use fully bidirectional attention (no causal mask), making them slightly more expressive
- **Replaced U-Nets**: Modern diffusion models have largely moved from convolutional U-Nets to transformers
- **LLM scaling knowledge transfer**: The extensive experience scaling transformers for language models directly benefits diffusion model training
- **Conditioning flexibility**: Transformers offer multiple ways to insert conditioning signals — extra tokens, broadcasting to all tokens, etc.
- **Noise level conditioning**: Typically broadcast to all tokens rather than added as a single token
- **Video considerations**: For video, the 3D volume (height × width × time) can be jointly processed, or a hybrid approach can use auto-regression in time with diffusion per frame

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — primary application
- [[UNetArchitecture]] — predecessor architecture
- [[SelfAttentionMechanism]] — core mechanism
- [[Veo]] — video model using transformers
- [[NanoBanana]] — image model using transformers
