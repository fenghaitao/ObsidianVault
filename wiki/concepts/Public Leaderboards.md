---
title: "Public Leaderboards"
type: concept
tags: [evaluation, benchmarking, model-comparison, leaderboards]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
Public leaderboards are aggregated rankings of AI model performance published online. They are the most common first stop for practitioners trying to determine which model is "state-of-the-art," but they suffer from inconsistency, lack of task specificity, and limited statistical significance when used naively.

## Key Information
- **Key leaderboards for image editing**: Design Arena, LM Arena (now called Arena), and Artificial Analysis
- **Inconsistency problem**: The three leaderboards produce different rankings. A model ranked #10 on Artificial Analysis may be ranked #5 on Arena. Elo score ranges differ completely between platforms (e.g., 1100-1300 on one, completely different on another)
- **Model coverage varies**: Some models appear on some leaderboards but not others; duplicate entries add noise
- **Aggregate vs. task-specific**: General leaderboards average over many tasks, obscuring per-task performance. Task-specific leaderboards for individual use cases (e.g., removing objects) show completely different rankings — ChatGPT Image is never #1 on any specific task
- **Sample size limitations**: Most leaderboards are built on only a few thousand samples — negligible compared to millions of daily inferences in production applications
- **Best practice**: Never trust a single leaderboard. Look at multiple, target your specific use case, and consider that models with approximately equivalent rankings are likely comparable

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[State-of-the-Art Ambiguity]] — the broader problem public leaderboards contribute to
- [[Elo Score]] — the scoring mechanism used by leaderboards
- [[Win Rate]] — what leaderboard rankings are derived from
- [[Pareto Frontier]] — better alternative to naive leaderboard checking
- [[Design Arena]] — specific image editing leaderboard
- [[LM Arena]] — general model leaderboard (now "Arena")
- [[Artificial Analysis]] — AI model comparison platform
- [[Game Arena]] — Kaggle's PvP benchmark platform
