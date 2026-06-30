---
title: "CosineDecay"
type: concept
tags: [training, optimization, learning-rate, scheduling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Cosine decay is a learning rate schedule that reduces the learning rate following a cosine curve from a peak value down to near-zero over the remaining training steps. Angelos Perivolaropoulos's workshop used cosine decay after a 100-step warmup, decaying over 5,000 total steps with the AdamW optimizer.

## Key Information
- Follows a cosine curve: starts at peak, smoothly decreases to near-zero
- Used after the warmup phase to gradually reduce the learning rate
- Workshop schedule: 100-step warmup → cosine decay from peak over remaining 4,900 steps (5,000 total)
- The smooth decay allows large changes early in training (to find good minima) and fine calibration later
- Implemented via the AdamW optimizer in the workshop
- Some practitioners prefer not to decay to exactly zero, as it makes restarting training difficult
- Cosine decay is one of several decay schedules; others include linear decay, step decay, and exponential decay

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[LearningRateScheduling]] — overall scheduling concept
- [[LearningRateWarmup]] — the warmup phase preceding decay
- [[WeightDecay]] — related regularization technique
- [[AdamW]] — optimizer implementing cosine decay
- [[LLMTrainingFromScratch]] — workshop context
