---
title: "Serverless Training"
type: concept
tags: [training, serverless, ml-infra, fine-tuning, modal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
Serverless Training is the paradigm of using on-demand, auto-scaling cloud compute resources (rather than dedicated GPU clusters) to train and fine-tune machine learning models, enabling fast iteration without infrastructure management overhead.

## Key Information
- Traditionally, training required dedicated GPU clusters isolated from production resources
- Serverless platforms (like Modal) provide on-demand GPU containers that scale to zero when idle
- Enables hyperparameter tuning by fanning out to many containers in parallel and killing unpromising runs immediately
- Supports massively parallel RL rollouts: customers scaling to 50,000–100,000 sandboxes
- Retains the fast iteration cycles of the frontier API end of the Model Spectrum while providing algorithm-level control
- Makes training accessible to teams without dedicated infrastructure engineers

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Modal]] — exemplar serverless platform
- [[Hyperparameter Tuning]] — key use case
- [[Reinforcement Learning Rollouts]] — parallel evaluation pattern
- [[Model Spectrum]] — the middle ground this enables
- [[FineTuning]] — primary training technique on serverless
