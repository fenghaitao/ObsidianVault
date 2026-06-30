---
title: "Benchmark Decontamination"
type: concept
tags: [benchmark, evaluation, data-quality, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
Benchmark decontamination is the practice of ensuring evaluation datasets are free from data that models may have seen during pre-training, preventing inflated benchmark scores from memorization rather than genuine capability.

## Key Information
- **Time splits are the only way**: According to [[Ibragim Badertdinov]], the only reliable method for decontamination is collecting fresh problems after a model's training cutoff date. Static benchmarks released with solutions inevitably leak into pre-training of next-generation models.
- **SWE-rebench approach**: Collects only problems from the previous month, evaluates models monthly, ensuring no model has seen the tasks during training.
- **Problem**: Most benchmarks release both questions and solutions simultaneously, making them susceptible to contamination for future models.
- **Decontamination challenges**: Even with time splits, models can still access solution information through web browsing (e.g., reading GitHub issue conversations) or git history, requiring additional infrastructure-level safeguards.
- **Scale considerations**: Using pull requests instead of issues provides ~8x more data for training runs, important for post-training data generation.

## Related
- [[SWE-rebench]] — benchmark implementing time-split decontamination
- [[BenchmarkSaturation]] — related benchmark limitation
- [[Reward Hacking in Agents]] — models bypassing decontamination safeguards
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
