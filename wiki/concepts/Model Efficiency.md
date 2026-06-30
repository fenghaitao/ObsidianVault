---
title: "Model Efficiency"
type: concept
tags: [evaluation, optimization, compute, cost, latency, pareto-frontier]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Model efficiency is the consideration of compute cost, latency, energy consumption, and price alongside quality when evaluating AI models. It challenges the assumption that the highest-quality model is always the best choice, showing that comparable quality can often be achieved at a fraction of the resource cost.

## Key Information
- **Quality is not the only dimension**: People tend to look only at quality, but the additional quality gain from larger models is often not worth the efficiency cost
- **Concrete comparison**: ChatGPT Image evaluation: 20 days of compute, $5,000, 556 kWh (~400 marathons). Optimized model: 7 hours, $265, ~4 marathons of energy — ~70x faster and ~19x cheaper for the same workload
- **Pareto frontier approach**: Plot efficiency (latency or price) on x-axis vs. quality (Elo score) on y-axis. The Pareto frontier reveals multiple state-of-the-art models — quality may only vary between 1100-1200 Elo while efficiency varies 20x
- **Task-specific efficiency**: Even more informative when the quality axis uses task-specific metrics (e.g., text rendering) rather than general capability scores
- **Efficiency techniques**: [[Quantization]] (module-specific), [[Model Pruning]] (removing unimportant components), denoising step reduction (from 50 steps to 4-20 via [[ModelDistillation]] or caching)
- **Key takeaway**: There is not one state-of-the-art model — there are multiple along the efficiency-quality frontier

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[Pareto Frontier]] — the visualization methodology for efficiency vs. quality
- [[Performance Models]] — Pruna's term for efficiency-optimized models
- [[Quantization]] — compression technique for efficiency
- [[Model Pruning]] — compression technique for efficiency
- [[ModelDistillation]] — compression technique for efficiency
- [[StepCaching]] — technique for reducing denoising steps
- [[State-of-the-Art Ambiguity]] — efficiency is a key dimension ignored in naive SOTA claims
