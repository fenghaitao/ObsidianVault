---
title: "GPT-2"
type: entity
tags: [model, llm, openai, transformer, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
GPT-2 is a decoder-only causal transformer model released by OpenAI, whose architecture serves as the basis for the workshop model trained by Angelos Perivolaropoulos. Its fundamental building blocks — multi-head self-attention, MLP layers, layer norms, and residual connections — remain largely unchanged in modern LLMs, though newer models add optimizations for longer context and better scaling.

## Key Information
- Decoder-only causal model architecture that serves as the foundation for many modern LLMs
- The fundamental building blocks (attention, MLP, layer norms, residuals) haven't changed much from GPT-2 to current models
- Newer models are more specialized for longer context and scaling to more tokens, but the core architecture is the same
- When OpenAI was about to release GPT-2, they claimed it was "too dangerous for humanity" — the code was essentially what a few hundred lines of PyTorch can implement today
- Standard GPT-2 embedding dimension is 384, which is used in the workshop model
- GPT-2's tokenizer vocabulary is 50,000 tokens, which would create a 19M parameter embedding table alone (50K × 384) — more than 3× the entire workshop model
- The workshop model uses the GPT-2 architecture but with only 65 tokens (character-level) and 1.8M total parameters

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[GPT-3]] — successor model using same fundamental architecture
- [[TransformerArchitecture]] — the underlying architecture
- [[AndrejKarpathy]] — co-founder of OpenAI
- [[nanoGPT]] — educational GPT implementation
- [[LLMTrainingFromScratch]] — workshop that uses GPT-2 architecture
