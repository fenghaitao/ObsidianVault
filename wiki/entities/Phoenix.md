---
title: "Phoenix"
type: entity
tags: [tool, open-source, observability, eval, arize]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26

## Definition
Phoenix is the open-source version of Arize, providing AI observability and evaluation capabilities. It shares many of the same setup flows and workflows as the commercial Arize platform but without scale, security, and support features.

## Key Information
- Open-source alternative to the commercial Arize platform.
- Built on OpenTelemetry (OTel) tracing standards.
- Uses the `arize-phoenix` and `arize-otel` Python packages for instrumentation.
- Supports auto-instrumentation for agent frameworks like LangGraph with a single line of code.
- Does not include all Arize features but provides core observability and eval workflows.
- Used by Kevin Madura in his DSPy workshop for observability and tracing of DSPy LLM calls.

## Related
- [[Arize]] — commercial version of Phoenix
- [[DSPy]] — framework Phoenix was used to observe
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
