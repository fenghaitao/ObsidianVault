---
title: "TracesAndSpans"
type: concept
tags: [observability, tracing, open-telemetry, agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Traces and Spans are observability primitives for AI agent systems. A trace represents the full input, output, and metadata of a request. A span is a unit of work within a trace, with timing information and a type (agent, tool, or LLM call).

## Key Information
- Traces consist of multiple spans, each representing a discrete operation in the agent pipeline.
- Span types include: agent (orchestration), tool (structured data actions), and LLM (generation from input and context).
- Each span has a time component showing how long the process took.
- Built on OpenTelemetry (OTel) standard, making instrumentation portable across platforms.
- Arize/Phoenix enriches standard traces with additional metadata (user ID, session ID, human/AI interaction context) for better visualization.
- Enables aggregate analysis: seeing which calls agents make, how they parallelize, and where bottlenecks occur.

## Related
- [[AgentVisualization]] — the visual representation of traces and spans
- [[Arize]] — platform that structures and displays traces and spans
- [[Phoenix]] — open-source tool for trace collection
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
