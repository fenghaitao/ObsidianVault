---
title: "Claude Sonnet 4.6"
type: entity
tags: [claude, model, anthropic, llm, foundation-model, sonnet, web-search]
sources: ["raw/01-articles/claude/2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering.md"]
last_updated: 2026-07-04
---

## Definition

Claude Sonnet 4.6 is Anthropic's mid-tier model released alongside [[Claude4.6Opus|Claude Opus 4.6]] (February 2026).

## Key Information

- With [[WebSearch|dynamic filtering]] enabled, BrowseComp accuracy rose from 33.3% to 46.6% and DeepSearchQA F1 from 52.6% to 59.4%.
- Price-weighted token costs decreased with dynamic filtering enabled for Sonnet 4.6 on both benchmarks (unlike Opus 4.6, where cost increased).
- **1M context general availability (March 2026)**: full 1M-token context window at standard pricing ($3/$15 per million tokens) across the entire window, no long-context premium multiplier.
- Supports [[ClaudeCode]]'s auto mode (March 2026), a classifier-gated permissions mode. See [[PermissionModes]].
- **[[ComputerUse|Computer use]] (May 2026)**: recommended as the default model for most computer-use clicking tasks, offering the best balance of click precision, reasoning, and cost; more mechanically precise and more robust to heavy screenshot downscaling than Opus 4.6, though [[Claude4.7Opus|Opus 4.7]] has since closed the precision gap. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[Claude4.6Opus]] — sibling flagship model released alongside Sonnet 4.6
- [[WebSearch]] — dynamic filtering benchmarked on this model
- [[ContextWindow]] — 1M-token context window reaching general availability
- [[ClaudeCode]] — permission modes this model supports
- [[PermissionModes]] — auto mode compatibility
- [[summary-2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering]] — source article
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — source summary
- [[summary-2026-03-24 - Auto mode for Claude Code]] — auto mode compatibility announcement
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — recommended default model for computer-use clicking tasks
