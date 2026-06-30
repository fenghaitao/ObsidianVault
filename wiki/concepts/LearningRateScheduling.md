---
title: "LearningRateScheduling"
type: concept
tags: [training, optimization, llm, deep-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Learning rate scheduling is the practice of varying the learning rate during training — typically starting low (warmup), increasing to a peak, then gradually decaying. Angelos Perivolaropoulos's workshop used a 100-step warmup followed by cosine decay over 5,000 total steps with the AdamW optimizer.

## Key Information
- Controls how much the model weights move toward the optimization direction at each step
- Too high a learning rate causes the model to "go off the rails" and become unstable
- Too low a learning rate means the model learns too slowly or gets stuck in poor local minima
- Standard schedule: warmup (start low → increase to peak) → decay (peak → gradually decrease)
- Workshop schedule: 100-step warmup, then cosine decay from peak to near-zero over 5,000 steps
- The peak learning rate should be as high as possible without causing instability
- Weight decay reduces the learning rate as training progresses, allowing large changes early and fine calibration later
- Some practitioners prefer not to decay to zero, as it makes restarting training difficult
- The AdamW optimizer implements this schedule via cosine decay

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LearningRateWarmup]] — the warmup phase
- [[CosineDecay]] — the decay schedule used
- [[WeightDecay]] — regularization component
- [[AdamW]] — optimizer implementing the schedule
- [[LLMTrainingFromScratch]] — workshop context
