---
title: "Two Camps of Wrong on Evals"
type: concept
tags: [evals, philosophy, methodology, benchmarks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Two Camps of Wrong on Evals is a framework describing the two fundamental ways people misunderstand and misuse AI evaluations: the Objective Metrics Camp (treating benchmark numbers as definitive truth) and the Taste/Vibes Camp (dismissing all quantitative measurement in favor of subjective feel). The correct approach lies in the middle.

## Key Information

### Camp 1: The Objective Metrics Camp
- Treats benchmark dashboards as definitive, objective truth
- Interprets similar scores across models as evidence the models are effectively the same
- Prone to [[Benchmark Maxing]] — optimizing for the benchmark rather than real-world performance
- Vulnerable to [[BenchmarkSaturation]] — believing a saturated benchmark still provides meaningful signal
- Critiques model provider numbers as "a hoax" when they don't align with lived experience

### Camp 2: The Taste/Vibes Camp
- Dismisses all quantitative evaluation as useless
- Relies purely on subjective feel and personal preference
- Anthropomorphizes models ("I like talking to her")
- Rejects systematic measurement entirely
- Cannot make data-driven decisions about agent improvements

### The Middle Ground
- Evals are neither the end-all-be-all nor completely useless
- There are right ways and wrong ways to use them
- Effective eval usage requires both heuristics for interpretation and disciplined processes like [[Hill Climbing (Evals)]]
- Must pass both the quantitative score check AND the qualitative vibe check
- The philosophy problem: you cannot exactly approximate the search space of where problems could fail, but you can build evals that are useful approximate representations

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[Eval Heuristics]] — practical heuristics derived from this framework
- [[Hill Climbing (Evals)]] — the methodology that sits in the middle ground
- [[Benchmark Maxing]] — the danger of the Objective Metrics Camp
- [[BenchmarkSaturation]] — why objective metrics lose signal over time
- [[Three Zones of Improvement]] — framework for disciplined improvement
- [[AgenticEvaluations]] — the type of evals this framework applies to
