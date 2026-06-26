---
title: "Arize"
type: entity
tags: [company, ai, observability, eval, platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Arize is an AI observability and evaluation platform that helps teams monitor, debug, and improve their LLM-powered applications and agents. It provides a unified platform for observability, evaluation, and development workflows.

## Key Information
- Provides tools for LLM evaluation, including LLM-as-judge capabilities that generate English-language explanations of model failures.
- Aparna Dhinakaran from Arize demonstrated prompt learning techniques using Arize's evaluation infrastructure to improve coding agent performance on SWE-bench.
- SallyAnn DeLucia (Director of RISE) and Fuad Ali (Product Manager) presented a hands-on workshop on building prompt optimization loops using Arize's prompt learning SDK.
- Aman Khan (AI PM) demonstrated the full eval workflow: traces/spans, prompt playground, dataset creation, experiment running, LLM-as-judge evals, and human-in-the-loop validation.
- Features include: agent visualization (graph-based representation of agent systems), prompt playground (iterate on prompts with production data), prompt hub (version control for prompts), eval runner (fast LLM-as-judge execution), labeling queue (human annotation), and a co-pilot for writing eval prompts.
- Built on OpenTelemetry (OTel) standard with auto-instrumentation for agent frameworks like LangGraph.
- Customers include Uber, Instacart, Reddit, Duolingo, Spotify, and Booking.com.
- Series C company with investment from Datadog and Microsoft.
- Open-source version called Phoenix provides core observability and eval workflows.
- The company publishes content on eval prompt optimization and is actively hiring.

## Related
- [[AparnaDhinakaran]] — speaker from Arize
- [[SallyAnnDeLucia]] — Director of RISE at Arize
- [[FuadAli]] — Product Manager at Arize
- [[AmanKhan]] — AI PM at Arize
- [[BookingCom]] — Arize client
- [[Phoenix]] — open-source version of Arize
- [[LLM-as-Judge]] — core evaluation technique used by the platform
- [[EvalEngineering]] — practice the company advocates for
- [[PromptLearning]] — technique the platform supports
- [[CoEvolvingLoops]] — optimization philosophy promoted by Arize
- [[AgentVisualization]] — feature shipped by Arize
- [[PromptPlayground]] — feature in the Arize platform
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
