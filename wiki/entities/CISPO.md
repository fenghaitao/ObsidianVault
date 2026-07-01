---
title: "CISPO"
type: entity
tags: [algorithm, reinforcement-learning, optimization, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
CISPO is an improvement over GRPO (Group Relative Policy Optimization), a reinforcement learning algorithm used for training LLMs. It was used in the tic-tac-toe experiment to train LFM-2 from a weak player into a master.

## Key Information
- An improvement over GRPO for LLM reinforcement learning
- Used in the Verifiers RL simple trainer for the tic-tac-toe training experiment
- Like GRPO, compares multiple rollouts from the same starting point to determine which trajectories to reinforce
- Benefits from noise reduction techniques like stratified sampling and deterministic seeding

## Related
- [[GRPO]] — predecessor algorithm
- [[Verifiers]] — library used for training
- [[TicTacToeRLTraining]] — experiment using this algorithm
- [[StratifiedSamplingInRL]] — technique to improve training stability
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
