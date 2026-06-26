---
title: "VerifiableRewards"
type: concept
tags: [reinforcement-learning, training, rewards, verification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
Verifiable rewards are a reinforcement learning technique where rewards are based on extractable, objectively verifiable outputs (such as final answers in math problems) rather than subjective quality judgments, naturally penalizing incomplete or looping responses that fail to produce a valid answer.

## Key Information
- Used in Liquid AI's RL stage for small models
- **Mechanism**: Extract final answer from model output → if no valid answer exists, no positive reward
- Naturally addresses doom looping because looping responses never produce extractable final answers
- Particularly effective for math, code, and other tasks with objectively correct outputs
- Combined with n-gram repetition penalty for additional doom loop prevention
- Works with temperature sampling to produce diverse rollouts

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[ReinforcementLearningWithLLMs]] — broader technique
- [[DoomLoop]] — problem this helps solve
- [[NgramRepetitionPenalty]] — complementary technique
- [[VerificationAsymmetry]] — related principle
