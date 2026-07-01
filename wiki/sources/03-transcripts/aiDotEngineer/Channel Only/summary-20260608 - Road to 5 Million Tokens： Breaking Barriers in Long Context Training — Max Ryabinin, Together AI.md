---
title: "summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI"
type: source
tags: [source, transcript, long-context, training, memory-optimization, context-parallelism, together-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Core Summary

Max Ryabinin, VP of R&D at Together AI, presents "Road to 5M" — a systematic walkthrough of memory optimization techniques for training transformer models with extremely long context windows. Starting from a baseline where even model parameters cannot fit on an 8×H100 node, he stacks progressively more advanced techniques: Fully Sharded Data Parallelism (FSDP), DeepSpeed Ulysses context parallelism, activation checkpointing, CPU offloading (pioneered by Unsloth), and Arctic sequence parallelism. These get to 3 million tokens, but their novel contribution — "Untitled Ulysses" (U-Pipe) — further subdivides attention head computation into time-sequenced chunks that reuse GPU buffers, enabling 5 million tokens on a single node with minimal throughput impact.

## Key Points

- **Two bottlenecks in long-context training**: Quadratic computation (O(n²) pairwise attention interactions) and linear memory growth from activation tensors that scale with sequence length
- **FSDP (Fully Sharded Data Parallelism)**: Chunks model parameters across 8 GPUs, dramatically reducing model memory but still leaving attention activations as the dominant consumer
- **DeepSpeed Ulysses**: Microsoft's context parallelism technique where each GPU computes attention for only one head over the full sequence, then aggregates results. Reduces activation memory ~8×. Compatible with Flash Attention implementations
- **Activation Checkpointing**: Recomputes activations during the backward pass instead of storing them, trading compute for another ~8× memory reduction. Available in most deep learning frameworks
- **CPU Offloading (Unsloth)**: Stores transformer block inputs on CPU when not needed, prefetches during backpropagation. First implemented by Unsloth. Dramatically expands context window with minimal performance impact
- **Arctic Sequence Parallelism**: Tiles element-wise operations (loss, MLPs) across the sequence length dimension to avoid creating buffers with dimension = 3 million
- **Untitled Ulysses (U-Pipe)**: The key novel contribution. Observes that computing one set of attention heads already saturates GPU compute within an iteration. Instead of computing all heads simultaneously, subdivides them into time-sequenced chunks that reuse the same allocated buffers. Further saves activation memory with negligible throughput impact at small scales
- **Results**: Matches the most memory-optimized transformer training implementations at 8B and 32B scales while reaching 5M tokens, and can be more performant at shorter context lengths
- **Tooling recommendation**: Use PyTorch profiler to identify unexpected memory bottlenecks

## Related

- [[Max Ryabinin]] — speaker, VP of R&D at Together AI
- [[Together AI]] — AI-native cloud, employer
- [[Context Parallelism]] — core technique for distributing attention across GPUs
- [[DeepSpeed Ulysses]] — Microsoft's context parallelism implementation
- [[Activation Checkpointing]] — memory-vs-compute tradeoff technique
- [[Activation Offloading]] — CPU offloading of intermediate activations
- [[Fully Sharded Data Parallelism]] — model parameter sharding across GPUs
- [[Sequence Parallelism]] — tiling element-wise ops across sequence length
- [[Untitled Ulysses]] — Together AI's chunked attention head technique (U-Pipe)
- [[Long Context Training]] — training models with extended context windows
- [[Quadratic Attention]] — O(n²) complexity bottleneck in transformers
- [[Unsloth]] — pioneered CPU offloading for activations
- [[FlashAttention]] — optimized attention kernel used alongside Ulysses
- [[PyTorch]] — recommended profiling tooling
- [[Llama3]] — baseline model architecture (3B)
- [[Nvidia]] — H100 GPU hardware
- [[HuggingFace]] — referenced blog post on model training memory
- [[Microsoft]] — creator of DeepSpeed Ulysses
