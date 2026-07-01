---
title: "OpenTelemetry"
type: entity
tags: [standard, observability, tracing, instrumentation, otel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30
---

## Definition
OpenTelemetry (also called OTel) is an open-source observability standard used by all major observability providers for logging, tracing, and metrics. It provides the foundation for capturing trace data from AI applications, with an LLM-specific extension called OpenInference.

## Key Information
- Used by all major observability providers for logging — Kubernetes logs, application traces, etc.
- Phoenix and Arize build on OpenTelemetry for their instrumentation layer
- The `phoenix.otel` Python package provides the `register()` function that auto-instruments AI frameworks
- Auto-instrumentation works by digging into framework internals where log lines are already plumbed in via the OpenInference standard
- In production, batch span processors are recommended over simple span processors (used in demos)
- Spans are the fundamental unit — each LLM call, tool call, or agent step produces a span
- Supports custom spans: developers can wrap agent logic in OTel spans to group related operations

- Arize is "OTel-first" — add one line of code via auto-instrumentation and it creates traces and spans from any framework/SDK.
- Traces are the "audit record" of what an agent did — code doesn't audit agents, telemetry does.

## Related
- [[OpenInference]] — LLM-specific extension to OpenTelemetry
- [[Phoenix]] — platform built on OpenTelemetry
- [[Arize]] — commercial platform using OpenTelemetry
- [[DatNgo]] — AI Architect who presented Arize's OTel-first approach
- [[TracesAndSpans]] — observability primitives
- [[AgentObservability]] — higher-level concept
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
