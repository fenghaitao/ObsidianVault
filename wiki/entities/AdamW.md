---
title: "AdamW"
type: entity
tags: [optimizer, training, deep-learning, pytorch]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
AdamW is a variant of the Adam optimizer that decouples weight decay from the gradient update, making it the most common optimizer for training transformer models. Angelos Perivolaropoulos used it in his LLM training workshop with a cosine decay learning rate schedule.

## Key Information
- The most common optimizer used for training transformer models (at least historically)
- Used in the workshop with a cosine decay learning rate schedule
- Supports the concept of controlling the learning rate over time: warmup from low → peak → cosine decay to near-zero
- Angelos noted there are "better normalizers" now, but AdamW is the simplest to start with
- Works with the learning rate schedule: 100-step warmup, then cosine decay over 5,000 total steps

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LearningRateScheduling]] — learning rate management
- [[CosineDecay]] — decay schedule used
- [[WeightDecay]] — decoupled weight decay
- [[LLMTrainingFromScratch]] — workshop context
