---
title: "TimeHorizon"
type: concept
tags: [benchmark, ai-capabilities, metr, evaluation, metric]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
Time Horizon is METR's metric for AI autonomous capabilities, defined as the human-time-to-complete a task at which an AI model is predicted to succeed 50% of the time on a given task distribution.

## Key Information
- Derived by gathering human baseline data for diverse tasks (HCAST, SWAR, RE-Bench), measuring AI performance under identical conditions, and fitting a curve of success probability vs. human completion time
- Models show a robust empirical pattern: less performant at tasks that take humans longer
- Claude 3 Opus had a time horizon of ~4 minutes; o1-preview ~15 minutes; GPT 5.1 CEX max extends much further
- Plotted against calendar time, time horizon follows a remarkably steady exponential trend, doubling every ~6-7 months
- The 50% threshold is debated but chosen as a consistent reference point
- Provides a way to "chain benchmarks together" over time as individual benchmarks saturate
- Even time horizon may eventually saturate as models improve, requiring ever harder tasks
- METR is exploring monitored vs. unmonitored capabilities as a way to extend time horizon's useful range: safety monitoring may reduce effective time horizon by 1-2 orders of magnitude
- Considerations like "building on prior work" and mergeability may reduce effective time horizon compared to raw benchmark scores
- As time horizons double, tasks eventually exceed the maximum possible task length — METR is working on ways around this

## Related
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[METR]] — organization that developed this metric
- [[JoelBecker]] — co-author of the time horizon paper
- [[BenchmarkSaturation]] — problem time horizon partially addresses
- [[HCAST]] — task distribution used in measurement
- [[SWAR]] — task distribution used in measurement
- [[RE-Bench]] — task distribution used in measurement
- [[ComputeCapabilityProportionality]] — framework linking time horizon to compute growth
- [[MonitoredVsUnmonitoredCapabilities]] — approach to extend time horizon's useful range
- [[CapabilityExtrapolation]] — broader framework time horizon fits into
