---
title: "Online Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition

Online evals are scoring functions pointed at live observability/production traffic to evaluate agent performance in real time. They enable alerting, monitoring, and continuous quality assessment without taking the agent offline.

## Key Information

- **Contrast with offline evals**: Online evals run against live production data; offline evals run in a controlled, safe environment
- **Use cases**: Alerting when agent quality degrades, monitoring trends, detecting new failure modes
- **Enabled at Stage 4**: Online evals become possible when the eval platform is integrated with production observability
- **Part of the flywheel**: Online evals detect issues → examples feed into offline evals → agent improves → redeploy
- **Scoring functions**: The same scoring functions used in offline evals can be pointed at production traffic

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (managed variables enable online eval A/B testing)
- [[OfflineEvals]] — the complementary evaluation mode
- [[EvalFlywheel]] — the loop connecting online and offline evals
- [[EvalMaturityStages]] — Stage 4 enables online evals
- [[AgentObservability]] — the data source for online evals
- [[Managed Variables]] — Logfire feature for production experimentation
- [[FailureModeAnalysis]] — detecting failure modes via online evals
