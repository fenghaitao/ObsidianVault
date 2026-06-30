---
title: "Distributional Control"
type: concept
tags: [benchmarks, evaluation, taxonomy, task-distribution, diversity]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI.md"]
last_updated: 2026-06-30
---

## Definition
Distributional Control is the second "science" axis of [[Benchmarking Agents]]. It means defining a clear taxonomy for the target domain and intentionally distributing benchmark tasks across that taxonomy — either to represent real-world traffic distributions or to characterize disproportionately important (but rare) failure modes.

## Key Information
- Two approaches: (1) capture real-world traffic distribution, or (2) taxonomize failure modes that are rare but disproportionately important
- Analogy: in self-driving, pedestrians and motorcyclists appear less often than highway driving but are disproportionately important to get right
- Exemplar: [[MMLU]] constructed a taxonomy of 57 academic and professional domains across STEM, humanities, etc.
- A hallmark of great benchmarks: being really intentional about distributing tasks
- Prevents benchmarks from over-representing easy or common scenarios while under-representing critical edge cases

## Related
- [[Benchmarking Agents]] — parent framework
- [[MMLU]] — exemplar benchmark
- [[Task Quality (Benchmarks)]] — complementary science axis
- [[Model Headroom]] — complementary science axis
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — source transcript
