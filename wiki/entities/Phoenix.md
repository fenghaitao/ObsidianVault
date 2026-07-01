---
title: "Phoenix"
type: entity
tags: [tool, open-source, observability, eval, arize]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-30

## Definition
Phoenix is the open-source version of Arize, providing AI observability and evaluation capabilities. It shares many of the same setup flows and workflows as the commercial Arize platform but without scale, security, and support features.

## Key Information
- Open-source alternative to the commercial Arize platform.
- Built on OpenTelemetry (OTel) tracing standards.
- Uses the `arize-phoenix` and `arize-otel` Python packages for instrumentation.
- Supports auto-instrumentation for agent frameworks like LangGraph with a single line of code.
- Does not include all Arize features but provides core observability and eval workflows.
- Used by Kevin Madura in his DSPy workshop for observability and tracing of DSPy LLM calls.
- Laurie Voss used Phoenix Cloud in his agent evaluation workshop — the zero-install cloud version avoids local setup.
- Phoenix Cloud endpoint: `app.phoenix/s/<username>`. Requires a Phoenix API key (separate from Arize AX).
- Provides built-in LLM evals: correctness, faithfulness, tool selection, tool invocation, document relevance, refusal detection.
- Supports custom LLM-as-judge evals via the `classification_evaluator` helper.
- Experiments feature: create datasets from failing traces, run tasks against datasets, compare scores to measure prompt improvements.
- Key APIs: `phoenix.otel.register()` for auto-instrumentation, `evaluate_dataframe()` for running evals, `log_span_annotations_dataframe()` for storing results.
- Phoenix Cloud is distinct from Arize AX — signing up on the Arize homepage defaults to AX, not Phoenix.
- Single-container deployment, no Kubernetes required — can deploy locally.
- The open-source version for "engineering-first folks" while AX serves the largest enterprises.

## Related
- [[Arize]] — commercial version of Phoenix
- [[ArizeAX]] — enterprise version with additional features
- [[DatNgo]] — AI Architect who presented Phoenix alongside AX
- [[DSPy]] — framework Phoenix was used to observe
- [[LaurieVoss]] — delivered workshop using Phoenix
- [[ClaudeAgentSDK]] — agent framework used in Phoenix workshop
- [[OpenTelemetry]] — instrumentation standard
- [[OpenInference]] — LLM-specific OTel extension
- [[LLMAsJudge]] — evaluation technique supported by Phoenix
- [[Code Evals]] — deterministic evaluation type
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
