---
title: "Claude Sonnet 4.6"
type: entity
tags: [model, llm, anthropic, claude, sonnet]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Claude Sonnet 4.6 is a version of Anthropic's Claude Sonnet model family evaluated in Sonar's LLM code quality assessment. It was identified as generating the highest security risk among the five highlighted models, with approximately 300 security issues per million lines of code.

## Key Information
- Evaluated by Sonar on 4,444+ Java programming assignments
- Generated 627,000 lines of code for the assignment set
- Had the highest security issue density among evaluated models: ~300 security issues per million lines of code
- Demonstrates the trade-off between functional correctness and code quality/security
- Part of Sonar's evaluation of 53+ models showing that high benchmark scores don't guarantee secure code

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Anthropic]] — creator
- [[Sonnet]] — model family
- [[Sonar Leaderboard]] — evaluation context
- [[LLM Code Quality Evaluation]] — evaluation framework
- [[Code Security]] — key quality dimension
- [[Code Verbosity]] — 627K LOC metric
