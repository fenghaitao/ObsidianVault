---
title: "CLIP Score"
type: concept
tags: [evaluation, metric, image-generation, clip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
CLIP score is a standard automated metric for evaluating image generation models. While commonly used as a first-check metric, it has significant limitations: rankings change across different datasets, and score variations between models are often too small to reliably distinguish them.

## Key Information
- **Common first-check metric**: When people evaluate image models, they often check CLIP score first
- **Ranking instability**: Rankings change completely across different datasets — a model ranked #1 on one dataset may rank much lower on another
- **Small score variations**: CLIP scores are typically between 0-1 or 0-100, but differences between models are often super small, making it hard to determine which model is truly best
- **Better alternative**: Use task-specific metrics that align with your use case. For example, text rendering metrics produce much more consistent rankings with significant, clearly distinguishable differences between models
- **Recommendation**: Understand what the metric actually measures, use multiple metrics, and prefer task-specific metrics over general ones

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[Manual Inspection Bias]] — the subjective alternative CLIP score tries to complement
- [[Public Leaderboards]] — where CLIP scores (or derived metrics) are published
- [[StateOfTheArt Ambiguity]] — metric inconsistency contributes to the ambiguity
