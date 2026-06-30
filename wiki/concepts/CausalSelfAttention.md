---
title: "CausalSelfAttention"
type: concept
tags: [attention, transformer, architecture, llm, decoder]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Causal self-attention is the attention mechanism used in decoder-only transformer models (like GPT-2) where each token can only attend to itself and previous tokens in the sequence — not future tokens. This enables autoregressive next-token prediction, the fundamental training objective of generative LLMs.

## Key Information
- Used in decoder-only causal models like GPT-2, which is the architecture basis for the workshop
- Each token can only attend to itself and previous tokens (causal mask prevents attending to future tokens)
- Enables autoregressive generation: the model predicts the next token given all previous tokens
- The fundamental mechanism hasn't changed much from GPT-2 to modern LLMs
- Different attention heads attend to different features (punctuation, grammar, etc.)
- Attention allows the model to understand relationships between tokens — e.g., "blue" and "sky" have high correlation
- The quality of these relationships depends heavily on the tokenizer: word-level tokens make correlations easier than character-level tokens
- Scaling to very long contexts (1M+) requires architectural innovations beyond simply increasing the block_size parameter

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[SelfAttentionMechanism]] — general attention mechanism
- [[MultiHeadAttention]] — multiple attention heads
- [[TransformerArchitecture]] — overall architecture
- [[NextTokenPrediction]] — training objective enabled by causal attention
- [[GPT-2]] — architecture using causal self-attention
