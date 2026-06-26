---
title: "Offline Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Offline evals are evaluations of AI agents run in a controlled, safe environment — effectively rerunning production scenarios without affecting real users. They are the pre-production experimentation counterpart to online evals and form one half of the eval flywheel.

## Key Information

- **Purpose**: Build confidence in agent behavior before and alongside production deployment
- **Process**: Take production examples → run agent against them in safe environment → compare outputs → iterate on agent configuration
- **Relationship to online evals**: Offline evals use examples pulled from production; online evals run against live traffic
- **Scoring**: Can use both automated scoring functions and human evaluation
- **Iteration**: Should be performed continuously throughout the agent's lifetime, not just before initial deployment
- **Analogy**: "Almost like you're rerunning production in a safe environment"

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[OnlineEvals]] — the complementary evaluation mode
- [[EvalFlywheel]] — the loop connecting offline and online evals
- [[EvalMaturityStages]] — all stages involve offline evals
- [[PlaygroundFeature]] — UI for running offline evals
- [[FailureModeAnalysis]] — methodology applied in offline evals
