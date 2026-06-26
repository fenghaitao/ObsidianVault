---
title: "Failure Mode Analysis"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Failure Mode Analysis is the practice of identifying the specific ways an AI agent can fail and building targeted scoring functions around those failure modes. The best way to discover failure modes is through production trace data — observing how real users interact with the agent.

## Key Information

- **Process**: Identify failure modes → build scoring functions → run evals → iterate
- **Discovery**: Production traces are the best source for finding failure modes because they reveal real user behavior, not just synthetic test scenarios
- **Scoring functions**: Automated evaluations built around specific known failure modes
- **Integration with playgrounds**: Playground features allow users to test agent configurations against failure-mode-specific scoring functions
- **Relationship to evals**: The best way to perform evals is to think about failure modes first, then build scoring around them
- **Continuous**: As new failure modes emerge in production, new scoring functions should be added

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalFlywheel]] — the loop that surfaces failure modes from production
- [[PlaygroundFeature]] — where failure mode scoring is applied
- [[EvalMaturityStages]] — Stage 3 enables this methodology
- [[OnlineEvals]] — detecting failure modes in production
- [[OfflineEvals]] — testing against known failure modes
