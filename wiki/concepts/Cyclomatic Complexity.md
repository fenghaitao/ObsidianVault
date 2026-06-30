---
title: "Cyclomatic Complexity"
type: concept
tags: [code-quality, metrics, complexity, software-engineering, static-analysis]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Cyclomatic complexity is a software metric that measures the number of independent execution paths through a program's source code. It counts branching constructs — if/else statements, for loops, while loops, switch statements — to quantify structural complexity. Higher cyclomatic complexity correlates with increased testing difficulty, bug likelihood, and maintenance cost.

## Key Information
- Measures control flow branches: if/else, for loops, while loops, switch statements, and other branching constructs
- Used by Sonar as a key metric in their LLM code quality evaluation alongside cognitive complexity
- Sonar found Gemini 3.1 Pro High had cyclomatic complexity of 234 on 4,444+ Java assignments
- Newer LLMs tend to generate code with higher cyclomatic complexity
- Higher cyclomatic complexity means more test cases needed for full coverage and harder-to-maintain code
- Distinguished from cognitive complexity: cyclomatic measures structural branching; cognitive measures how hard code is for humans to read and understand

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Cognitive Complexity]] — complementary Sonar-proprietary metric
- [[Sonar Leaderboard]] — tracks cyclomatic complexity across 53+ models
- [[LLM Code Quality Evaluation]] — evaluation framework using this metric
- [[Enterprise Quality Code]] — quality standard incorporating complexity
- [[Code Verbosity]] — correlated with higher complexity
- [[SonarQube]] — platform measuring this metric
