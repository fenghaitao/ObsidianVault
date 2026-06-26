---
title: "LLaMA"
type: entity
tags: [model, meta, architecture, llm, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - Low Level Technicals of LLMs： Daniel Han.md"]
last_updated: 2026-06-26
---

## Definition
LLaMA (Large Language Model Meta AI) is Meta's open-source language model family whose decoder-only transformer architecture serves as the canonical reference for understanding modern LLM internals.

## Key Information
- Daniel Han uses the LLaMA architecture as the canonical example to walk through all components of a transformer decoder
- Architecture includes: token embedding, RoPE positional encoding, repeated decoder layers (e.g., 32 layers), each with attention + MLP blocks wrapped in LayerNorm and residual connections, and a final LM head outputting token probabilities
- The LLaMA architecture is the basis for understanding how newer models deviate from established patterns
- Serving as the reference implementation helps identify bugs when other models (Gemma, Nemotron) differ from expected architecture patterns

## Related
- [[summary-20240731 - Low Level Technicals of LLMs： Daniel Han]] — source
- [[SelfAttentionMechanism]] — core component of LLaMA architecture
- [[RoPE]] — positional encoding used in LLaMA
- [[LayerNorm]] — normalization used throughout LLaMA
- [[GroupedQueryAttention]] — attention variant used in newer LLaMA versions
