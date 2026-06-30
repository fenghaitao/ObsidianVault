---
title: "Benchmark Noise from Task Quality"
type: concept
tags: [benchmarks, data-quality, evaluation, agentic-tasks, noise]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Benchmark Noise from Task Quality refers to the phenomenon where low-quality or impossible-to-complete tasks in public benchmarks introduce noise that masks whether models are actually improving. Tasks that can never be completed (due to underspecification, broken environments, or logical errors) create false ceilings that make genuine model progress harder to detect.

## Key Information
- **Impossible tasks as noise**: Tasks that literally cannot be completed (due to design flaws) will never be solved by any model, creating a permanent source of benchmark noise
- **Masking improvement**: When a benchmark contains impossible tasks, it becomes harder to tell whether models are actually improving — the impossible tasks create a floor that obscures real progress
- **Terminal Bench findings**: Snorkel's internal analysis comparing public benchmarks found that some Terminal Bench tasks never get completed, and this was identified as a source of noise in evaluating model improvement
- **Saturation connection**: Task quality noise can contribute to or be confused with benchmark saturation — when scores stop improving, it may be due to impossible tasks rather than model capability ceilings
- **Quality distinction**: This is different from genuine benchmark saturation (where models have mastered all tasks); it represents a design flaw in the benchmark itself
- **Remediation**: Requires task quality assessment (achievable, non-trivial, functionally correct, environment reliable) to identify and filter out impossible tasks

## Related
- [[Task Fidelity Scaling Laws]] — research identifying the impact of task quality on training
- [[Task Quality in Agentic Benchmarks]] — framework for assessing task quality
- [[Underspecification in Agentic Tasks]] — common cause of impossible tasks
- [[BenchmarkSaturation]] — related but distinct concept about benchmarks losing signal
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[TerminalBench]] — benchmark cited as having quality noise
- [[Snorkel]] — company conducting the analysis
