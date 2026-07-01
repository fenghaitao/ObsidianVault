---
title: "Adaptive Testing For LLMs"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Adaptive testing for LLMs is an evaluation approach where test suites change and evolve alongside the AI applications they assess, rather than remaining static. Instead of fixed question-and-answer pairs, adaptive tests selectively target areas of change, incorporate new patterns from production, and adjust based on shifting user behavior and agent capabilities.

## Key Information

- **Core question**: "Why are static benchmarks static?" — if agent applications are constantly changing, why don't test suites change with them?
- **Academic precedent**: Referenced an existing paper on adaptive testing for LLM evals that proposes tests that evolve with applications
- **Selective testing**: Rather than running full suites, adaptive testing focuses on areas where change is detected — more efficient and more relevant
- **Contrast with static benchmarks**: Static benchmarks test the same questions regardless of whether the agent or its environment has changed. Adaptive tests respond to change signals.
- **Implementation pathway**: Production traces reveal changing patterns → test suites update to incorporate new scenarios → evaluation stays aligned with reality

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[Malleable Evals]] — broader framework encompassing adaptive testing
- [[SelfCurating Test Suites]] — specific mechanism for adaptive test generation
- [[Static Benchmarks]] — the approach being superseded
- [[Eval Calcification]] — the problem adaptive testing prevents
