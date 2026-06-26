---
title: "Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"
date: 2026-04-29
tags: [small-models, edge-models, pre-training, architecture, doom-looping, reinforcement-learning, liquid-ai]
---

## Core Thesis

Small language models are not simply scaled-down versions of large models — they have unique challenges (memory constraints, low knowledge capacity, latency sensitivity, task specificity) that require specialized architectures, training recipes, and post-training techniques. When properly optimized for their constraints and paired with agentic tools, edge models can perform remarkably well on targeted tasks.

## Key Points

- **Small model characteristics**: memory-bound, low knowledge capacity, task-specific, latency-sensitive — not general-purpose chatbots
- **Architecture innovation**: LFM 2 uses gated short convolutions + GQA hybrid architecture, with a much smaller embedding layer (only ~10% of parameters vs 63% for Gemma 3 270M), yielding more effective parameters
- **On-device profiling**: Liquid AI profiles architectures on target hardware (AMD Ryzen, Samsung Galaxy S25 Ultra) rather than relying on theoretical benchmarks
- **Training recipe**: Pre-training on 28T tokens (far beyond Chinchilla scaling laws), supervised fine-tuning, preference alignment (on-policy length-normalized DPO), and reinforcement learning with verifiable rewards
- **Doom looping solution**: Two-stage approach — on-policy data generation during DPO (temperature sampling with 5 rollouts + 1 temperature-zero rollout, LLM jury scoring) plus RL with verifiable rewards and n-gram repetition penalty
- **Agentic future**: Small models excel at agentic tasks when given web search and Python tools to compensate for low knowledge capacity and limited context windows

## Entities

- [[MaximeLabonne]] — Head of pre-training at Liquid AI, presenter
- [[LiquidAI]] — AI company focused on edge models for on-device deployment
- [[LFM]] — Liquid Foundation Models, family of small models (350M to 24B parameters)
- [[Gemma]] — Google's small model family (Gemma 3 270M, Gemma 2.5 0.8B)
- [[Qwen]] — Alibaba's model family; Qwen 3.5 0.8B referenced as a scaled-down model with high doom loop rates
- [[AMD]] — Hardware target for on-device profiling (Ryzen Max Plus 395)
- [[Samsung]] — Hardware target for on-device profiling (Galaxy S25 Ultra)
- [[HuggingFace]] — Platform where Liquid AI models are available

## Concepts

- [[EdgeModels]] — Models designed for on-device deployment with memory and latency constraints
- [[HybridArchitecture]] — Combining multiple attention/convolution mechanisms in a single model
- [[ShortConvolutions]] — Fast gated convolution blocks used in LFM 2 for latency-sensitive inference
- [[EmbeddingLayerEfficiency]] — Minimizing embedding layer size to maximize effective parameters for reasoning
- [[OnDeviceProfiling]] — Profiling model architectures on target hardware rather than using theoretical benchmarks
- [[TestTimeScalingLaws]] — New scaling laws by Roberts et al showing more pre-training tokens continue to improve small models
- [[OnPolicyDataGeneration]] — Generating training data from the policy model itself using temperature sampling for diversity
- [[VerifiableRewards]] — RL rewards based on extractable, verifiable outputs (e.g., final answers in math)
- [[NgramRepetitionPenalty]] — Penalty applied during RL to reduce repetitive text generation and doom loops
- [[AgenticReinforcementLearning]] — Using RL to train small models for agentic tool-use capabilities
- [[ColdStartSFTData]] — Including task-specific examples in SFT mixture to prime models for RL training
- [[GQA]] — Grouped Query Attention, used in LFM 2 and Gemma hybrid architectures
- [[SlidingWindowAttention]] — Attention mechanism used in Gemma 3 hybrid architecture
- [[GatedDeltaNet]] — Gated Delta Net architecture used in Gemma 2.5
- [[GatedLinearAttention]] — Linear attention variant compared against short convolutions
- [[ChinchillaScalingLaws]] — Compute-optimal training laws that small models significantly exceed in practice

## Related

- [[DoomLoop]] — Failure mode particularly severe in small reasoning models on complex tasks
- [[ModelDistillation]] — Technique used by Gemma that leads to oversized embedding layers
- [[ReinforcementLearningWithLLMs]] — RL as a key technique for small model training
- [[ModelScaling]] — Contrasting perspective: scaling up vs. optimizing small
