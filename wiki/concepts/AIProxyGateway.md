---
title: "AI Proxy Gateway"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-26
---

## Definition

An AI Proxy Gateway is an architectural pattern where all LLM calls are routed through a proxy that automatically adds tracing and instrumentation. This ensures that teams cannot avoid instrumenting their LLMs — governance is applied centrally rather than relying on individual developers to add tracing.

## Key Information

- **Purpose**: Automatic, non-optional tracing of all LLM calls in an organization
- **Governance**: Centralized control over LLM observability rather than opt-in per developer
- **Integration**: Works with eval platforms to feed all LLM traffic into observability and evals
- **Future direction**: Phil Hetzel identified this as a consideration for mature eval platforms
- **Benefit**: Eliminates the gap where some LLM calls go unmonitored because developers didn't add tracing

## Related

- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source
- [[AgentObservability]] — the observability enabled by proxy tracing
- [[EvalFlywheel]] — the loop fed by proxy-captured traces
- [[EvalPlatforms]] — the platform context
- [[TraceDataChallenges]] — the data infrastructure needed to handle proxy-captured traffic
