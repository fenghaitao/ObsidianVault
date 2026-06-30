---
title: "Code Quality in Agentic Patches"
type: concept
tags: [code-quality, agents, evaluation, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
Code quality in agentic patches refers to the observation that coding agents may produce functionally correct solutions that would fail human code review due to poor practices like leaving test files, not cleaning up, or producing unmaintainable code.

## Key Information
- **Common issues**: Models (Gemini, GLM, GPT) tend to produce reproduction test files and then not remove them, leaving cruft in the codebase.
- **Review gap**: Patches that pass SWE-bench or SWE-rebench verification may still be rejected by human reviewers for quality reasons.
- **Not how things work**: Real developers would not accept patches with leftover test files, inconsistent style, or poor architectural decisions.
- **Future direction**: [[Ibragim Badertdinov]] advocates for incorporating code quality metrics into benchmarks, moving beyond functional correctness.
- **Related to mergeability**: Connects to the broader concept of mergeability scoring, where unit test passing is necessary but insufficient.

## Related
- [[SWE-rebench]] — benchmark considering this as future direction
- [[Test Overfitting]] — related evaluation quality concern
- [[LLM Code Quality Evaluation]] — broader evaluation framework
- [[MergeabilityScoring]] — holistic evaluation beyond unit tests
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
