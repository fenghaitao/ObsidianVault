---
title: "Eval Flywheel"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

The Eval Flywheel is the continuous loop connecting production observability with offline experimentation for AI agents. Observability and evals are treated as the same problem from a systems perspective — production traces reveal real user behavior and failure modes, which feed back into offline evals for continuous agent improvement.

## Key Information

- **The loop**: Observe agents in production → analyze real user interactions → pull examples back into offline environment → improve agent via offline evals → redeploy → repeat
- **Origin**: Braintrust started as an evals-only platform, then noticed a customer piping all production traffic into evals every hour. This revealed that observability and evals are fundamentally the same data problem.
- **Continuous**: The loop should run for the lifetime of the agent, not as a one-time process
- **Signal quality**: Production traces provide far higher signal about real user behavior than synthetic test cases
- **Offline evals as safe replay**: Effectively rerunning production scenarios in a controlled environment
- **Online evals**: Pointing scoring functions at live observability traffic for alerting and monitoring

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company that coined the term
- [[AgentObservability]] — the observability half of the flywheel
- [[OnlineEvals]] — scoring on live traffic
- [[OfflineEvals]] — scoring in controlled environment
- [[EvalMaturityStages]] — Stage 4 enables this flywheel
- [[FailureModeAnalysis]] — key methodology powered by the flywheel
