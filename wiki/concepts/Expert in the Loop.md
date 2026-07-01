---
title: "Expert in the Loop"
type: concept
tags: [data-quality, human-annotation, ai-data, scaling, quality-assurance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Expert in the Loop is a data generation and quality assurance approach where human domain experts guide the creation and validation of training data and evaluation tasks. Snorkel uses human experts combined with LLM judges and rubric-based evaluation to deliver high-quality data at scale, treating expert involvement as an essential element of data quality rather than an optional enhancement.

## Key Information
- **Snorkel's approach**: Human experts are central to data generation, providing ground truth information that can then be used to inform and calibrate LLM judges
- **Scaling mechanism**: Experts define rubrics and provide initial annotations; LLM judges replicate and scale what human annotators deliver, with ongoing validation through inter-annotator agreement
- **Quality foundation**: Snorkel has a "strong feeling that the expert in the loop is an important element of delivering data quality" — it is not just about having humans involved but having the right expertise
- **Platform integration**: Snorkel's platform brings together human annotators and LLM judges, using experts to give ground truth that informs automated quality assessment
- **Rubric development**: Experts help build rubrics with detailed criteria that both LLM judges and human annotators can apply consistently
- **Across domains**: Applied in both verifiable domains (coding, math — where tests pass/fail) and less verifiable domains (emotional, human-centric tasks with spectrum-based scoring)
- **Contrast with pure automation**: Explicitly positioned against approaches that rely solely on automated data generation without expert oversight; the quality difference is empirically measurable (5x training uplift)

## Related
- [[InterAnnotator Agreement]] — quality validation technique enabled by expert ground truth
- [[RubricBased Evaluation]] — framework experts help develop
- [[LLMAsJudge]] — scaled evaluation informed by expert annotations
- [[Snorkel]] — company using this approach
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[Task Fidelity Scaling Laws]] — research validating the importance of expert-driven quality
- [[Task Quality in Agentic Benchmarks]] — quality framework experts help ensure
- [[HumanInTheLoopEvaluation]] — related concept for validating LLM judges
