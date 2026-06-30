---
title: "MultiHeadAttention"
type: concept
tags: [attention, transformer, architecture, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Multi-head attention runs multiple attention operations in parallel, each with its own learned projections (Q, K, V), allowing different heads to attend to different features of the input. In Angelos Perivolaropoulos's workshop, the model used 6 attention heads, with each head potentially focusing on different linguistic features like punctuation, grammar, or semantic relationships.

## Key Information
- Multiple attention heads run in parallel, each with independent Q, K, V projections
- Different heads can specialize in different features: one might attend to punctuation, another to grammar, another to semantic relationships
- The workshop model used 6 attention heads with 384 embedding dimension
- Each head's output is concatenated and projected back to the embedding dimension
- Part of the standard transformer block alongside MLP and layer normalization
- The number of attention heads is a key hyperparameter alongside number of layers and embedding dimension
- Increasing attention heads allows the model to capture more types of relationships between tokens

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[SelfAttentionMechanism]] — the underlying attention computation
- [[CausalSelfAttention]] — decoder-only variant
- [[TransformerArchitecture]] — overall architecture
- [[GroupedQueryAttention]] — variant sharing KV across query heads
