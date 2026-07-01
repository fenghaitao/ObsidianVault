---
title: "Fully Sharded Data Parallelism"
type: concept
tags: [training, memory-optimization, parallelism, distributed-training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Fully Sharded Data Parallelism (FSDP) is a distributed training strategy that partitions model parameters, gradients, and optimizer states across multiple GPUs rather than replicating them on each device. It is the first-level optimization for fitting large models and long sequences into limited GPU memory.

## Key Information
- **Mechanism**: Chunks (shards) all model parameters across the available GPUs, with each GPU only holding its portion
- **Memory reduction**: Dramatically reduces per-GPU model memory, but attention activations remain the dominant memory consumer for long sequences
- **Limitation**: Even with FSDP applied, a standard Llama 3B model cannot fit 3M tokens on an 8×H100 node — attention activations still overflow memory
- **Position in optimization stack**: The first technique applied after discovering that raw model parameters alone exceed GPU memory
- **Followed by**: [[Context Parallelism]] (e.g., [[DeepSpeed Ulysses]]) to address the remaining activation memory bottleneck

## Related
- [[Context Parallelism]] — next technique in the optimization stack
- [[DeepSpeed Ulysses]] — specific context parallelism implementation
- [[Long Context Training]] — primary application
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
