---
title: "Custom Tracing Tools"
type: concept
tags: [tracing, observability, llm, tool-calls, debugging, product-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md"]
last_updated: 2026-06-29
---

## Definition
Custom Tracing Tools are in-house observability systems built by product teams to gain full visibility into LLM agent behavior, including individual tool calls, reasoning steps, search tools, and costs. Unlike generic SaaS tracing platforms, custom tools structure data exactly to the team's needs and serve non-engineer stakeholders (product, data, CX) through purpose-built UIs.

## Key Information
- **Granola's implementation**: Built custom tracing tools with full visibility on tool calls from start to end — why each call was made, search tools, reasoning tools, and costs — structured exactly how they wanted
- **Non-engineer accessibility**: The UI is built for product, data, and CX teams, not just engineers; no need for complex CloudWatch queries
- **Founder-level usage**: Granola's founder follows agent loops completely front-to-back in the tracing UI to diagnose what went wrong
- **LLMs enabled this**: Previously, building custom tracing tools required a SaaS provider and too much time; now teams can one-shot custom tools with LLMs
- **Data ownership**: Custom tools give complete control over data structure, storage, and presentation — not dependent on provider changes or limitations
- **OpenTelemetry option**: Can be built on OpenTelemetry or custom wrappers around AI SDKs, with data saved to a DB and a front-end as the critical component
- **Debugging workflow**: From "this output feels off" → trace through the tool calls → identify exactly what failed → iterate and improve
- **Beyond black-box LLMs**: Tracing tools are the key to understanding LLM behavior, which is otherwise a black box

## Related
- [[Granola]] — company that built custom tracing tools
- [[Product Feedback Loops]] — the observability half of Granola's feedback loop
- [[AI Observability]] — broader category of AI monitoring
- [[AgentObservability]] — related concept in agent systems
- [[Mehedi Hassan]] — speaker who described this approach
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — source transcript
