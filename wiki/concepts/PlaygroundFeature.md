---
title: "Playground Feature"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

A Playground Feature is a UI capability in eval platforms that allows both technical and non-technical users to tweak agent parameters (such as system instructions) in a sandbox environment and compare different configurations side-by-side with automated scoring. It represents Stage 3 in the eval maturity model.

## Key Information

- **Purpose**: Enable experimentation, not just documentation/reporting
- **Audience**: Both technical users (via SDK) and non-technical users (via UI)
- **Capabilities**: Give users access to an agent configuration in a sandbox; allow tweaking parameters (system prompts, model settings); run evals across different configurations; bubble up scores for comparison
- **Example**: Changing system instructions for an agent and comparing two configurations with automated scoring
- **Significance**: This is where "the rubber meets the road" — the best evals come from understanding failure modes and building scoring functions around them
- **Common across platforms**: Many eval platforms include a playground feature

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalMaturityStages]] — Stage 3 where playgrounds emerge
- [[EvalPlatforms]] — the platform context
- [[FailureModeAnalysis]] — methodology enabled by playgrounds
- [[OfflineEvals]] — the type of evals run in playgrounds
