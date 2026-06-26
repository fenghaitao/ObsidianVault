---
title: "Triton"
type: entity
tags: [language, gpu, kernel, openai, programming]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
Triton is OpenAI's GPU kernel programming language used for writing efficient low-level operations like attention mechanisms, layer normalization, and matrix multiplications in LLM implementations.

## Key Information
- Used to write forward and backward kernels for operations like layer normalization in LLM implementations
- The forward kernel for LayerNorm in Triton is relatively simple (few lines of actual computation, with the rest being data loading)
- The backward kernel (differentiation through LayerNorm) is significantly more complex due to derivatives through row sums and normalization operations
- Daniel Han has tutorials on writing Triton kernels for LLM components
- Enables custom, high-performance implementations of transformer operations beyond what PyTorch natively provides

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[LayerNorm]] — operation implemented with Triton kernels
- [[SelfAttentionMechanism]] — attention kernel often written in Triton
- [[DanielHan]] — provides tutorials on Triton
- [[FlashAttention]] — efficient attention often implemented via Triton
