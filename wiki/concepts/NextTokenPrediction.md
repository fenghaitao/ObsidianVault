---
title: "NextTokenPrediction"
type: concept
tags: [training, llm, objective, transformer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Next-token prediction is the fundamental training objective of autoregressive language models: given a sequence of previous tokens, predict the most probable next token. The training data is offset by one — input is T₀...Tₙ, target is T₁...Tₙ₊₁ — and cross-entropy loss measures prediction accuracy. Poolside considers this an "amazing technological breakthrough" but argues it must be paired with reinforcement learning to achieve more capable intelligence.

## Key Information
- **Role**: The base mechanism underlying modern LLMs and transformer architectures
- **Training mechanics**: Input sequence is offset by one from target sequence; the model learns to predict each next token given all previous tokens
- **Loss function**: Cross-entropy loss measures the difference between predicted and actual next token
- **Initial loss**: For a model with V possible tokens, random guessing gives loss = ln(V); for the workshop's 65 tokens, this was ~4.17
- **Poolside's View**: Necessary but insufficient on its own for advancing toward AGI-level capabilities
- **Pairing**: Must be combined with reinforcement learning for the next leap in intelligence
- **Evolution**: The world has progressed from completions to chat to agentic systems, all built on this foundation
- **Causal masking**: Requires causal self-attention so the model cannot "cheat" by looking at future tokens

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[ReinforcementLearningWithLLMs]]
- [[Poolside]]
- [[AGI]]
- [[MalibuAgent]]
- [[CrossEntropyLoss]] — the loss function used
- [[CausalSelfAttention]] — the attention mechanism enabling this objective
- [[LLMTrainingFromScratch]] — workshop context
