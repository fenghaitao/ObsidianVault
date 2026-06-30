---
title: "Environment for RL Training"
type: concept
tags: [reinforcement-learning, agent-training, simulation, tools, mock-user]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
An environment for RL training is the simulated or real-world context in which an agent (LLM) operates during reinforcement learning. It includes tools the agent can use, users the agent interacts with, and a reward signal that evaluates outcomes. RL was originally designed for training agents in environments, making it a natural fit for LLM agent training.

## Key Information
- **Two scenarios**: (1) The environment already exists — e.g., Manulife had agents in production with settled workflows, so the model could be plugged directly into the existing environment, (2) The environment must be built — mock tools and mock users are created to simulate the target scenario
- **Components**: Tools (APIs, databases, functions the agent can call), users (real or mock), and a reward signal
- **Agent training data**: The environment produces trajectories as a byproduct, solving the problem that agent training data doesn't exist in the wild
- **Reward definition**: Success is defined by business outcomes, KPIs, or LLM-as-judge evaluations within the environment
- **Natural fit for RL**: RL was originally created to train robots/agents to live in environments and take actions — LLM agents are a natural extension

## Related
- [[Mock User]] — the simulated user component of the environment
- [[Rejection Sampling for Bootstrapping]] — using environment trajectories for data creation
- [[Reward Signal]] — the evaluation mechanism within the environment
- [[Reinforcement Learning with LLMs]] — the training technique
- [[Manulife]] — customer with existing agent environment
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
