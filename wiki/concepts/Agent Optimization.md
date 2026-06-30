---
title: "Agent Optimization"
type: concept
tags: [agents, optimization, prompt-engineering, evals, gepa]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Agent Optimization is the process of systematically improving an AI agent's performance by tuning its configuration — prompts, model choice, temperature, compaction strategy, tool registration, and other parameters — using evaluation metrics and automated optimization algorithms like GEPA.

## Key Information
- Goes beyond prompt optimization to include model selection, compaction strategy, tool registration, code mode, and other agent configuration parameters
- **GEPA approach**: Genetic algorithm that selects best candidates from the Pareto frontier, mixes them, and uses a proposer LLM to generate new candidates
- **Eval-driven**: Optimization requires a golden dataset or scoring function to measure performance improvements
- **Model-specific**: Optimization results are tied to a specific model — changing models requires re-running optimization
- **Most valuable for private data**: When models lack pre-training knowledge of a domain, optimization of context and instructions is critical
- **Cost optimization**: Shopify reduced costs from $5M/year to $73K/year by optimizing prompts and switching to a smaller model
- **Overfitting risk**: Small training sets can cause the optimizer to overfit (e.g., excluding valid relations not in training data)
- **Verbosity problem**: Optimized prompts tend to become verbose; splitting prompts into key-value pairs with selection limits can control this
- **Variance management**: Running evals many times reduces variance; some hedge funds spend $20K/night on eval runs
- **Production deployment**: Managed variables enable deploying optimized configurations without redeployment
- **Self-driving vision**: The end goal is autonomous optimization where the platform continuously hill-climbs toward better performance
- **Not always worth it**: For many use cases, eyeballing prompts and waiting for the next model release is more practical than systematic optimization

## Related
- [[GEPA]] — the optimization algorithm
- [[PromptOptimization]] — subset focusing on prompts
- [[Managed Variables]] — deployment mechanism for optimized configs
- [[Golden Dataset]] — required for eval-driven optimization
- [[Pareto Frontier]] — selection strategy
- [[EvalEngineering]] — crafting effective evaluations
- [[ModelTransferability]] — optimization is model-specific
- [[OverfittingAsExpertise]] — domain specialization trade-off
- [[Shopify]] — notable cost optimization case study
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
