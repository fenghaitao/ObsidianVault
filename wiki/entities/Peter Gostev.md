---
title: "Peter Gostev"
type: entity
tags: [person, ai, benchmark, arena, model-evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
Peter Gostev is a researcher at Arena.ai who created BullshitBench, a benchmark that tests whether AI models push back against nonsense questions rather than going along with them. He presented at the AI Engineering conference on what models still struggle with, combining BullshitBench results with Arena.ai's dissatisfaction rate data.

## Key Information
- Works at **Arena.ai**, which tracks over 700 text models and has collected 5.5M+ human preference votes since Q2 2023
- Created **BullshitBench**: 155 nonsense questions used to test whether models push back or comply
- Found that Claude/Sonnet models perform best at nonsense detection, while GPT and Gemini models go along with nonsense ~50% of the time
- Discovered that reasoning/thinking often makes bullshit detection worse, not better — models question the premise then spend paragraphs trying to solve anyway
- Hypothesis: models are trained to solve tasks at any cost, not trained to say "maybe don't solve this"
- Presented Arena's dissatisfaction rate data: users can vote "both models bad" — currently ~9% for top models
- Showed that dissatisfaction rate improvements are uneven across categories: math improved dramatically, but medical/finance/law and gaming have barely improved
- Argues the gap between "line goes up" benchmarks and real user experience comes from benchmarks measuring narrow, well-specified tasks that don't capture the full dimensions of real work
- Calls for improving the bottom of the distribution, not just the frontier

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[ArenaAi]] — platform he works at
- [[BullshitBench]] — benchmark he created
- [[Model Dissatisfaction Rate]] — Arena metric he presented
- [[Anthropic]] — best BullshitBench performer
- [[OpenAI]] — GPT models ~50/50 on BullshitBench
- [[GoogleDeepMind]] — Gemini models ~50/50 on BullshitBench
- [[Qwen]] — decent BullshitBench performer
- [[Reasoning Limits]] — his finding that reasoning can worsen nonsense detection
- [[Nonsense Detection]] — core capability BullshitBench measures
- [[BenchmarkSaturation]] — context for his critique of standard benchmarks
- [[ModelBehavior]] — his observation about solve-at-any-cost training
