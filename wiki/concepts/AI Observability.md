---
title: "AI Observability"
type: concept
tags: [observability, monitoring, opentelemetry, evals, logfire]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
AI Observability is the practice of monitoring, tracing, and evaluating AI agent behavior in production. Samuel Colvin argues it is a feature, not a standalone category — it will eventually be absorbed by either general observability platforms or AI platforms.

## Key Information
- **Colvin's thesis**: AI observability is a feature, not a category. It will be eaten by either observability (e.g., Datadog adding AI features) or AI platforms (e.g., agent frameworks adding monitoring)
- **Logfire's approach**: Built on OpenTelemetry for standard logs, metrics, and traces, then adds AI-specific features: evals, managed variables, and (in development) autonomous optimization
- **Beyond standard observability**: Includes eval comparison views, per-metric performance graphs, case-level drill-down, and A/B testing via managed variables
- **Privacy modes**: Can record categorical performance (good/bad) without exfiltrating raw data — used by legal tech companies like Legora and Harvey
- **Enterprise self-hosting**: Available for VPC deployment to keep sensitive data in-house
- **Instrumentation**: Can instrument Pydantic AI agents, print output, and custom code
- **Scrubbing control**: Can disable automatic PII scrubbing when needed for debugging
- **Gateway observability**: The Pydantic AI Gateway provides visibility into model requests across teams

## Related
- [[Pydantic Logfire]] — the observability platform
- [[OnlineEvals]] — production evaluation enabled by observability
- [[OfflineEvals]] — pre-production evaluation
- [[Managed Variables]] — runtime configuration feature
- [[Agent Optimization]] — optimization enabled by observability data
- [[EvalFlywheel]] — continuous improvement loop
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
