---
title: "Mixed Quality Training Data"
type: concept
tags: [training-data, llm, code-quality, security, data-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Mixed quality training data refers to the problem that LLM training datasets contain both high-quality and low-quality code examples, including insecure patterns and subtle bugs. When models train on this mixed data, they learn to reproduce the flaws alongside the good patterns, contributing to security vulnerabilities and quality issues in generated code.

## Key Information
- **Source of the problem**: open source code and other public datasets used for training contain insecure code examples, hidden bugs, and poor engineering practices
- **Built-in security flaws**: models pick up insecure coding patterns from training data that contains known vulnerabilities
- **Hidden bugs**: subtle logic errors in training data cause models to produce code that fails or misbehaves in production
- **Probabilistic reproduction**: models don't deterministically reproduce flaws — they probabilistically mix good and bad patterns
- **Sonar's response**: Sonar Sweep treats training data quality as a first-class concern in the ACDC framework — fixing data at the source rather than trying to fix generated code
- **Maturation effect**: as models undergo more reinforcement learning, they fix known security issues but introduce new, subtler bugs that are harder for humans to detect

## Related
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Sonar]] — addressing this via Sonar Sweep
- [[ACDC Framework]] — Guide phase addresses this
- [[Enterprise Quality Code]] — quality standard undermined by this problem
- [[LLM Code Quality Evaluation]] — evaluation framework that exposes this
- [[Code Security]] — directly impacted dimension
