---
title: "Pareto Frontier"
type: concept
tags: [optimization, genetic-algorithm, selection, gepa]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
The Pareto Frontier has two key applications in AI:

1. **Optimization (GEPA)**: A selection strategy where only the best-performing candidates are retained and used for breeding new candidates, while poor performers are excluded. Analogous to breeding only the best race horses.

2. **Model evaluation**: A visualization methodology that plots efficiency (latency or price) on the x-axis vs. quality (Elo score or task-specific metric) on the y-axis. The Pareto frontier reveals that there is not a single state-of-the-art model, but multiple models along the frontier — each representing a different quality-efficiency tradeoff.

## Key Information
- Core selection mechanism in GEPA (Genetic Evolutionary Pareto Algorithm)
- **Analogy**: Like breeding race horses — you take the best race horses and breed them, not add slow horses into the mix
- Only candidates on the Pareto frontier (best performers across all metrics) are selected for mixing
- The proposer agent receives context about frontier candidates to generate new prompt variations
- New candidates are evaluated, and if they outperform existing frontier members, they join the frontier
- Enables exploration of the prompt space while maintaining quality
- Can operate on multi-key dicts: if optimizing multiple variables (model, prompt, tools), the frontier contains the best combinations across all dimensions
- Contrasts with exhaustive search — focuses computational resources on promising regions
- In [[Heterogeneous Intelligence]]: heterogeneous model mixtures shift the Pareto frontier beyond what any singular model can achieve — Callosum demonstrated this on Video Web Arena where a mixture of Quant 3 VL8B and Kimi K2.5 outperformed either alone
- **Model evaluation use**: When evaluating models, the Pareto frontier shows multiple SOTA models — quality may vary only between 1100-1200 Elo while efficiency varies 20x. [[Pruna]] used this to show that ChatGPT Image (20 days compute) and an optimized model (7 hours) are both on the frontier at different efficiency points
- **Task-specific frontiers**: Even more informative when using task-specific quality metrics (e.g., text rendering) rather than general capability scores — Pruna and [[Black Forest Labs]] optimized Flux 2 Flex to stay on the text rendering Pareto frontier while being way faster

## Related
- [[GEPA]] — the algorithm using Pareto frontier selection
- [[Agent Optimization]] — the broader optimization process
- [[GEA]] — DSPy's related evolutionary optimizer
- [[PromptOptimization]] — the specific application to prompts
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
- [[Heterogeneous Intelligence]] — heterogeneous models shift the Pareto frontier
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source (model evaluation use)
- [[Model Efficiency]] — the efficiency dimension of the Pareto frontier
- [[StateOfTheArt Ambiguity]] — the Pareto frontier resolves SOTA ambiguity by showing multiple optimal models
