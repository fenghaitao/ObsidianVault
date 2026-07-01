---
title: "TicTacToeRLTraining"
type: concept
tags: [reinforcement-learning, experiment, training, sft, grpo, verifiers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
A complete experiment demonstrating how to transform a small language model (LFM-2 by Liquid AI) from a weak tic-tac-toe player into a master using supervised fine-tuning warmup followed by reinforcement learning with verifiable rewards via CISPO.

## Key Information

**Pipeline:**
1. **Evaluation baseline**: GPT-5 Mini was a good player but not perfect; LFM-2 struggled with format and valid moves
2. **SFT warmup**: Generated 200 synthetic games using GPT-5 Mini (filtering out losses), fine-tuned LFM-2 to learn format and valid move syntax
3. **RL Phase 1**: CISPO training with opponent random move probability 20-70%, batch size 256, stratified sampling; model became very competent
4. **RL Phase 2**: Harder opponents (0-25% random moves), increased temperature for exploration; achieved 85% draws against optimal minimax opponent, outperforming the teacher model (GPT-5 Mini)

**Environment design choices:**
- Model plays as X (sometimes first, sometimes second)
- Outputs move 0-8 inside XML tags with think tags for reasoning
- Invalid moves: -0.1 penalty, game continues (not immediate loss)
- Reward functions: win (+1), format (0.2 weight), invalid move penalty
- Deterministic seeding: example seed + board state hash ensures fair comparisons
- Opponent: minimax with configurable random move probability

**Training configuration:**
- CISPO (improvement over GRPO) for RL
- Separate GPU for inference and training
- Stratified sampling ensures balanced opponent difficulty per batch
- Temperature increased in Phase 2 to force exploration beyond learned strategies

## Related
- [[CISPO]] — RL algorithm used
- [[GRPO]] — predecessor algorithm
- [[StratifiedSamplingInRL]] — key training technique
- [[HiddenBiasesInRLEnvironments]] — minimax bias lesson
- [[BatchSizeInRLTraining]] — critical hyperparameter lesson
- [[LFM]] — base model family
- [[Verifiers]] — library used for the environment
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
