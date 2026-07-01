---
title: "MultiTurnEnvironments"
type: concept
tags: [reinforcement-learning, environments, verifiers, agent-interaction]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
Multi-turn environments are RL environments where each trajectory involves multiple interactions between the model (agent) and the environment. They form the foundation for all environment types in Verifiers, implementing the core single-agent rollout loop.

## Key Information
- **State**: A dictionary tracking information during a rollout, initialized via `setup_state`
- **Env response**: The environment can reply with dynamically generated messages based on state, not just static responses
- **Stop condition**: A decorated method that runs at every turn; once it returns true, the rollout terminates
- **Loop mechanics**: Model and environment take turns exchanging messages, updating shared state, until stopping condition is met
- **Foundation**: All other Verifiers environment types (Tool, MCP, Stateful Tool) are built on multi-turn
- **Examples**: Double-check environment (model answers math, then asked "Are you sure?"), tic-tac-toe (multiple moves per game)
- Contrasts with single-turn environments where the interaction ends after one model response

## Related
- [[SingleTurnEnvironments]] — simpler alternative
- [[ToolEnvironments]] — built on multi-turn foundation
- [[Verifiers]] — library providing this abstraction
- [[TicTacToeRLTraining]] — multi-turn environment example
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
