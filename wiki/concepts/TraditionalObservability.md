---
title: "Traditional Observability"
type: concept
category: methodology
tags: [observability, monitoring, metrics, traces, spans, uptime]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Traditional observability is the established practice of monitoring software applications for uptime and technical performance — measuring whether the application is operational and delivering the expected user experience from a technical lens. It uses metrics, traces, and spans to track latency, error rates, and interaction duration. Tools include Datadog and Grafana. Traditional observability is complementary to, but fundamentally different in scope from, agent observability.

## Key Information

- **Scope**: Uptime and technical performance — is the application up? Is it giving the expected technical user experience?
- **Key metrics**: Latency, duration of interactions, 400 and 500 level errors, error count
- **Building blocks**: Metrics (aggregatable measurements), traces (full interaction workflows), spans (individual steps within a trace)
- **Tools**: Datadog, Grafana — well-established, operate at scale, mature ecosystem
- **Persona**: Systems engineers, product engineers — strictly technical people
- **Data characteristics**: Structured, compact (KB-scale spans), deterministic
- **Limitations for agents**: Cannot measure qualitative aspects (groundedness, tool usage correctness, brand alignment), cannot handle gigabyte-scale semi-structured traces, cannot perform full-text search across unstructured trace text, does not support non-technical domain expert workflows
- Braintrust itself is a happy Datadog user for traditional website uptime monitoring, demonstrating that traditional and agent observability are complementary, not competing

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[AgentObservability]] — the complementary, broader paradigm for AI agents
- [[Datadog]] — commercial traditional observability tool
- [[Grafana]] — open-source traditional observability tool
- [[TracesAndSpans]] — shared building blocks with agent observability
- [[NonDeterministicAgents]] — why agents require broader observability
- [[AgentTraceData]] — the fundamentally different data type agents produce
