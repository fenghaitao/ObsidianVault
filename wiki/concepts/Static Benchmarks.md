---
title: "Static Benchmarks"
type: concept
category: problem
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Static benchmarks are fixed evaluation datasets used to measure AI model or agent performance at a single point in time. They consist of predetermined questions, tasks, or scenarios with expected answers or outcomes, and they do not evolve as the systems they evaluate change.

## Key Information

- **Dominance in AI**: Academic AI conferences are heavily focused on benchmark creation — "I created a benchmark for adding numbers and what LLMs think about it" — often disconnected from practical utility
- **Core limitation**: AI applications are not static, but static benchmarks treat them as if they were. When agent harnesses self-modify (e.g., [[OpenClaw]] creating skills and adapting behavior), static benchmarks cannot keep pace.
- **Failure mode**: Organizations build enormous datasets to approximate agent behavior, but these only work until something goes wrong — and something always goes wrong
- **The gap**: Software engineering evolved through unit tests → regression suites → CI/CD → chaos engineering. AI evaluation has largely stopped at the static benchmark stage, missing the chaos engineering equivalent.
- **Contrast with adaptive approaches**: [[Malleable Evals]], [[Adaptive Testing For LLMs]], and [[SelfCurating Test Suites]] represent the evolution beyond static benchmarks

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — critique of static benchmarks
- [[Malleable Evals]] — the proposed alternative
- [[Eval Calcification]] — the long-term consequence of relying on static benchmarks
- [[Adaptive Testing For LLMs]] — methodology for evolving beyond static benchmarks
- [[SelfCurating Test Suites]] — mechanism for generating dynamic benchmarks
- [[IntentBased Outcomes]] — evaluation philosophy that replaces static answer comparison
- [[OnlineEvals]] — continuous evaluation that supplements static benchmarks
