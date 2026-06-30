---
title: "Reinforcement Learning Rollouts"
type: concept
tags: [reinforcement-learning, training, parallelism, modal]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
Reinforcement Learning Rollouts are the massively parallel evaluation phase in RL training where a model generates many candidate outputs across independent environments to collect reward signals for learning. Modern serverless platforms enable scaling rollouts to tens of thousands of sandboxes simultaneously.

## Key Information
- Rollouts are an "embarrassingly parallel" evaluation problem — each rollout is independent
- Modern open-source RL libraries make RL accessible in ~300 lines of code
- Modal customers have scaled to 50,000–100,000 sandboxes for RL rollouts
- Unified APIs for sandboxes and GPU containers enable seamless scaling between training and evaluation
- Part of the broader trend making fine-tuning and RL training accessible without dedicated infrastructure teams

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Serverless Training]] — the infrastructure paradigm enabling this
- [[Modal]] — platform with unified sandbox/GPU APIs
- [[Fine-tuning]] — related training technique
- [[Reinforcement Learning]] — broader RL concept
