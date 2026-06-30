---
title: "Arena.ai"
type: entity
tags: [platform, benchmark, model-evaluation, human-preference, arena]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
Arena.ai is a model evaluation platform that collects human preference data through blind A/B battles. Users submit prompts, receive responses from two anonymous models, and vote which is better — or vote that both are bad. With 5.5M+ votes across 700+ text models since Q2 2023, it provides one of the longest-running and broadest views of model performance.

## Key Information
- **Battle mode**: Users submit a query, get two anonymous model responses, vote A or B (or "both bad")
- **Text Arena**: 5.5M+ votes collected since Q2 2023
- **700+ text models** tracked over time
- **Dissatisfaction rate**: The "both models bad" vote mechanic — currently ~9% for top 25 models (down from ~20% pre-reasoning era)
- **Expert category**: Filters to high-signal prompts from domain experts, narrowed to top 25 model battles (~40,000 prompts)
- **Key advantage over static benchmarks**: Cannot be exhausted — users can always ask new questions; captures the full breadth of what users actually care about, not just narrow benchmark tasks
- **Category trends**: Math dissatisfaction dropped dramatically; creative writing improved modestly; medical, finance, law barely improved
- **Software subcategories**: Overall 23.5% → 13% dissatisfaction (Q2 2024 → Q1 2026), but gaming, security, and other subcategories show uneven progress
- **Data published on Hugging Face**: leaderboards, expert prompts, and other datasets shared publicly
- Also offers private evals for model trainers

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[Peter Gostev]] — researcher at Arena.ai
- [[BullshitBench]] — benchmark created by Arena researcher
- [[Model Dissatisfaction Rate]] — key Arena metric
- [[Model Evaluation]] — broader context
- [[BenchmarkSaturation]] — contrast with static benchmarks
- [[HuggingFace]] — where Arena publishes data
