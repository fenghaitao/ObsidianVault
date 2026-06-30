---
title: "OpenInference"
type: entity
tags: [standard, observability, instrumentation, llm, otel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
OpenInference is an open-source extension to OpenTelemetry that adds LLM-specific instrumentation capabilities. It captures prompt text, completion text, token counts, model names, tool invocations, and other AI-specific metadata that standard OpenTelemetry doesn't handle.

## Key Information
- Built on top of OpenTelemetry (OTel) as an extension layer
- Adds LLM-specific attributes: prompt text, completion text, token counts, which model was called, what tools were invoked
- All major AI frameworks (Claude, OpenAI, Gemini, LangChain, CrewAI, LlamaIndex) have OpenInference instrumentation packages
- Arize/Phoenix provides integration packages (`openinference-instrumentation-claude-agent-sdk`) that auto-instrument frameworks
- The standard is adopted by framework builders — developers don't need to manually plumb log lines
- Two lines of code (`import phoenix.otel` + `register()`) enable full auto-instrumentation

## Related
- [[OpenTelemetry]] — parent standard
- [[Phoenix]] — platform using OpenInference
- [[Arize]] — commercial platform using OpenInference
- [[TracesAndSpans]] — the data captured via OpenInference
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
