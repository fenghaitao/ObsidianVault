---
title: "20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"
author: "Bertrand Charpentier"
date: 2026-06-01
ingested: 2026-06-30
---

## Core Thesis

The question "what model is state-of-the-art?" has no single answer. Both common approaches — checking public leaderboards and running internal evaluations — are deeply flawed. Leaderboards disagree with each other, aren't task-specific, and lack statistical significance. Internal evaluations suffer from manual inspection bias, inconsistent metrics, and small sample sizes. Moreover, quality is driven by compute, and the marginal quality gain from larger models often isn't worth the efficiency cost. The real answer is multiple state-of-the-art models along a Pareto frontier of quality vs. efficiency. Proper model selection requires evaluating on many samples, targeting your specific use case, using multiple benchmarks, and always considering efficiency alongside quality.

## Key Points

- **Two naive approaches to finding SOTA**: (1) Check public leaderboards and pick the top model; (2) Run internal benchmarks with manual inspection. Both tend to lazily select large foundation models without deeper consideration.
- **Leaderboard inconsistency**: Design Arena, LM Arena (now Arena), and Artificial Analysis all rank image editing models differently. Top models vary, Elo score ranges differ (some 1100-1300, others completely different ranges), and some models appear on only some leaderboards. No single leaderboard is trustworthy.
- **Task-specific rankings matter**: Aggregate leaderboard scores obscure performance on specific tasks. When broken down by use case (removing objects, changing backgrounds, editing text), rankings change completely. ChatGPT Image is never #1 on any specific task leaderboard.
- **Statistical insignificance**: Public leaderboards are built on only a few thousand samples — negligible compared to millions of inferences per day in real applications. Win rates show that even top models lose at least 40% of battles; your use case may fall in that 40%.
- **Manual inspection is doubly biased**: Bertrand demonstrated with audience voting that (1) people have different aesthetic preferences, and (2) people change their minds based on which samples they see. Manual inspection biases by both the evaluator and the sample selection.
- **Metric inconsistency**: CLIP score rankings change completely across different datasets, with variations between models being super small — making it hard to distinguish models. Task-specific metrics (e.g., text rendering metrics) produce much more consistent rankings with significant differences between models.
- **The compute cost of evaluation**: ChatGPT Image evaluations on Design Arena took 26K battles, each image taking 62 seconds — totaling 20 days of compute, $5K cost, and 556 kWh of energy (equivalent to ~400 marathons). An optimized model like Pruna's can do the same evaluation in 7 hours, $265, and the energy equivalent of ~4 marathons.
- **The Pareto frontier approach**: Plot efficiency (latency or price) on x-axis vs. quality (Elo score) on y-axis. The Pareto frontier reveals multiple state-of-the-art models — not one. Models can be 20x faster with comparable quality. Task-specific Pareto fronts (e.g., text rendering) are even more informative.
- **Efficiency techniques**: Pruna uses module-specific quantization, pruning of unimportant components, and step reduction (denoising from 50 steps down to 4-20 via distillation or caching). Their open-source package provides compression algorithms; they also have proprietary algorithms for hosted models.
- **Benchmarking isn't dead**: Done properly — many samples, use-case conditions, multiple benchmarks, efficiency considered — benchmarking reveals that small performance models often beat large foundation models for specific tasks.

## Entities Mentioned

- [[Bertrand Charpentier]] — Speaker, from Pruna
- [[Pruna]] — Company building "performance models" — compressed, efficient AI models served behind API endpoints; also contributes open-source compression tools
- [[ChatGPT Image]] — OpenAI's image generation model; ranked #1 on some aggregate leaderboards but never #1 on task-specific rankings
- [[Black Forest Labs]] — Creator of Flux models; collaborated with Pruna on optimizing Flux 2 Flex for text rendering
- [[Flux]] — Image model family from Black Forest Labs; Flux 2 Flex variant optimized with Pruna for efficiency
- [[Design Arena]] — Public leaderboard for image editing models
- [[LM Arena]] — Now called "Arena"; public leaderboard ranking AI models
- [[Artificial Analysis]] — Public leaderboard for AI model comparisons

## Concepts Introduced

- [[State-of-the-Art Ambiguity]] — The problem that "state-of-the-art" is not a single, well-defined concept; different leaderboards, tasks, and evaluation methods yield different answers
- [[Public Leaderboards]] — Aggregated rankings of AI model performance; useful as a starting point but unreliable when used naively due to inconsistency, lack of task specificity, and small sample sizes
- [[Elo Score]] — Quality score used by leaderboards to rank models; ranges and meanings vary between leaderboards, making cross-leaderboard comparisons difficult
- [[Win Rate]] — The percentage of head-to-head battles a model wins; even top models lose 40%+ of battles, meaning the "best" model is wrong for a significant fraction of use cases
- [[Manual Inspection Bias]] — The double bias introduced by evaluating models through manual inspection: evaluator preference bias and sample selection bias
- [[Model Efficiency]] — The consideration of compute cost, latency, and energy alongside quality when evaluating models; the Pareto frontier approach shows multiple efficient SOTA models exist
- [[CLIP Score]] — A standard metric for evaluating image models; rankings change across datasets and variations between models are small, making it unreliable for distinguishing models
- [[Performance Models]] — Pruna's term for compressed, optimized models that achieve comparable quality to large foundation models at a fraction of the compute cost

## Related

- [[summary-20260508 - FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs]] — also discusses Flux models and image generation
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — image/video generation models
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — model evaluation and benchmarks
- [[summary-20260410 - Running LLMs locally： Practical LLM Performance on DGX Spark — Mozhgan Kabiri chimeh, NVIDIA]] — model efficiency and quantization
