---
title: "TracesAndSpans"
type: concept
tags: [observability, tracing, open-telemetry, agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
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
- Laurie Voss frames traces as logs for AI applications: "just as logs record what your server did at runtime, traces record what your AI did." Every agent call, tool call, LLM invocation, input and output are recorded.
- Spans are nested: a full agent turn is a span containing sub-spans for LLM calls and tool calls. This nested JSON structure captures the full execution tree.
- Each span records input, output, and metadata: timing, token counts, cost, model used.
- Custom spans can wrap multi-turn agent operations to group them as a single trace — essential for multi-step agents where research and writing are separate turns.
- Reading traces is a prerequisite to writing evals: you must see what the agent actually produces (including unexpected behaviors like writing to disk) before defining what to test.
- Traces reveal patterns: systemic failures (prompt problems) vs one-off failures (non-determinism).

## Related
- [[AgentVisualization]] — the visual representation of traces and spans
- [[Arize]] — platform that structures and displays traces and spans
- [[Phoenix]] — open-source tool for trace collection
- [[OpenTelemetry]] — instrumentation standard
- [[OpenInference]] — LLM-specific OTel extension
- [[Cascading Failures]] — diagnosed through trace analysis
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
