---
title: "Eval Calcification"
type: concept
category: problem
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Eval calcification is the progressive hardening and increasing brittleness of AI evaluations over time when they are not updated adaptively. As agent behavior, user bases, and query patterns change, static benchmarks become progressively less representative — calcifying into measurements that no longer reflect reality.

## Key Information

- **Origin**: Term coined by [[VincentKoc]] during his talk on malleable evals
- **Mechanism**: Static benchmarks are created at a point in time. As the agent, its users, and its environment evolve, the benchmark remains frozen — widening the gap between what is measured and what actually happens
- **Consequence**: Organizations invest in optimizing for benchmarks that are increasingly disconnected from production behavior, creating a false sense of security
- **Solution**: Adaptive evaluation — self-curating test suites from traces, online always-on evaluation, and telemetry-in-the-loop approaches that keep evaluations aligned with reality
- **Relationship to the 80/20 rule**: The 20% of behavior that constantly changes is where calcification hits hardest, and where businesses break

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator of the term
- [[Malleable Evals]] — the solution to eval calcification
- [[Static Benchmarks]] — the source of calcification
- [[SelfCurating Test Suites]] — mechanism for preventing calcification
- [[EvalFlywheel]] — continuous evaluation loop that prevents calcification
