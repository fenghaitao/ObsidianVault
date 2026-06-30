---
title: "Cognitive Complexity"
type: concept
tags: [code-quality, metrics, complexity, sonar, software-engineering, static-analysis, readability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Cognitive complexity is a Sonar-proprietary software metric that measures how difficult code is for a human being to read, understand, and maintain. Unlike cyclomatic complexity (which counts branches), cognitive complexity assesses readability from a human comprehension perspective, penalizing constructs that increase mental effort such as nested conditions, recursion, and breaks in linear flow.

## Key Information
- Sonar proprietary metric designed to complement cyclomatic complexity
- Measures human readability and maintainability rather than structural branching
- Penalizes constructs that increase mental effort: deeply nested conditions, recursion, non-linear control flow
- Used as a key dimension in Sonar's LLM code quality leaderboard evaluating 53+ models
- Provides a more nuanced view of code quality than cyclomatic complexity alone
- Newer LLM models tend to generate code with higher cognitive complexity, making AI-generated code harder for humans to review and maintain
- Part of the argument that functional correctness (SWE-bench scores) is insufficient — code must also be understandable and maintainable by humans

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Cyclomatic Complexity]] — complementary structural complexity metric
- [[Sonar]] — company that created this metric
- [[SonarQube]] — platform that calculates cognitive complexity
- [[Sonar Leaderboard]] — tracks cognitive complexity across 53+ models
- [[LLM Code Quality Evaluation]] — evaluation framework using this metric
- [[Enterprise Quality Code]] — quality standard incorporating readability
- [[Code Maintainability]] — closely related quality dimension
