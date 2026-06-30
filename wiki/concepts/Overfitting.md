---
title: "Overfitting"
type: concept
tags: [training, llm, evaluation, machine-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md"]
last_updated: 2026-06-29
---

## Definition
Overfitting occurs when a model memorizes the training data rather than learning generalizable patterns, causing training loss to continue decreasing while actual performance on unseen data degrades. In Angelos Perivolaropoulos's workshop, overfitting began when the loss dropped below 1.0, with optimal performance at ~2,400 steps.

## Key Information
- Model memorizes training data instead of learning generalizable patterns
- Training loss continues decreasing, but performance on new data gets worse
- Detected by monitoring validation loss: if train loss decreases but val loss increases, the model is overfitting
- For the workshop's Shakespeare model: loss below 1.0 indicated overfitting; optimal at ~2,400 steps
- Small models with limited data are especially prone to overfitting
- Overfit models become less creative — they reproduce training data rather than generating novel text
- Validation loss is a cheap proxy metric; serious LLM training uses benchmark evaluations running alongside training
- Signs of overfitting: val loss increasing while train loss decreases, model producing memorized passages verbatim

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[ValidationLoss]] — metric used to detect overfitting
- [[CrossEntropyLoss]] — the loss function that indicates overfitting
- [[WeightDecay]] — regularization technique to prevent overfitting
- [[LLMTrainingFromScratch]] — workshop context
