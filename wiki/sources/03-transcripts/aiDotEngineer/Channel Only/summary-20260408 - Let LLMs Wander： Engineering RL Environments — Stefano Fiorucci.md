---
title: "summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci"
type: source
tags: [source, transcript, reinforcement-learning, rl-environments, verifiers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Core Summary

Stefano Fiorucci from Deepset presents reinforcement learning environments for LLM evaluation and training. Using the open-source Verifiers library, he shows how to build RL environments as software artifacts and demonstrates training a small model from barely playing tic-tac-toe to mastery through RL with verifiable rewards.

## Key Points

- RL with verifiable rewards: model explores, environment scores, model learns — fundamentally different from SFT (statistical imitation).
- DeepSeek R1 and MiniMax use thousands of RL environments; DeepSeek used GRPO algorithm for lighter setup vs PPO.
- Verifiers (Prime Intellect): open-source library for building RL environments as Python packages. Supports single-turn, multi-turn, and tool environments.
- Classic RL concepts map to LLMs: model = agent, environment = data + harnesses + scoring rules, reward = verifiable outcome.
- Shift from SFT to RL: model discovers strategies through trial and error, no longer limited by human example quality.
- Demo: small model trained via RL environment goes from random tic-tac-toe play to mastery.
- Andrej Karpathy: environments "give the LLM an opportunity to actually interact, take actions, see outcomes."

## Related

- [[StefanoFiorucci]] — speaker, Deepset/Haystack
- [[Deepset]] — company behind Haystack
- [[Haystack]] — open-source LLM framework
- [[Verifiers]] — RL environment library
- [[ReinforcementLearning]] — training paradigm
- [[GRPO]] — RL algorithm
- [[DeepSeekR1]] — model using RL with verifiable rewards
