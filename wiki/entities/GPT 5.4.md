---
title: "GPT 5.4"
type: entity
tags: [model, llm, openai, gpt, frontier-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
GPT 5.4 is an OpenAI model release evaluated in Sonar's LLM code quality assessment. It was identified as generating the highest verbosity — 1.2 million lines of code for 4,444+ Java programming assignments, roughly 4x more than Gemini 3.1 Pro High.

## Key Information
- Evaluated by Sonar on 4,444+ Java programming assignments
- Generated 1.2 million lines of code — the most verbose among evaluated models
- GPT 5.4 Pro High variant also evaluated with similarly high verbosity
- Represents a trend where newer, larger models generate increasingly more code for the same tasks
- This verbosity contributes to higher complexity (cyclomatic and cognitive) and maintenance burden
- Demonstrates that higher capability does not necessarily mean higher quality code output

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[OpenAI]] — creator
- [[GPT 5.2]] — predecessor, generated ~1M LOC
- [[Sonar Leaderboard]] — evaluation context
- [[LLM Code Quality Evaluation]] — evaluation framework
- [[Code Verbosity]] — key quality concern
- [[Cyclomatic Complexity]] — correlated with verbosity
