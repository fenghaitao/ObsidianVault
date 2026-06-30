---
title: "Underspecification in Agentic Tasks"
type: concept
tags: [task-design, benchmarks, agentic-tasks, data-quality, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Underspecification in Agentic Tasks occurs when a benchmark task's definition does not clearly specify the desired testable outcome, but the back-end tests expect certain behaviors or outputs that were never communicated to the model. This mismatch creates apparent difficulty that reflects task design flaws rather than genuine model capability gaps.

## Key Information
- **Primary cause of rejected tasks**: Underspecification is a leading reason tasks fail Snorkel's quality criteria and end up in the rejected bucket
- **Test mismatch pattern**: The task definition is vague or incomplete, but the verification tests expect specific results that were never requested in the task prompt
- **Implicit dependencies**: Tasks may have dependencies that aren't communicated to the model — the model doesn't receive the context needed to know those dependencies exist, making completion impossible
- **Consequence**: Makes tasks appear harder than they genuinely are, but the difficulty comes from poor task design rather than challenging problem-solving requirements
- **Distinction from genuine difficulty**: Unlike tasks that are hard because they require complex reasoning or many steps, underspecified tasks fail because the specification is broken — no model could succeed regardless of capability
- **Benchmark impact**: Underspecified tasks contribute to benchmark noise, creating false signals about model performance and masking genuine improvements

## Related
- [[Task Quality in Agentic Benchmarks]] — the quality framework that identifies underspecification
- [[Task Fidelity Scaling Laws]] — research showing the impact of quality issues like underspecification
- [[Benchmark Noise from Task Quality]] — consequence of underspecified tasks in benchmarks
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[Snorkel]] — company studying this issue
- [[BenchmarkSaturation]] — related concept about benchmarks losing signal
