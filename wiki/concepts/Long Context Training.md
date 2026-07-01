---
title: "Long Context Training"
type: concept
tags: [training, long-context, memory-optimization, transformers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Long context training is the practice of training transformer-based language models to process extremely long input sequences (millions of tokens), driven by agent applications requiring large context windows and video generation tasks needing temporal consistency across many frames.

## Key Information
- **Drivers**: Agent applications (putting as many tokens as needed in context) and video generation (tracking multiple frames per second with temporal consistency)
- **Two bottlenecks**: Quadratic computation (O(n²) pairwise attention interactions) and linear memory growth from activation tensors scaling with sequence length
- **Optimization stack** (in order): [[Fully Sharded Data Parallelism]] → [[DeepSpeed Ulysses]] ([[Context Parallelism]]) → [[Activation Checkpointing]] → [[Activation Offloading]] → [[Sequence Parallelism]] → [[Untitled Ulysses]] (U-Pipe)
- **State of the art**: Together AI's "Road to 5M" project achieved 5 million token context on a single 8×H100 node
- **Broader relevance**: Understanding memory bottlenecks benefits training at all scales, not just extreme context lengths — freed memory can be reinvested in other optimizations
- **Tooling**: PyTorch profiler is recommended for identifying unexpected memory bottlenecks

## Related
- [[Quadratic Attention]] — the O(n²) computation bottleneck
- [[Context Parallelism]] — key technique for distributing attention
- [[Untitled Ulysses]] — Together AI's breakthrough enabling 5M tokens
- [[Activation Checkpointing]] — compute-memory tradeoff technique
- [[Activation Offloading]] — CPU offloading technique
- [[GradientOffloading]] — related technique for gradient tensors
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
