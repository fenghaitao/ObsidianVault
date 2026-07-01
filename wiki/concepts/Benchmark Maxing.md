---
title: "Benchmark Maxing"
type: concept
tags: [evals, benchmarks, overfitting, anti-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Benchmark maxing is the practice of optimizing an AI model or agent specifically to achieve the highest possible score on a benchmark, at the expense of real-world performance. It is the Zone 3 danger zone in the [[Three Zones of Improvement]] framework — a form of [[Overfitting]] applied to evaluation rather than training.

## Key Information
- Distinct from legitimate improvement (Zone 2) which produces gains that transfer to real-world use
- Often manifests as "straight-up cheating" — exploiting benchmark-specific quirks rather than building genuine capability
- Critiqued by Ara Khan with a reference to a Meta tweet that morning: "classic benchmark maxing — just like we're doing best on the benchmark, everything's great"
- Real-world testing of benchmark-maxed models reveals they "won't hold the test of actual real-world evidence"
- The temptation is to get a great score and "make a tweet about it" — but this is counterproductive
- Requires active discipline to avoid, especially when [[Hill Climbing (Evals)]] produces diminishing returns in Zone 2
- Related to [[GoodhartsLaw]]: when a measure becomes a target, it ceases to be a good measure

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[Three Zones of Improvement]] — Zone 3 is benchmark maxing
- [[Overfitting]] — the underlying phenomenon
- [[BenchmarkSaturation]] — a related problem where benchmarks lose signal
- [[Two Camps of Wrong on Evals]] — the Objective Metrics Camp is prone to benchmark maxing
- [[GoodhartsLaw]] — the principle explaining why benchmark maxing is destructive
- [[Hill Climbing (Evals)]] — the disciplined methodology that avoids benchmark maxing
