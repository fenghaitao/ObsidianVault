---
title: "Sonar"
type: entity
tags: [company, code-quality, static-analysis, security, llm-evaluation, devtools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Sonar is a code quality and security company known for its SonarQube platform. It has expanded into evaluating and improving LLM-generated code quality through its evaluation framework, leaderboard, and the ACDC (Agent-Centric Development Cycle) product portfolio.

## Key Information
- Creator of SonarQube, a widely used static code analysis platform
- Has evaluated 53+ LLM models on 4,444+ Java programming assignments for code quality beyond functional correctness
- Maintains a public LLM quality leaderboard at sonar.com/leaderboard
- Developed the ACDC framework: Guide (Sonar Sweep, Context Augmentation), Verify (Agentic Analysis), Solve (Remediation Agent)
- Supports 40+ programming languages and frameworks
- Products integrate with IDEs, CI/CD pipelines, and DevOps workflows
- SonarQube Agentic Analysis runs in 1-5 seconds (vs. 1-5 minutes for CI), enabling pre-commit code quality checks
- SonarQube Remediation Agent creates PRs per issue, re-runs analysis and compilation, and discards regressions
- Proprietary metrics include cognitive complexity (how hard code is for humans to read and understand)

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Prasenjit Sarkar]] — speaker/presenter
- [[SonarQube]] — flagship product
- [[ACDC Framework]] — Agent-Centric Development Cycle
- [[Sonar Leaderboard]] — public model quality leaderboard
- [[Cognitive Complexity]] — proprietary metric
- [[Cyclomatic Complexity]] — standard metric used in evaluation
- [[LLM Code Quality Evaluation]] — evaluation methodology
- [[Enterprise Quality Code]] — quality standard
