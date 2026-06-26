---
title: "Headless Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

Headless Evals refers to programmatic interaction with eval platforms via coding agents rather than through a human-facing UI. In this pattern, a coding agent (like Claude Code or Codex) queries the eval platform's data backend, pulls evaluation results into context, and modifies the agent under test — all without a human manually using the eval UI.

## Key Information

- **Pattern**: Coding agent queries eval platform → pulls aggregate data into context → modifies target agent → loop
- **Self-healing**: Enables agents to improve themselves based on eval results
- **Data backend requirement**: Requires a robust data layer that supports SQL and programmatic access, not just a UI
- **Growing trend**: Braintrust has observed increasing demand for headless use cases where users don't care about the UI at all
- **Platform design implication**: Eval platforms must be built for both humans and agents as consumers

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[EvalPlatforms]] — the platform context
- [[EvalFlywheel]] — the loop headless evals automate
- [[AgentQualityPlatform]] — platform category supporting this pattern
- [[TraceDataChallenges]] — the data infrastructure needed for programmatic access
