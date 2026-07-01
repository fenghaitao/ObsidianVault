---
title: "Activation Checkpointing"
type: concept
tags: [training, memory-optimization, compute-memory-tradeoff]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Activation checkpointing is a memory optimization technique that trades compute for memory by discarding intermediate activations during the forward pass and recomputing them during the backward pass when they are needed for gradient calculation. It is available in virtually all modern deep learning frameworks.

## Key Information
- **Core tradeoff**: Saves memory at the cost of additional computation (recomputing activations during backward pass)
- **Memory reduction**: Can reduce activation memory usage by approximately 8× in long-context training scenarios
- **Framework support**: Available in PyTorch, JAX, TensorFlow, and most deep learning frameworks — requires correct configuration to avoid excessive computational overhead
- **Position in optimization stack**: Applied after context parallelism (e.g., [[DeepSpeed Ulysses]]) but before CPU offloading in the long-context training pipeline
- **Complementary to**: [[Activation Offloading]] (CPU offloading), which stores activations on CPU rather than recomputing them
- **Context**: Critical stepping stone toward 3M+ token context lengths on limited GPU memory

## Related
- [[Activation Offloading]] — alternative approach (store on CPU instead of recompute)
- [[Long Context Training]] — primary application
- [[GradientOffloading]] — related technique for gradients rather than activations
- [[summary-20260608 - Road to 5 Million Tokens： Breaking Barriers in Long Context Training — Max Ryabinin, Together AI]] — source
