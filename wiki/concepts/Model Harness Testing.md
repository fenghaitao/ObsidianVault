---
title: "Model Harness Testing"
type: concept
tags: [evals, agent-harness, model-evaluation, agent-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Model Harness Testing is the recognition that when running agent evaluations, three distinct components are being tested simultaneously: the model itself, the coding harness, and the quality of the evaluation problems. Understanding which component is the bottleneck is essential for effective [[Hill Climbing (Evals)]].

## Key Information

### Three Components Being Tested

1. **The Model Itself**: A strong model can compensate for a weak harness — it can "overshoot" so hard that you get a great score despite having a horrible agent. Conversely, a weak model will struggle regardless of harness quality.

2. **The Coding Harness**: How well the agent framework actually leverages the model's capabilities. This explains why Anthropic models may work well with Cursor or other coding agents but seem to work significantly better with Claude Code — the harness is better at extracting the model's potential. The harness includes tool calling, context management, guardrails, and the agent loop.

3. **The Problem Quality**: If you're testing on trivial or irrelevant problems, a 100% score means nothing. The problems must be meaningful approximations of real-world tasks. [[TerminalBench]] is cited as an example where problem quality has been well-managed by the Loda Institute.

### Practical Implications
- When a score is low, you must diagnose which of the three components is the bottleneck
- Fixing the harness (Zone 1-2 of [[Three Zones of Improvement]]) often produces larger gains than switching models
- A great harness with a cheap model can outperform a poor harness with an expensive frontier model
- Problem quality must be continuously validated — saturated benchmarks test nothing useful

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[AgentHarness]] — the coding harness component
- [[Three Zones of Improvement]] — framework for which component to improve
- [[Hill Climbing (Evals)]] — the methodology that disentangles these components
- [[TerminalBench]] — benchmark with well-managed problem quality
- [[Harness Engineering]] — the discipline of building effective harnesses
