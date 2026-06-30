---
title: "Win Rate"
type: concept
tags: [evaluation, model-comparison, benchmarking, leaderboards]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Win rate is the percentage of head-to-head battles a model wins against other models in leaderboard evaluations. It reveals that even the highest-ranked models are not universally superior — they lose a significant fraction of comparisons, meaning the "best" model is wrong for a meaningful percentage of use cases.

## Key Information
- **No model wins everything**: Even top-ranked models on leaderboards lose at least 40% of their head-to-head battles
- **Implication for model selection**: If your specific use case falls within the 40% of battles the "best" model loses, selecting that model based on aggregate ranking alone will give you the wrong model
- **Statistical perspective**: Win rates underscore the need to evaluate on many samples — the more battles, the more reliable the win rate estimate
- **Relationship to Elo**: Win rates are the raw data from which [[Elo Score]] rankings are derived
- **Practical takeaway**: Rather than trusting aggregate rankings, evaluate models on your own data under your specific use case conditions

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[Elo Score]] — derived from win rates
- [[Public Leaderboards]] — where win rates are computed
- [[State-of-the-Art Ambiguity]] — win rates are a key reason SOTA is ambiguous
- [[Pareto Frontier]] — alternative evaluation that considers efficiency alongside quality
