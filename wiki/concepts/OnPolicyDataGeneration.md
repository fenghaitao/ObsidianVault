---
title: "OnPolicyDataGeneration"
type: concept
tags: [training, dpo, preference-alignment, data-generation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI.md"]
last_updated: 2026-06-26
---

## Definition
On-policy data generation is a technique for preference alignment where training data is generated from the policy model itself (the model being trained) using temperature sampling to produce diverse rollouts, which are then scored by an LLM jury to create chosen/rejected pairs for DPO training.

## Key Information
- Used in Liquid AI's preference alignment (DPO) stage
- **Pipeline**: Start with ~1M prompts → generate 5 rollouts with temperature sampling (diverse) → generate 1 rollout with temperature zero (likely to doom loop) → LLM jury scores all rollouts → best = chosen, worst = rejected
- Temperature sampling ensures diversity; at least one rollout should avoid doom loops
- Temperature-zero rollout intentionally produces lower-quality output likely to contain doom loops
- LLM jury scoring selects the best and worst responses for DPO training pairs
- Effectively trains the model to avoid doom loops during preference alignment

## Related
- [[summary-20260429 - Everything I Learned Training Frontier Small Models — Maxime Labonne, Liquid AI]] — source
- [[DoomLoop]] — problem this technique addresses
- [[LLM-as-Judge]] — scoring mechanism used
- [[TemperatureInAI]] — key parameter in rollout generation
- [[ReinforcementLearningWithLLMs]] — complementary technique
