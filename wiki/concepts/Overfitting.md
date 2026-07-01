---
title: "Overfitting"
type: concept
tags: [training, llm, evaluation, machine-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
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

### Eval Overfitting (Zone 3)

In the context of agent evaluation, overfitting manifests as [[Benchmark Maxing]] — optimizing an agent or model specifically to achieve high benchmark scores at the expense of real-world performance. This is Zone 3 of the [[Three Zones of Improvement]] framework and must be actively avoided during [[Hill Climbing (Evals)]]. Unlike Zone 2 (nuanced, model-specific improvements that transfer to real use), Zone 3 overfitting produces gains that don't generalize.

## Related
- [[summary-20260504 - Training an LLM from Scratch, Locally — Angelos Perivolaropoulos, ElevenLabs]] — source
- [[ValidationLoss]] — metric used to detect overfitting
- [[CrossEntropyLoss]] — the loss function that indicates overfitting
- [[WeightDecay]] — regularization technique to prevent overfitting
- [[LLMTrainingFromScratch]] — workshop context
- [[Benchmark Maxing]] — eval overfitting in the agent context
- [[Three Zones of Improvement]] — Zone 3 is the overfitting danger zone
- [[Hill Climbing (Evals)]] — methodology that must avoid overfitting
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source (eval overfitting)
