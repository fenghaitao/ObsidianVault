---
title: "NonDeterministicTesting"
type: concept
tags: [testing, evals, llm, non-deterministic, context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Non-Deterministic Testing is the practice of testing LLM-based systems (including context evals) by running tests multiple times and measuring success rates rather than expecting deterministic pass/fail results. It acknowledges that LLM outputs vary between runs and that traditional CI/CD pass/fail gating is insufficient.

## Key Information
- Introduced by Patrick Debois in the context of the CDLC Test phase
- Core problem: if you run an eval once, it might pass; run it again, it might fail — you cannot debug a single run
- Solution: run tests 5 times and measure how many times they succeed
- Some tests may hit 100% consistently (great), others may not
- Uses error budgets: critical tests are allowed minimal failures, less critical tests have more tolerance
- Represents a fundamental shift from deterministic software testing to statistical quality measurement
- Applies to context evals, LLM-as-judge evaluations, and any system with LLM-generated outputs

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextTesting]] — the testing practice this applies to
- [[ErrorBudgetsForContext]] — the CI/CD mechanism for managing non-determinism
- [[LLMAsJudge]] — evaluation method subject to non-determinism
- [[EvalEngineering]] — practice of crafting evals that work with non-determinism
