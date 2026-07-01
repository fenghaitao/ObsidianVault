---
title: "Self-Curating Test Suites"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Self-curating test suites are evaluation datasets that agents automatically generate and maintain from production traces, rather than being manually created and frozen in time. As user behavior, query patterns, and agent capabilities change, the test suite evolves to stay representative of actual usage.

## Key Information

- **Generation mechanism**: Agents analyze production traces to identify representative patterns and edge cases, automatically building and updating test suites
- **Responds to demographic shifts**: When a customer base changes — leading to different question styles, new use cases, or shifted expectations — the test suite adapts rather than remaining calibrated to the old user population
- **80% rule application**: The 80% of behavior that is stable can be covered by static intent-defined evaluations, but the 20% that changes is where self-curating suites provide value — detecting and incorporating new patterns
- **Human notification**: Changes detected by the agent are communicated to owners, who can validate or reject test suite modifications
- **Contrast with manual curation**: Traditional eval suites require humans to notice changing patterns, design new test cases, and update the suite — a slow process that cannot keep pace with agent evolution

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — proposed the concept
- [[Malleable Evals]] — broader framework
- [[Adaptive Testing For LLMs]] — related methodology
- [[Static Benchmarks]] — the approach being superseded
- [[Eval Calcification]] — the problem self-curating suites prevent
- [[OnlineEvals]] — data source for suite generation
