---
title: "Topic Modeling for Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Topic Modeling for Evals is the application of topic modeling techniques to agent trace data to uncover "unknown unknowns" — usage patterns, failure modes, and user behaviors that the engineering team wasn't aware of. It helps teams know where to spend their engineering time without manually reviewing thousands of traces.

## Key Information

- **Purpose**: Surface unknown unknowns in agent usage — don't make engineers look across thousands of traces manually
- **Output**: Identifies clusters of user interactions, common failure patterns, and emerging use cases
- **Value**: Directs engineering effort to the highest-impact areas
- **Future direction**: Phil Hetzel identified this as a key capability that eval platforms should build toward
- **Relationship to flywheel**: Complements the observability-evals loop by adding automated discovery of patterns

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalFlywheel]] — the loop this technique enhances
- [[FailureModeAnalysis]] — discovering failure modes through topic modeling
- [[AgentObservability]] — the data source for topic modeling
- [[TraceDataChallenges]] — the data infrastructure needed to support this
