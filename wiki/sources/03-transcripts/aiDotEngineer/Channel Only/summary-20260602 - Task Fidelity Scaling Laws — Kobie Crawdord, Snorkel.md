---
title: "Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel.md"
author: "Kobie Crawford"
date: 2026-06-02
ingested: 2026-06-30
---

## Core Thesis

Data quality is the critical factor in AI training outcomes, and this extends to task quality in agentic benchmarks. Snorkel's research empirically validates that higher-quality benchmark tasks produce dramatically better RL training results — a ~5x improvement uplift (6% vs 1%) when training on accepted (high-quality) tasks versus rejected (low-quality) tasks. The quality of the data used for training and evaluation is not just a philosophical position but a measurable, empirically verifiable driver of model performance.

## Key Points

- **Snorkel's origin and thesis**: Founded from a Stanford University AI research lab, Snorkel's core thesis since 2019 has been that data quality is critical. They are a "frontier AI data lab" producing datasets for foundation models to train on.
- **Task quality definition**: Four criteria define a high-quality agentic task: (1) achievable, (2) non-trivial, (3) functionally correct (logic plays as expected), (4) environment is reliable. These are verified through Snorkel's research harness tests.
- **Accepted vs rejected tasks**: Tasks passing all four criteria are "accepted" (high-quality); those failing any are "rejected" (low-quality). These two buckets form the basis for empirical comparison.
- **Empirical validation with SOTA models**: Using Sonnet 4.5 and Codex (GPT-5.1, GPT-5.2, GPT-4.0 variants), Snorkel compared performance on accepted vs rejected tasks. Accepted tasks showed: 2x more tool calls (more difficulty, more steps), lower pass rates (higher intrinsic difficulty), and more output tokens (more reasoning required).
- **Failure mode analysis**: Failures were categorized to distinguish meaningful failures (model couldn't achieve logical conclusion) from degenerate failures (environmental problems that no model could solve). Accepted tasks produced "cleaner" failures — failures due to genuine task difficulty rather than underspecification or environmental noise.
- **The 5x training uplift**: RL training with the same model, same compute budget, and same number of tasks showed: low-quality tasks improved the base model by ~1%, while high-quality tasks improved it by ~6% — a 5x uplift difference attributable purely to task quality.
- **Benchmark noise from low-quality tasks**: In public benchmarks like Terminal Bench, tasks that are literally impossible to complete become a source of noise that masks whether models are actually improving. These impossible tasks create a ceiling that models can never surpass.
- **Underspecification as a quality issue**: A common cause of rejected tasks is underspecification — the task definition doesn't clearly specify the desired testable outcome, but back-end tests expect things that were never requested. Implicit dependencies in tests that aren't communicated to the model also cause failures.
- **Expert in the loop**: Snorkel uses human experts in the loop for data generation and quality assurance, combined with LLM judges and rubric-based evaluation to scale quality assessment.
- **Inter-annotator agreement**: Snorkel tests and achieves high inter-annotator agreement between individual humans and between LLM judges and humans, using rubrics with detailed criteria. This agreement data informs quality assessment across all domains.
- **Open benchmark grants program**: Snorkel partners with organizations developing benchmarks in less verifiable domains (emotional, human-centric tasks with multiple possible outcomes scored on a spectrum), extending quality principles beyond coding and math.
- **Future challenges**: Verification is straightforward in coding and math but becomes fuzzy in long-horizon, open-ended tasks. Snorkel is exploring multiple possible outcomes scored differently on a spectrum.

## Entities Mentioned

- [[Kobie Crawford]] — Speaker, Developer Advocate at Snorkel
- [[Snorkel]] — Frontier AI data lab; produces datasets for foundation models; originated from Stanford University AI research lab
- [[Stanford]] — Stanford University, where Snorkel's origins began from an AI research lab and the CEO's PhD thesis
- [[TerminalBench]] — Benchmark referenced for terminal-bench-style agentic tasks; cited as having tasks that never get completed, creating noise in model improvement evaluation

## Concepts Introduced

- [[Task Fidelity Scaling Laws]] — Empirical finding that higher-quality agentic benchmark tasks produce ~5x better RL training outcomes (6% vs 1% improvement)
- [[InterAnnotator Agreement]] — Measuring agreement between human annotators and between LLM judges and humans to validate quality assessment; used by Snorkel with rubric-based criteria
- [[Expert in the Loop]] — Using human domain experts to guide data generation and quality assurance, combined with LLM judges to scale the process
- [[Task Quality in Agentic Benchmarks]] — Four criteria (achievable, non-trivial, functionally correct, environment reliable) defining high-quality agentic tasks; quality directly impacts training outcomes
- [[Underspecification in Agentic Tasks]] — Task definitions that fail to clearly specify desired testable outcomes, causing mismatches between requested behavior and backend test expectations
- [[Benchmark Noise from Task Quality]] — Impossible-to-complete tasks in benchmarks mask whether models are actually improving, creating false ceilings

## Related

- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — Terminal Bench discussion, minimal agent design
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — benchmark saturation, task quality
- [[summary-20260525 - Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind]] — agentic evaluations at scale
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — evaluation and feedback loops
