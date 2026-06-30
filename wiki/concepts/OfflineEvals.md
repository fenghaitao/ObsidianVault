---
title: "Offline Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
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
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (GEPA optimization uses offline evals against golden dataset)
- [[OnlineEvals]] — the complementary evaluation mode
- [[EvalFlywheel]] — the loop connecting offline and online evals
- [[EvalMaturityStages]] — all stages involve offline evals
- [[PlaygroundFeature]] — UI for running offline evals
- [[Golden Dataset]] — ground truth for offline evals
- [[Agent Optimization]] — optimization driven by offline eval results
- [[FailureModeAnalysis]] — methodology applied in offline evals
