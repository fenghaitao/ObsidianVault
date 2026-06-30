---
title: "Model Dissatisfaction Rate"
type: concept
tags: [model-evaluation, arena, human-preference, dissatisfaction, benchmark]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
Model Dissatisfaction Rate is an Arena.ai metric that tracks how often users vote "both models give a bad response" in blind A/B battles between top AI models. It serves as a complementary signal to win rates, capturing the frequency with which even the best models fail to meet user expectations.

## Key Information
- **Source**: Arena.ai battle mode — users can vote A, B, or "both bad"
- **Current rate**: ~9% for top 25 models (Q1 2026)
- **Historical trend**: ~20-17% pre-reasoning era → ~12% after o1 → ~9% now
- **Interpretation**: 9% of the time, two top models both produce unsatisfactory responses — improvement is real but not zero
- **Category breakdown** (top 25 models, expert prompts):
  - Math/quantitative: dropped dramatically (25-27% → much lower)
  - Creative writing: improved modestly
  - Medical, finance, law: flat — barely improved
  - Software (overall): 23.5% → 13% (Q2 2024 → Q1 2026)
  - Software subcategories: uneven — gaming, security, GPU compute show mixed progress
- **Key insight**: Unlike static benchmarks that can be saturated, dissatisfaction rate captures shifting user expectations — as models improve, users ask harder questions
- **Data published on Hugging Face** by Arena.ai

## Why It Matters
- Provides a long-running, non-saturating metric that static benchmarks can't match
- Captures the full breadth of user tasks, not just narrow benchmark categories
- Reveals that improvement is uneven — some categories barely budge while others improve dramatically
- Challenges the "line goes up" narrative by showing that even top models fail 9% of the time

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[Arena.ai]] — platform that produces this metric
- [[Peter Gostev]] — presenter of this data
- [[BullshitBench]] — complementary benchmark from same researcher
- [[BenchmarkSaturation]] — contrast with static benchmarks
- [[Model Evaluation]] — broader context
- [[HuggingFace]] — where data is published
