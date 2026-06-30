---
title: "Intelligence Per Joule"
type: concept
tags: [metrics, efficiency, hardware, benchmarking, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md"]
last_updated: 2026-06-30
---

## Definition
Intelligence per joule is a metric for AI efficiency that measures model quality at a specific task divided by the energy consumed, tracking how much "intelligence" you get per unit of energy. It is improving exponentially, with a ~5x improvement over 2 years from hardware and ~3x from model improvements.

## Key Information
- Developed by Hazy Research at Stanford as a way to track efficiency improvements over time
- More accurately "intelligence per joule" than "intelligence per watt" because time is not the primary concern — total energy for a given task is what matters
- Encompasses the three critical local inference metrics: memory capacity, memory bandwidth, and energy per byte
- Has been improving exponentially: ~5x from hardware improvements over 2 years, ~3x from model improvements, compounding together
- Provides a framework for tracking whether local inference is on a trajectory to become viable for consumers
- EXO Labs plans to use this as one of their benchmark metrics alongside raw tokens-per-second and model quality
- Implies that even if raw performance is lower locally, the total energy efficiency may be competitive with cloud

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source
- [[Hazy Research]] — developed the metric
- [[Memory-Bound vs Compute-Bound]] — the technical context for this metric
- [[Memory Bandwidth]] — one of the three components
- [[EXO Labs]] — plans to benchmark using this metric
