---
title: "Impact Hierarchy"
type: concept
tags: [eval, optimization, improvement, prioritization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
The impact hierarchy is a prioritization framework for AI agent improvement that ranks where to invest evaluation and optimization effort, from highest to lowest impact: data quality fixes, prompting improvements, model selection, and hyperparameter tuning.

## Key Information
- **1. Data quality fixes (highest impact)**: If the agent is searching wrong sources or has stale data in its knowledge base, no amount of prompt engineering will help. Fix data first
- **2. Prompting improvements**: Few-shot examples in prompts, explicit instructions, constraints on what the agent should and shouldn't do. Often the highest ROI changes after data is fixed. Examples: requiring specific financial ratios, demanding buy/sell/hold recommendations, requiring news from last 6 months
- **3. Model selection**: Sometimes a more capable model solves problems that prompting can't, but it also costs more. Use evals to determine whether the trade-off is worth it
- **4. Hyperparameter tuning (lowest impact)**: Temperature, top P, etc. Very seldom make a meaningful difference to eval outcomes
- Each change should map to a specific failure observed in evals — data-driven prompt engineering, not random changes
- In Laurie Voss's workshop: prompt improvements (level 2) were enough to one-shot the actionability eval from 6/13 to 6/6, demonstrating that higher-impact changes aren't always needed

## Related
- [[DataFlywheel]] — the cycle powered by systematic improvement
- [[EvalEngineering]] — the practice that informs where to invest
- [[FailureModeAnalysis]] — identifying what to fix
- [[CostNormalized Accuracy]] — evaluating model selection trade-offs
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
