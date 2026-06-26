---
title: "Eval Maturity Stages"
type: concept
category: framework
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Eval Maturity Stages is a four-stage framework describing how organizations progress in building LLM/agent evaluation platforms, from simple spreadsheets to fully integrated observability-evals systems.

## Key Information

### Stage 1: Spreadsheet + For Loop
- Iterate through input examples, execute agent, record outputs in a spreadsheet
- Zero barrier to entry; great starting point
- Limitations: more documentation than experimentation, hard to compare experiments over time, human scoring doesn't scale, non-technical users won't engage, slow

### Stage 2: Vibe-Coded UI
- Bespoke UI with a proper database (e.g., Neon/Postgres) for persistence
- More approachable for non-technical users
- Limitations: still primarily a reporting/documentation tool, not encouraging rapid iteration

### Stage 3: Experimentation Platform
- Playground features for both technical and non-technical users
- Users can tweak agent parameters (system prompts, configurations) and compare results side-by-side
- Automated scoring functions built around known failure modes
- Failure modes discovered through production trace data
- SDK-driven experience alongside UI

### Stage 4: Observability-Integrated Platform
- Connects production observability with offline evals to form a flywheel
- Production traces reveal real user behavior → examples feed back into offline evals → agent improves → redeploy
- Requires solving hard data problems: high-velocity ingestion, low-latency viewing, aggregate analytics, full-text search
- Supports online evals (scoring functions on live traffic) and alerting
- Must manage the platform at the pace of industry evolution

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalPlatforms]] — the platform these stages describe
- [[EvalFlywheel]] — the loop enabled at Stage 4
- [[PlaygroundFeature]] — key capability at Stage 3
- [[FailureModeAnalysis]] — methodology enabled at Stage 3
- [[OnlineEvals]] — capability at Stage 4
- [[OfflineEvals]] — capability across stages
