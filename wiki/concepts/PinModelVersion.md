---
title: "PinModelVersion"
type: concept
tags: [best-practice, llm, api, reliability, production]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Pin Model Version is the practice of locking LLM API calls to a specific model version (e.g., GPT-4 1106, GPT-4o) rather than using a floating latest alias. This is critical because LLM APIs exhibit behavior changes that are hard to quantify, and unpinned versions cause silent drift in application behavior.

## Key Information
- Advocated by Shreya Shankar in the 2024 AI Engineer Summit keynote's tactical section
- LLM APIs are known to exhibit different behavior for certain tasks across versions — changes that are "very hard to quantify"
- Using floating aliases (like "gpt-4" which points to the latest version) means your application behavior drifts silently when the provider updates the underlying model
- Part of the broader traceability practice: know which model version, prompt version, and code version produced each output
- Complemented by MLflow-style traceability — the ability to trace back from any output to the exact configuration that produced it

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[ShreyaShankar]] — advocated this practice
- [[MLflow]] — tool that pioneered model version traceability
- [[ContinuousImprovement]] — the framework this practice supports
- [[EvalEngineering]] — evals are impacted by unpinned model changes
