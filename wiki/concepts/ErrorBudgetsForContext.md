---
title: "ErrorBudgetsForContext"
type: concept
tags: [context, testing, ci-cd, error-budget, non-deterministic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Error Budgets for Context is the practice of assigning acceptable failure rates to context tests in CI/CD, acknowledging that LLM-based evaluations are non-deterministic and cannot be gated on exact pass/fail. Critical tests get tight budgets (near-zero allowed failures), while less critical tests get looser budgets.

## Key Information
- Introduced by Patrick Debois as part of the CDLC Test phase
- Addresses the problem that running an eval once and gating on pass/fail is unreliable due to LLM non-determinism
- Instead: run tests N times, measure success rate, compare against the error budget
- Critical tests (e.g., security rules, compliance requirements) get tight error budgets
- Less critical tests (e.g., style preferences) get looser budgets
- Analogous to SRE error budgets but applied to context quality rather than service reliability
- Enables CI/CD for context: you can run context tests in pipelines with meaningful gating

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[NonDeterministicTesting]] — the testing approach error budgets enable
- [[ContextTesting]] — the broader testing practice
- [[ContextDevelopmentLifeCycle]] — the lifecycle phase this supports
