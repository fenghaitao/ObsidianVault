---
title: "Paul Iusztin"
type: entity
tags: [person, towards-ai, ai-engineering, education, llm-engineer-handbook]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Paul Iusztin is a software engineer with eight years of experience and four-plus years in the AI teaching space. He is the author of the LLM Engineer's Handbook bestseller and a contributor to Towards AI. He presented the writing workflow and observability/eval portions of the deep research workshop.

## Key Information
- Building software for eight years, teaching AI for four-plus years
- Author of the LLM Engineer's Handbook bestseller
- Contributed to the Towards AI deep research workshop, presenting the LinkedIn writing workflow, observability, and AI evals sections
- Designed the evaluator-optimizer pattern for content generation: writer creates draft, reviewer (separate context window) provides structured Pydantic feedback, editor applies prioritized reviews
- Emphasizes that writing workflows are deterministic (not agentic) because content creation follows static steps
- Advocates for structured outputs (Pydantic objects) over free-form LLM responses for reviewer feedback
- Built an AI evals system with labeled datasets, train/dev/test splits, and LLM-as-judge calibration using F1 score
- Uses Opic for observability: threads (full workflows), traces (individual calls), latency, cost, and token tracking
- Recommends fixed iteration counts (3-4) over score-based thresholds for creative evaluator-optimizer loops

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Towards AI]] — company he contributes to
- [[LouisFrançois Bouchard]] — co-presenter
- [[Samridhi]] — co-presenter
- [[aiDotEngineer]] — conference where the workshop was presented
- [[EvaluatorOptimizer Pattern]] — writing refinement pattern he presented
- [[Writing Profiles]] — static styling layer for content generation
- [[LLMAsJudge]] — evaluation technique used for post quality calibration
- [[Structured Outputs]] — Pydantic objects for reviewer feedback
- [[AgentObservability]] — monitoring approach using Opic
- [[EvalEngineering]] — building and calibrating evaluation systems
- [[FewShotExamples]] — in-context learning for generation and evaluation
