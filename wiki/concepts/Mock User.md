---
title: "Mock User"
type: concept
tags: [reinforcement-learning, agent-training, simulation, synthetic-data, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
A mock user is an LLM-based simulation of a real user, used in RL training environments to create realistic interaction scenarios for training agents. Mock users can be trained on real data (e.g., customer-agent transcripts) to simulate specific user behaviors, including difficult or emotional interactions.

## Key Information
- **Purpose**: Simulate realistic user behavior in RL agent training environments when real users aren't available or practical
- **Training**: Can be trained on real data (e.g., transcripts of customer calls) to behave like actual users, including panicked, repetitive, or difficult customers
- **CCS example**: Medical supply customers calling in panic — this "dirty real conversation" can be mocked by an LLM trained on real transcripts
- **Relationship to environment**: Mock users are one component of the [[Environment for RL Training]], alongside mock tools
- **Agent training use**: The mock user interacts with the agent-in-training, and the reward signal evaluates whether the agent handled the interaction correctly

## Related
- [[Environment for RL Training]] — the broader training setup that includes mock users
- [[Rejection Sampling for Bootstrapping]] — mock users help generate trajectories for data creation
- [[CCS]] — customer using mock users trained on real medical supply call transcripts
- [[ReinforcementLearningWithLLMs]] — the training technique that uses mock users
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
