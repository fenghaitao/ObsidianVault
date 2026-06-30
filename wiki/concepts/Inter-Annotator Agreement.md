---
title: "Inter-Annotator Agreement"
type: concept
tags: [data-quality, evaluation, human-labeling, llm-as-judge, annotation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Inter-Annotator Agreement is a measure of consistency between different evaluators (human annotators or LLM judges) when assessing the same outputs against defined criteria. Snorkel uses high inter-annotator agreement — both between individual humans and between LLM judges and humans — as a key quality signal to validate their data generation and evaluation processes.

## Key Information
- **Snorkel's approach**: Tests and achieves high inter-annotator agreement between individual human annotators and between LLM judges and humans
- **Rubric-based**: Uses detailed rubrics with longer lists of criteria and data points to achieve consistent agreement. Rubrics are used by both human annotators and LLM judges
- **Quality assessment role**: Inter-annotator agreement data is used as part of Snorkel's quality assessment process across all domains — from explicitly verifiable coding tasks to more subjective domains
- **Scaling mechanism**: Human experts provide ground truth information that informs LLM judges, allowing quality assessment to scale beyond what humans alone could handle
- **Domain applicability**: Even in explicitly verifiable domains (where tests pass or fail deterministically), Snorkel maintains this guiding principle as part of their overall quality framework
- **Multi-dimensional**: Agreement is measured on both high-level qualitative aspects and individual quantitative comparisons through rubric criteria

## Related
- [[LLM-as-Judge]] — the automated evaluation technique validated through inter-annotator agreement
- [[HumanInTheLoopEvaluation]] — validating LLM judges against human labels
- [[Rubric-Based Evaluation]] — the rubric framework enabling consistent agreement
- [[Expert in the Loop]] — human experts providing ground truth for agreement measurement
- [[Snorkel]] — company using this technique
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[Task Quality in Agentic Benchmarks]] — quality framework this validates
