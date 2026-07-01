---
title: "StratifiedSamplingInRL"
type: concept
tags: [reinforcement-learning, training, noise-reduction, grpo, sampling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
A technique in group-based reinforcement learning (GRPO/CISPO) that forces each training batch to contain a perfectly balanced mix of difficulty levels — in the tic-tac-toe case, opponent skill spanning the chosen random move probability range — to prevent reward fluctuations caused by uneven batch composition.

## Key Information
- **Problem**: Without stratification, a small batch might randomly contain many hard opponents or many easy opponents, causing average reward to fluctuate and training to become unstable
- **Mechanism**: The `num_groups` parameter in the training configuration enforces balanced representation across the opponent difficulty spectrum in every batch
- **Why it matters**: In GRPO, differences in rewards should come from how the model plays, not from environment randomness
- **Combined with deterministic seeding**: Example seeds for starting player + turn seeds derived from example seed and board state ensure fair comparison between rollouts
- **Result**: Stable training signals that genuinely reflect model improvement rather than sampling luck
- Key to successful RL training when environment difficulty varies across examples

## Related
- [[GRPO]] — algorithm that benefits from this technique
- [[CISPO]] — improved algorithm using this technique
- [[TicTacToeRLTraining]] — experiment applying this technique
- [[BatchSizeInRLTraining]] — related hyperparameter concern
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
