---
title: "SingleTurnEnvironments"
type: concept
tags: [reinforcement-learning, environments, verifiers, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
Single-turn environments are the simplest type of RL environment in Verifiers, with just one interaction between the model and the environment. The model receives a question, generates a response, and the environment evaluates it.

## Key Information
- **Workflow**: Load environment → sample dataset examples → prepare conversation with system prompt and question → send to model → parse response → compute reward → save results
- **Components**: Dataset loading and mapping, XML/structured parser, reward function (e.g., longest common subsequence ratio), rubric (collection of weighted rewards)
- **Example**: Reverse text environment — model must reverse a text paragraph; reward compares output to ground truth
- **Evaluation run**: Each example used multiple times (e.g., 3 rollouts) with same question but different completions due to model randomness
- **Results**: Summary statistics and reward distribution at end of evaluation
- Training follows the same core mechanism with the additional step of updating model parameters
- Contrasts with multi-turn environments that involve multiple agent-environment exchanges per trajectory

## Related
- [[MultiTurnEnvironments]] — more complex alternative
- [[Verifiers]] — library providing this abstraction
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
