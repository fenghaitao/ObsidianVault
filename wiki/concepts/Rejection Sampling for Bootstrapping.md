---
title: "Rejection Sampling for Bootstrapping"
type: concept
tags: [reinforcement-learning, synthetic-data, training-data, bootstrapping, data-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML.md"]
last_updated: 2026-06-30
---

## Definition
Rejection sampling for bootstrapping is a technique that uses an RL environment with a reward signal to generate synthetic training data. The model explores the environment, and trajectories that receive high rewards are kept while low-reward trajectories are rejected — creating a high-quality dataset to bootstrap the first model training, especially for agent use cases where training data doesn't exist in the wild.

## Key Information
- **How it works**: The RL environment produces trajectories. The reward signal identifies which trajectories are good and which are not. Good trajectories are kept (rejection sampling), creating a dataset for initial supervised fine-tuning or RL training.
- **Why it matters**: Agent training data doesn't exist in the wild — there's no scrapable data of agents using tools. RL environments produce this data as a natural byproduct.
- **Bootstrapping**: Even companies without exact training data can use this approach to create an initial dataset, then improve through the RL feedback loop
- **Leveraging existing data**: Companies can also use existing data (e.g., real customer-agent transcripts) to train mock users that generate more realistic training trajectories
- **Related to RL**: The environment and reward are the same ones used for ongoing RL training — rejection sampling is just the data-extraction step

## Related
- [[Environment for RL Training]] — the environment that produces trajectories
- [[Reward Signal]] — the mechanism that identifies good trajectories
- [[Mock User]] — used to create realistic environments for trajectory generation
- [[Synthetic Data Generation]] — broader concept
- [[Reinforcement Learning with LLMs]] — the training technique that follows bootstrapping
- [[summary-20260512 - Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML]] — source
