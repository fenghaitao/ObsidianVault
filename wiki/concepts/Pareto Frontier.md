---
title: "Pareto Frontier"
type: concept
tags: [optimization, genetic-algorithm, selection, gepa]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
The Pareto Frontier is a selection strategy used in GEPA optimization where only the best-performing candidates are retained and used for breeding new candidates, while poor performers are excluded. It is analogous to breeding only the best race horses to produce better offspring.

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

## Related
- [[GEPA]] — the algorithm using Pareto frontier selection
- [[Agent Optimization]] — the broader optimization process
- [[GEA]] — DSPy's related evolutionary optimizer
- [[PromptOptimization]] — the specific application to prompts
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
- [[Heterogeneous Intelligence]] — heterogeneous models shift the Pareto frontier
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
