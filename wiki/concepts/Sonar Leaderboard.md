---
title: "Sonar Leaderboard"
type: concept
tags: [leaderboard, llm, code-quality, evaluation, sonar, benchmark]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
The Sonar Leaderboard (sonar.com/leaderboard) is a public evaluation platform that assesses LLM code generation quality across multiple dimensions beyond functional correctness — including security issues, bugs, cyclomatic complexity, cognitive complexity, and verbosity (lines of code). It covers 53+ models evaluated on 4,444+ Java programming assignments.

## Key Information
- Publicly available at sonar.com/leaderboard
- 53+ models evaluated across multiple versions (including thinking variants)
- Metrics tracked: SWE-bench pass rate (functional correctness), lines of code (verbosity), cyclomatic complexity, cognitive complexity, bugs per million LOC, security issues per million LOC
- Data is open-sourced for public transparency
- Continuously updated as new models are released
- Top performers (80%+ accuracy): Gemini 3.1 Pro High (84.17%), plus four other models crossing the 80% threshold
- Enables informed model selection based on organizational architecture and quality needs
- Each model has detailed breakdown of specific issue types
- Complements traditional benchmarks (SWE-bench, HumanEval, MBPP) with quality dimensions

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — creator
- [[SonarQube]] — underlying analysis platform
- [[LLM Code Quality Evaluation]] — evaluation methodology
- [[Enterprise Quality Code]] — quality standard being measured
- [[Cyclomatic Complexity]] — tracked metric
- [[Cognitive Complexity]] — tracked metric
- [[Code Verbosity]] — tracked metric
- [[SWE-bench]] — complementary benchmark (functional correctness only)
- [[Gemini 3.1 Pro]] — top-performing model
