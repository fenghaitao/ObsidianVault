---
title: "Malleable Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Malleable evals are evaluations designed to adapt alongside self-optimizing AI agents, rather than remaining as fixed, static benchmarks. The core premise is that as AI systems become capable of self-modification (changing their own harness, creating skills, adapting behavior), evaluations must evolve from point-in-time measurements into living, self-adjusting assessment systems.

## Key Information

- **Contrast with static benchmarks**: Traditional evals are fixed datasets that do not adapt when the agent or its user base changes. Malleable evals evolve continuously based on production behavior.
- **Four pillars**: Intent-based outcomes, self-curating test suites from traces, online always-on evaluation, and telemetry in the loop
- **80/20 principle**: 80% of behavior is stable and can use static evaluation; the 20% that changes is what breaks businesses and requires adaptive monitoring
- **End-state orientation**: Malleable evals define what success looks like (the goal), then let the agent self-correct toward it — the eval becomes the destination, not the dataset
- **Origins**: Proposed by [[VincentKoc]] as a response to the disconnect between self-adapting agent harnesses like [[OpenClaw]] and the static benchmarks used to evaluate them

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator of the concept
- [[Intent Engineering]] — the paradigm shift enabling malleable evals
- [[Eval Calcification]] — the problem malleable evals address
- [[Self-Curating Test Suites]] — one pillar of malleable evals
- [[Telemetry In The Loop]] — one pillar of malleable evals
- [[Intent-Based Outcomes]] — one pillar of malleable evals
- [[OnlineEvals]] — related concept of scoring against live production traffic
- [[EvalFlywheel]] — the continuous loop connecting production and evaluation
- [[Static Benchmarks]] — the traditional approach being superseded
- [[Chaos Engineering For AI]] — methodology for discovering system limits
