---
title: "LLM Code Quality Evaluation"
type: concept
tags: [evaluation, llm, code-quality, security, benchmarking, sonar]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
LLM Code Quality Evaluation is the practice of assessing LLM-generated code across multiple dimensions beyond functional correctness — including security vulnerabilities, bugs, cyclomatic complexity, cognitive complexity, and verbosity. Sonar's framework evaluates models on 4,444+ Java programming assignments to provide a holistic view of code quality that traditional benchmarks (SWE-bench, HumanEval, MBPP) miss.

## Key Information
- **Beyond functional correctness**: traditional benchmarks measure only whether code passes test cases, missing security, maintainability, and engineering discipline
- **Multi-dimensional assessment**: security issues per million LOC, bugs per million LOC, cyclomatic complexity, cognitive complexity, lines of code (verbosity)
- **Scale**: 4,444+ distinct Java programming assignments from open source datasets
- **53+ models evaluated**: including Gemini, Claude, GPT families across multiple versions and thinking variants
- **Key findings**: high SWE-bench scores don't correlate with low security issues or bugs; newer models generate more code but also more complexity; models fix known issues but introduce subtler bugs
- **Verbosity trend**: GPT 4.0 generated ~250K LOC, GPT 5.2 High ~1M LOC, GPT 5.4 ~1.2M LOC for the same tasks
- **Security trend**: total vulnerabilities decreasing but shifting to different, sometimes more subtle categories
- **Public transparency**: all evaluation data published on Sonar Leaderboard

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — evaluation framework creator
- [[Sonar Leaderboard]] — public results platform
- [[Enterprise Quality Code]] — quality standard being evaluated
- [[Cyclomatic Complexity]] — evaluation dimension
- [[Cognitive Complexity]] — evaluation dimension
- [[Code Verbosity]] — evaluation dimension
- [[Code Security]] — evaluation dimension
- [[Mixed Quality Training Data]] — root cause of quality issues
- [[SWE-bench]] — traditional benchmark (functional correctness only)
- [[Model Evaluation]] — broader evaluation concept
