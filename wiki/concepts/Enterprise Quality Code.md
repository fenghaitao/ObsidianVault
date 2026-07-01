---
title: "Enterprise Quality Code"
type: concept
tags: [code-quality, enterprise, software-engineering, llm, security, maintainability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Enterprise quality code goes beyond functional correctness to encompass security, maintainability, readability, architectural soundness, engineering discipline, and context-aware analysis. LLM benchmarks like SWE-bench measure only functional correctness (passing test cases) while missing these critical dimensions that determine whether code is truly production-ready.

## Key Information
- **Dimensions beyond functional correctness**: security vulnerabilities, real-world reliability, engineering/architectural problems, engineering discipline, code maintainability, tech debt, context-aware analysis
- **LLM code quality problem**: models achieving 80%+ on SWE-bench still generate hundreds of bugs and security issues per million lines of code
- **Training data quality**: mixed-quality training data (open source, insecure examples) causes models to reproduce security flaws and hidden bugs
- **Probabilistic nature**: same prompt to same model on different days yields different code — not deterministic or explainable
- **Limited context**: models don't understand company-specific codebases, data, or architecture
- **Verbosity trend**: newer models generate increasingly more lines of code, correlated with higher complexity and maintenance burden
- **Quality requires lifecycle integration**: enterprise quality demands code quality checks embedded throughout the development lifecycle, not just at CI/CD

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — company focused on this problem
- [[SonarQube]] — platform for enforcing code quality
- [[LLM Code Quality Evaluation]] — Sonar's evaluation methodology
- [[Cyclomatic Complexity]] — structural complexity metric
- [[Cognitive Complexity]] — human-readability metric
- [[Code Security]] — security dimension of quality
- [[Code Verbosity]] — verbosity as a quality concern
- [[Mixed Quality Training Data]] — root cause of quality issues
- [[ACDC Framework]] — lifecycle approach to quality
- [[SWEBench]] — benchmark that misses quality dimensions
- [[TechnicalDebtInML]] — related concept for ML systems
