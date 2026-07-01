---
title: "BatchSizeInRLTraining"
type: concept
tags: [reinforcement-learning, training, hyperparameters, stability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
In reinforcement learning training for LLMs, batch size (the number of games/trajectories used to update model weights) is a critical hyperparameter. Small batch sizes cause unstable training and model collapse, while larger batch sizes provide stable learning at the cost of apparent slowness.

## Key Information
- **Small batch risk**: If batch size is too low, the model learns from a very small number of matches and opponent types at once, reinforcing suboptimal strategies
- **Observed failure**: In the tic-tac-toe experiment, values below 256 caused unstable training and model collapse
- **Large batch benefit**: Batch size of 256+ forces the model to learn from diverse matches and opponent types, leading to generalizable strategies
- **Trade-off**: Large batches appear to learn slowly but produce stable, genuinely improving models; small batches show apparent progress that collapses
- **Interaction with stratified sampling**: Larger batches make stratified sampling more effective by naturally including diverse opponent difficulties
- **Recommendation**: Start training with a large enough batch size and let it run — don't prematurely tweak based on early plot fluctuations

## Related
- [[StratifiedSamplingInRL]] — complementary technique
- [[TicTacToeRLTraining]] — experiment where this was discovered
- [[GRPO]] — algorithm sensitive to batch size
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
