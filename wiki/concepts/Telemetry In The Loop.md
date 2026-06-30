---
title: "Telemetry In The Loop"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition

Telemetry in the loop is an evaluation and self-healing approach where agent harnesses consume their own observability data — errors, costs, performance metrics — to self-correct without human intervention. The agent becomes aware of what is breaking and autonomously adjusts its behavior.

## Key Information

- **Self-correction mechanism**: When the agent harness has access to telemetry about errors, issues, and costs, it can fix itself and continue operating — rather than requiring human diagnosis and intervention
- **Condition-based adaptation**: Operators can set conditions around telemetry signals (e.g., cost thresholds, error rates), and the agent self-corrects when those conditions are triggered
- **Paper reference**: Vincent Koc has written on this concept, proposing that agentic systems should be aware of their own telemetry for self-correction
- **Relationship to malleable evals**: One of the four pillars — instead of predicting what will go wrong, use telemetry data to enable the agent to heal itself
- **Implementation**: Requires observability integration with the agent harness, condition definitions, and feedback mechanisms that route telemetry signals back into agent decision-making

## Related

- [[summary-20260512 - Malleable Evals： Why Are We Evaluating Adaptive Systems with Static Tests — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — author of the concept paper
- [[Malleable Evals]] — broader framework incorporating telemetry in the loop
- [[AgentObservability]] — prerequisite data source
- [[OnlineEvals]] — scoring functions that can feed telemetry signals
- [[EvalFlywheel]] — continuous loop telemetry enables
