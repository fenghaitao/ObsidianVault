---
title: "WeightDecay"
type: concept
tags: [training, optimization, regularization, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Weight decay is a regularization technique that gradually reduces the magnitude of model weights during training, preventing them from growing too large and helping the model generalize better. In the AdamW optimizer used by Angelos Perivolaropoulos, weight decay is decoupled from the gradient update, making it more effective than in standard Adam.

## Key Information
- Gradually reduces the magnitude of model weights to prevent overfitting
- Acts as a form of L2 regularization, penalizing large weights
- In AdamW, weight decay is decoupled from the adaptive gradient update — a key improvement over standard Adam
- Works alongside the learning rate schedule: as the learning rate decays, weight decay continues to regularize
- Helps the model generalize to unseen data rather than memorizing training data
- Part of the standard training recipe for transformer models
- Angelos Perivolaropoulos noted that AdamW with cosine decay is "the most common optimizer people use" for transformer training

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[AdamW]] — optimizer that decouples weight decay
- [[LearningRateScheduling]] — related training technique
- [[Overfitting]] — the problem weight decay helps prevent
- [[LLMTrainingFromScratch]] — workshop context
