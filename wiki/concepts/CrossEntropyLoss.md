---
title: "CrossEntropyLoss"
type: concept
tags: [training, loss-function, llm, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Cross-entropy loss is the standard loss function for training language models. It measures the difference between the model's predicted token distribution and the actual next token. In Angelos Perivolaropoulos's workshop, the loss started at ~4.17 (ln(65), completely random) and decreased as the model learned to predict Shakespearean text.

## Key Information
- Standard loss function for next-token prediction in LLM training
- Measures how well the predicted probability distribution matches the actual next token
- Training works by offsetting the sequence by one: input is tokens T₀...Tₙ, target is T₁...Tₙ₊₁
- The model learns to predict each next token given all previous tokens
- Initial loss for the workshop model: ln(65) ≈ 4.17 (random guessing among 65 tokens)
- Loss progression indicates learning: 3.3 (character frequencies), 2.5 (bigrams), 1.5-2.0 (words), 1.0-1.2 (decent text)
- Below 1.0 loss indicates overfitting for this dataset
- Computed during the forward pass alongside logits; backward pass uses the loss to compute gradients

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[NextTokenPrediction]] — the training objective using cross-entropy
- [[Overfitting]] — indicated by very low cross-entropy loss
- [[ValidationLoss]] — cross-entropy on held-out data
- [[LLMTrainingFromScratch]] — workshop context
