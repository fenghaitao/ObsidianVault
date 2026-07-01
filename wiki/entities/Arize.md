---
title: "Arize"
type: entity
tags: [company, ai, observability, eval, platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
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
- Laurie Voss (Head of Developer Experience) delivered a hands-on workshop covering the full eval lifecycle: instrumentation with OpenTelemetry and Phoenix, code evals, built-in LLM evals (correctness, faithfulness), custom LLM-as-judge evals (actionability), meta-evaluation, experiments, and practical frameworks like the impact hierarchy, data flywheel, and Swiss cheese model.
- Phoenix Cloud provides a zero-install option for workshops — traces are sent to app.phoenix/s/<username> with an API key.
- Has two products: Arize Phoenix (open-source) and Arize AX (enterprise). Signing up on the homepage defaults to AX.
- Dat Ngo (AI Architect) frames Arize's mission around three pillars: observability (traces, spans, sessions, distributional views), evals (five flavors of signal, four eval scopes), and experimentation/improvement (datasets, controlled experiments, automated flywheel).
- Ultimate vision: fully automate users out of the observability-evals-experimentation loop via the AI assistant Alex and programmatic APIs for coding agents.
- Exposes all primitives via CLI and tools/skills so external coding agents (Claude Code, Codex) can drive the platform.
- Customers include Uber, Booking.com, and Reddit.

## Related
- [[AparnaDhinakaran]] — speaker from Arize
- [[SallyAnnDeLucia]] — Head of Product at Arize
- [[FuadAli]] — Product Manager at Arize
- [[AmanKhan]] — AI PM at Arize
- [[LaurieVoss]] — Head of Developer Experience at Arize
- [[DatNgo]] — AI Architect at Arize
- [[AlexArizeAgent]] — Arize's internal AI assistant
- [[BookingCom]] — Arize client
- [[Phoenix]] — open-source version of Arize
- [[LLMAsJudge]] — core evaluation technique used by the platform
- [[EvalEngineering]] — practice the company advocates for
- [[PromptLearning]] — technique the platform supports
- [[CoEvolvingLoops]] — optimization philosophy promoted by Arize
- [[AgentVisualization]] — feature shipped by Arize
- [[PromptPlayground]] — feature in the Arize platform
- [[SmartTruncation]] — context management strategy used by Arize's Alex
- [[LongSessionEvals]] — evaluation technique developed at Arize
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — source
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
- [[ArizeAX]] — enterprise version
