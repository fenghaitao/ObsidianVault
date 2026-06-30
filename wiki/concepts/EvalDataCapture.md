---
title: "Eval Data Capture"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Eval Data Capture is the practice of gathering production traces or UAT-level traces and incorporating them into evaluation datasets. Rather than constructing synthetic test scenarios, teams capture real agent interactions to build eval datasets that reflect actual user behavior, enabling the mindset of "rerunning production" through evals.

## Key Information

- **Philosophy**: Don't think of evals as running tests — think of evals as rerunning production. The goal is confidence that the agent will perform correctly under real usage conditions.
- **Source**: Production traces (real user interactions) or UAT-level traces (pre-production testing)
- **Purpose**: Build eval datasets that represent real failure modes and user behaviors, not synthetic edge cases
- **Relationship to the flywheel**: Data capture is the input mechanism for the [[EvalFlywheel]] — capture traces → understand failures → bring back to offline environment → rerun via evals → guide improvement
- **Timing**: At Phase 2 of eval practice maturity, teams should be gathering production/UAT traces into their eval datasets, not just using manually created examples
- **Benefits**: Surfaces failure modes that would never be anticipated through synthetic test design; reveals how real users actually interact with the agent

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[EvalFlywheel]] — the continuous loop that data capture feeds
- [[EvalPracticePhases]] — Phase 2 where data capture becomes essential
- [[EvalPrimitives]] — the dataset component of every eval
- [[FailureModeAnalysis]] — production traces are the best source for discovering failure modes
- [[AgentObservability]] — the source of production trace data
