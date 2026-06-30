---
title: "Task Fidelity Scaling Laws"
type: concept
tags: [data-quality, rl-training, benchmarks, agentic-tasks, scaling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"]
last_updated: 2026-06-30
---

## Definition
Task Fidelity Scaling Laws describe the empirical relationship between the quality of agentic benchmark tasks and the training outcomes achieved when using those tasks for reinforcement learning. Snorkel's research demonstrated that higher-quality tasks produce ~5x better RL training improvement (6% vs 1% on the same model with the same compute budget), establishing that task quality is not just a philosophical position but a measurable driver of model performance.

## Key Information
- **Core finding**: Training with high-quality (accepted) tasks produced a ~6% improvement over the base model, while low-quality (rejected) tasks produced only ~1% — a 5x uplift difference attributable purely to task quality
- **Experimental setup**: Same model, same compute budget, same number of tasks in each training run; only variable was task quality
- **Validation methodology**: Used Sonnet 4.5 and Codex (GPT-5.1, GPT-5.2, GPT-4.0) to compare performance on accepted vs rejected tasks, confirming accepted tasks showed: 2x more tool calls, lower pass rates, more output tokens
- **Failure mode analysis**: Categorized failures to distinguish meaningful failures (model couldn't achieve logical conclusion) from degenerate failures (environmental problems no model could solve). Accepted tasks produced "cleaner" failures useful for hill climbing
- **Benchmark implications**: Low-quality tasks in public benchmarks become noise that masks whether models are actually improving. Impossible-to-complete tasks create false ceilings
- **Quality definition**: Task quality is defined by four criteria: achievable, non-trivial, functionally correct (logic plays as expected), and environment reliability
- **Extends to data quality**: The same principles apply to dataset quality for foundation model training — Snorkel's core thesis since 2019
- **Models used in validation**: Sonnet 4.5, Codex (GPT-5.1, GPT-5.2, GPT-4.0)

## Related
- [[Task Quality in Agentic Benchmarks]] — the quality framework underlying the scaling laws
- [[summary-20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel]] — source transcript
- [[Snorkel]] — company that conducted the research
- [[Kobie Crawford]] — presenter of the research
- [[TerminalBench]] — benchmark referenced as having quality-related noise
- [[BenchmarkSaturation]] — related concept about benchmarks losing signal
- [[Underspecification in Agentic Tasks]] — common cause of low-quality tasks
- [[Expert in the Loop]] — Snorkel's approach to ensuring data quality
- [[Inter-Annotator Agreement]] — quality validation technique
