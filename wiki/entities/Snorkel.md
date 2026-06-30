---
title: "Snorkel"
type: entity
tags: [company, data-quality, ai-data, rl-training, benchmarks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Snorkel is a frontier AI data lab that produces high-quality datasets for foundation models to train on. The company originated from a Stanford University AI research lab, with its core technology beginning as part of the CEO's PhD thesis and later released as an open-source library before evolving into a commercial data platform.

## Key Information
- Founded in 2019, with origins at Stanford University's AI research lab
- Core thesis: data quality is critical for AI training outcomes — this has been the consistent through line since founding
- Produces datasets for foundation models, now extending into the agentic space
- Research team is highly integrated with production work, with emphasis on integrating research into practice
- Uses human experts in the loop for data generation, combined with LLM judges and rubric-based evaluation to scale quality
- Validates quality through inter-annotator agreement between humans and LLM judges
- Runs an open benchmark grants program partnering with organizations developing benchmarks in less verifiable domains
- Built and curates benchmarks including "Agentic Coding" focused on terminal-bench-style tasks
- Research on task fidelity scaling laws showed that higher-quality tasks produce ~5x better RL training outcomes (6% improvement vs 1%)
- Task quality criteria: achievable, non-trivial, functionally correct, environment reliable

## Related
- [[Kobie Crawford]] — Developer Advocate at Snorkel
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[Task Fidelity Scaling Laws]] — key research finding from Snorkel
- [[Task Quality in Agentic Benchmarks]] — Snorkel's quality framework
- [[Inter-Annotator Agreement]] — quality validation technique used by Snorkel
- [[Expert in the Loop]] — data generation approach used by Snorkel
- [[TerminalBench]] — benchmark referenced in Snorkel's research
- [[Stanford]] — where Snorkel's technology originated
