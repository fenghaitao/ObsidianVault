---
title: "HiddenBiasesInRLEnvironments"
type: concept
tags: [reinforcement-learning, environments, debugging, training-pitfalls, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
Hidden biases in RL environments are subtle implementation details that cause models to memorize specific patterns rather than learn general strategies. They produce misleadingly good benchmark results while the model fails in real interactions.

## Key Information
- **Example (minimax bias)**: A naive minimax algorithm that always selects the first free position when multiple moves have the same optimal score. Over many games, the model memorizes this specific opponent pattern instead of learning general tic-tac-toe strategy
- **Detection**: Programmatic evaluation showed great results, but playing against the model revealed it was "clueless" — it had only learned to beat one specific opponent implementation
- **Solution**: Use randomized tie-breaking in deterministic algorithms, or vary opponent behavior
- **General principle**: Any deterministic pattern in the environment that the model can exploit becomes a memorization shortcut instead of genuine learning
- **Recommendation**: Always test models in the real task after training, not just programmatic evaluation — inspect rollouts and try the model yourself

## Related
- [[TicTacToeRLTraining]] — experiment where this bias was discovered
- [[RLEnvironmentsForLLMs]] — broader context
- [[BatchSizeInRLTraining]] — another training pitfall
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
