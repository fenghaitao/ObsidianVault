---
title: "TransformerArchitecture"
type: concept
tags: [deep-learning, architecture, attention, diffusion, generative-models]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow.md"]
last_updated: 2026-06-29
---

## Definition
Transformer architecture is the foundational neural network design for modern LLMs, built from four core building blocks: multi-head self-attention, MLP/feed-forward networks, residual connections, and layer normalization. In the context of LLMs, it uses causal (decoder-only) self-attention for next-token prediction; in diffusion models, it uses bidirectional self-attention as a denoiser backbone replacing U-Nets.

## Key Information
- **Core building blocks**: Multi-head self-attention, MLP/feed-forward network, residual connections, layer normalization — these fundamentals haven't changed much from GPT-2 to modern models
- **Decoder-only (LLMs)**: Uses causal self-attention where each token only attends to previous tokens, enabling autoregressive next-token prediction
- **Bidirectional (diffusion)**: Unlike LLM transformers, diffusion transformers use fully bidirectional attention (no causal mask), making them slightly more expressive
- **Replaced U-Nets**: Modern diffusion models have largely moved from convolutional U-Nets to transformers
- **LLM scaling knowledge transfer**: The extensive experience scaling transformers for language models directly benefits diffusion model training
- **Conditioning flexibility**: Transformers offer multiple ways to insert conditioning signals — extra tokens, broadcasting to all tokens, etc.
- **Noise level conditioning**: Typically broadcast to all tokens rather than added as a single token
- **Video considerations**: For video, the 3D volume (height × width × time) can be jointly processed, or a hybrid approach can use auto-regression in time with diffusion per frame
- **Transformer block structure**: layer norm → attention → residual add → layer norm → MLP → residual add — repeated n_layer times
- **GPT-2 architecture**: The workshop model used 6 layers, 6 attention heads, 384 embedding dim, 256 context window — totaling ~1.8M parameters
- **Scaling**: Newer models add optimizations for longer context and better scaling, but the core architecture is the same; the same code with more data powered GPT-2 and GPT-3

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source (LLM architecture, building blocks)
- [[summary-20260508 - How Transformers Finally Ate Vision – Isaac Robinson, Roboflow]] — source (ViT, vision adaptation)
- [[DiffusionModels]] — primary application
- [[UNetArchitecture]] — predecessor architecture
- [[SelfAttentionMechanism]] — core mechanism
- [[MultiHeadAttention]] — multiple attention heads
- [[CausalSelfAttention]] — decoder-only variant
- [[ResidualConnections]] — stability mechanism
- [[LayerNorm]] — normalization technique
- [[GPT-2]] — architecture basis for the workshop
- [[LLMTrainingFromScratch]] — workshop using this architecture
- [[Veo]] — video model using transformers
- [[NanoBanana]] — image model using transformers
- [[ViT (Vision Transformer)]] — vision adaptation using patchify
- [[Patchify]] — image-to-token preprocessing for vision
