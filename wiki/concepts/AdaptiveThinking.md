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
- **Opus 4.7 (April 2026)**: exclusively uses adaptive thinking — [[ExtendedThinking|extended thinking]] with a fixed token budget is not supported on this model. Adaptive thinking is reported as improved and less prone to overthinking versus the prior release. See [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]].
- **Effort-level tuning for [[ComputerUse|computer use]] (May 2026)**, benchmarked on OSWorld Verified and end-to-end UI automation tasks: `medium` effort is the general sweet spot (near-highest success rate at roughly half the output tokens of `high`; performance plateaus beyond `medium`, and `medium`/`high` converge under retries). `low` effort is a surprisingly strong low-cost option — it uses fewer total output tokens than disabling thinking entirely (fewer mistakes, fewer retries) while matching or slightly beating no-thinking accuracy, making it best for high-throughput workloads. `max` is explicitly **not recommended** for computer use — no accuracy benefit over `high`, since UI tasks are primarily perceptual rather than deeply logical. Opus 4.7 at `low` effort scores similarly to Sonnet 4.6 at `max`, using ~1/10th the tokens. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-14 - The thinking lever]] — London talk on thinking
- [[summary-14 - The thinking lever]] — San Francisco talk on thinking
- [[Claude4.7Opus]] — model that exclusively uses adaptive thinking (no fixed-budget extended thinking); corrected from an earlier mislink to [[ClaudeFable5]]
- [[ClaudeCode]] — defaults to extra high effort with adaptive thinking
- [[ContextWindow]] — related constraint on model reasoning
- [[summary-2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code]] — source summary
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — effort-level benchmarks specifically for computer-use / UI automation tasks
- [[ComputerUse]] — capability whose effort-level tuning is benchmarked here
