---
title: "summary-20260410 - Judge the Judge： Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI"
type: source
tags: [source, transcript, evals, llm-as-judge, gepa, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - Judge the Judge： Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI.md"]
last_updated: 2026-06-30
---

## Core Summary

Mahmoud Mabrouk from Agenta AI presents a workshop on building calibrated LLM-as-judge evaluators using GEPA prompt optimization. The workflow: design specific binary metrics from use cases → annotate traces with reasoning → optimize the judge prompt via GEPA → validate. Calibrated LLM judges enable fast eval loops and the data flywheel.

## Key Points

- Uncalibrated LLM-as-judge gives useless signal — the eval loop moves fast but goes nowhere.
- Workflow: (1) Design metrics from business use case with subject matter experts. (2) Annotate traces with binary labels + reasoning (reasoning is critical for optimization). (3) Optimize judge prompt using GEPA. (4) Validate against held-out annotations.
- Use binary metrics (adhered/failed) not 1-5 scales — even humans struggle to agree on scores.
- Split complex evaluation into multiple specific judges (policy adherence, response style, info delivery, tool usage) rather than one monolithic judge.
- Data annotation is the hardest part: quality, distribution, and reasoning content determine optimization success.
- Demo uses TauBench airline customer support agent with 599 annotated traces.

## Related

- [[Mahmoud Mabrouk]] — speaker, co-founder/CEO Agenta AI
- [[Agenta AI]] — open-source LLMOps platform
- [[LLMAsJudge]] — evaluation technique
- [[GEPA]] — prompt optimization algorithm
- [[EvalEngineering]] — evaluation practice
- [[TauBench]] — benchmark dataset
