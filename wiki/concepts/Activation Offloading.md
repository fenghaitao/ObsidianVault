---
title: "Activation Offloading"
type: concept
tags: [training, memory-optimization, cpu-offloading, long-context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han.md"]
last_updated: 2026-06-30
---

## Definition
Activation offloading is a memory optimization technique that moves intermediate activations (inputs to each transformer block) from GPU memory to CPU memory when they are not actively needed, then prefetches them back during backpropagation. First implemented by Unsloth, it enables dramatically larger context windows with minimal performance impact.

## Key Information
- **Origin**: First implemented by [[Unsloth]], to the best of Together AI's knowledge
- **Mechanism**: Store transformer block inputs on CPU during forward pass; prefetch them back to GPU when backpropagating through the corresponding layer
- **Performance impact**: Minimal — offloading and prefetching are non-blocking operations that overlap with GPU computation
- **Position in optimization stack**: Applied after [[Activation Checkpointing]] in the long-context training pipeline; reduces memory by a further significant factor
- **Contrast with gradient offloading**: [[GradientOffloading]] targets gradient tensors; activation offloading targets intermediate layer activations
- **Scale**: With offloading, memory drops to ~37 GB in the 3M token training scenario, but further techniques are still needed

## Related
- [[Unsloth]] — first implementation
- [[GradientOffloading]] — related technique for gradient tensors
- [[Activation Checkpointing]] — complementary technique (recompute instead of offload)
- [[Long Context Training]] — primary application
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
- [[summary-20240731 - Fixing bugs in Gemma, Llama, & Phi 3： Daniel Han]] — source (Unsloth's gradient offloading)
