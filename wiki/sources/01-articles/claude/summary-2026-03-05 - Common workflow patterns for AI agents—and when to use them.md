---
title: "summary-2026-03-05 - Common workflow patterns for AI agents—and when to use them"
type: source
tags: [source, agent-workflows, orchestration, patterns]
sources: ["raw/01-articles/claude/2026-03-05 - Common workflow patterns for AI agents—and when to use them.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic lays out three production-proven agent workflow patterns — sequential, parallel, and evaluator-optimizer — as the building blocks covering the vast majority of real-world agent deployments. Workflows don't replace agent autonomy; they shape where and how agents apply it, giving intelligence within each step and predictability across the overall flow.

## Key Points

- **Sequential**: tasks execute in a predetermined order, each stage's output feeding the next. Best for tasks with clear dependencies and genuinely different work per stage; trades latency for accuracy by focusing each agent narrowly. Try a single-agent prompt first — only split into sequential steps if one agent can't handle it reliably.
- **Parallel**: independent tasks run simultaneously across multiple agents (fan-out/fan-in), then results are merged. Best when subtasks are truly independent or multiple perspectives are needed; enables separation of concerns across engineers. Avoid when agents need cumulative context, when result aggregation becomes too complex, or when there's no clear strategy for resolving contradictory outputs — design the aggregation strategy (majority vote, confidence averaging, most-specialized-agent deference) before implementing.
- **Evaluator-optimizer**: one agent generates content, another evaluates it against specific criteria, and the generator refines iteratively until a quality threshold or max-iteration count is hit. Works when quality criteria are clear/measurable and the first-attempt-to-final quality gap justifies the extra tokens/latency; skip it when first-attempt quality already suffices, criteria are too subjective for consistent AI evaluation, or a deterministic tool (e.g., a linter) already exists. Set explicit stopping criteria upfront to avoid expensive loops that plateau in quality.
- **General guidance**: default to sequential; move to parallel only when latency is the bottleneck and tasks are independent; add evaluator-optimizer loops only when the quality improvement is measurable. Patterns are modular building blocks — nest or combine them as requirements grow, avoiding complete rewrites.

## Related

- [[MultiAgentSystem]] — related concept covering when multi-agent architectures beat a single agent; this article covers the *shape* of the workflow once multiple agents are used
