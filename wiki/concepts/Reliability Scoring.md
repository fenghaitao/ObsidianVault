---
title: "Reliability Scoring"
type: concept
tags: [eval, reliability, pass-at-k, non-determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Reliability scoring measures how consistently an AI agent succeeds across multiple attempts, using two complementary metrics: Pass@K (succeeds at least once in K tries) and Pass^K (succeeds every time in K tries). These metrics diverge dramatically as K increases.

## Key Information
- **Pass@K**: Can the agent succeed at least once in K tries? Approaches 100% as K increases. Good for use cases where eventual success matters — e.g., coding assistants where you can retry until it works
- **Pass^K**: Can the agent succeed every single time in K tries? Approaches 0% as K increases. Good for use cases where every interaction must succeed — e.g., customer support bots where one failure in five is unacceptable
- As K increases, these two measures diverge: Pass@K → 100%, Pass^K → 0%
- Which metric to use depends on the use case: coding assistant → Pass@K (can retry), customer support → Pass^K (must work every time)
- Addresses the fundamental non-determinism problem: the same prompt produces different outputs on every run
- Experiments should run each example multiple times to account for non-determinism
- Sample size math: 200 samples at 3% defect rate gives 95% confidence interval of 0.6%-5.4%; 400 samples narrows to 1.3%-4.7%

## Related
- [[Pairwise Evaluation]] — complementary advanced technique
- [[AgentExperiments]] — experimental framework using reliability scoring
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
