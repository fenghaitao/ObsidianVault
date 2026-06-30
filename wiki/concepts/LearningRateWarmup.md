---
title: "LearningRateWarmup"
type: concept
tags: [training, optimization, llm, stability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Learning rate warmup is the practice of starting training with a very small learning rate and gradually increasing it to the target peak over a number of initial steps. This allows the optimizer's internal state (momentum, etc.) to stabilize before making large weight updates, preventing the model from diverging early in training.

## Key Information
- Starts training with a very small learning rate and gradually increases to the peak
- Allows optimizer state (momentum estimates in Adam/AdamW) to stabilize before large updates
- Prevents the model from "going off the rails" in the first few steps when weights are random
- Angelos Perivolaropoulos's workshop used 100 warmup steps before reaching the peak learning rate
- After warmup, the learning rate follows a cosine decay schedule down to near-zero
- Without warmup, early training steps with random weights can cause large, destabilizing gradient updates
- Standard practice in LLM training; nearly all production training runs use warmup

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LearningRateScheduling]] — overall schedule including warmup
- [[CosineDecay]] — the decay phase following warmup
- [[AdamW]] — optimizer used with warmup
- [[LLMTrainingFromScratch]] — workshop context
