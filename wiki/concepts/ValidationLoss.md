---
title: "ValidationLoss"
type: concept
tags: [evaluation, training, llm, machine-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Validation loss is the cross-entropy loss computed on a held-out portion of data the model never sees during training. It serves as a proxy metric for detecting overfitting — if training loss decreases but validation loss increases, the model is memorizing rather than learning. In Angelos Perivolaropoulos's workshop, validation loss was computed periodically to find the optimal stopping point (~2,400 steps).

## Key Information
- Computed on data the model has never seen during training (held-out validation set)
- If train loss decreases but val loss increases → overfitting
- If both decrease → model is genuinely learning
- A cheap proxy metric for model quality; serious LLM training uses benchmark evaluations
- In the workshop, the Shakespeare data was split into training and validation sets
- Validation loss was monitored during training to determine when to stop
- For this specific setup, optimal performance was at ~2,400 steps
- After this point, val loss started increasing even though train loss continued decreasing
- The model was run in forward-pass-only mode on validation data (no gradient computation)

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[Overfitting]] — the problem validation loss detects
- [[CrossEntropyLoss]] — the loss function used
- [[LLMTrainingFromScratch]] — workshop context
