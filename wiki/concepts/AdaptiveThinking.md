---
title: "AdaptiveThinking"
type: concept
tags: [thinking, reasoning, test-time-compute, effort, model-capability]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/15 - The thinking lever.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/14 - The thinking lever.md]
last_updated: 2026-06-23
---

## Definition

Adaptive thinking is Claude's capability to freely choose when to think, call tools, or output text in any order during task execution. Unlike earlier paradigms where thinking was mandated at specific points (e.g., before tool calls), adaptive thinking gives Claude the option to use its internal reasoning scratchpad whenever appropriate — including skipping thinking entirely for simple queries.

## Key Information

- **Evolution:** Fixed thinking → Interleaved thinking (think between tool calls) → Adaptive thinking (think whenever appropriate, in any order).
- **Not a model router:** Claude isn't classifying requests by difficulty; it's given the thinking tool and decides when to use it.
- **Three token types:** Thinking (internal monologue), tool calling (interfacing with world), text (communicating with user) — freely interleaved.
- **Pareto efficient:** Adaptive thinking matches or beats interleaved thinking on all benchmarks while delivering better user experience.
- **Thinking toggle is a poor proxy:** Turning off extended thinking removes a core capability rather than expressing desired effort. Better to always enable thinking and control via effort levels.
- **Effort levels:** Low (latency-sensitive), Medium, High, Extra High (default for Claude Code), Max (hardest tasks, diminishing returns).
- **Task budgets:** Upper bounds on token spend before Claude checks in — can be expressed in tokens, time, or cost.

## Related

- [[summary-14 - The thinking lever]] — London talk on thinking
- [[summary-14 - The thinking lever]] — San Francisco talk on thinking
- [[ClaudeFable5]] — Opus 4.7 enabling adaptive thinking
- [[ClaudeCode]] — defaults to extra high effort with adaptive thinking
- [[ContextWindow]] — related constraint on model reasoning
