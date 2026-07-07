---
title: "AgentWorkflowPatterns"
type: concept
tags: [agent-workflows, orchestration, sequential, parallel, evaluator-optimizer]
sources: ["raw/01-articles/claude/2026-03-05 - Common workflow patterns for AI agents—and when to use them.md"]
last_updated: 2026-07-04
---

## Definition

Agent workflow patterns are structured execution shapes that channel an AI agent's autonomy toward complex, multi-step problems requiring coordination, predictability, or orchestrated timing. A workflow doesn't replace agent autonomy — it establishes checkpoints and boundaries within which agents still reason and act dynamically. Anthropic identifies three patterns covering most production use cases: sequential, parallel, and evaluator-optimizer.

## Key Information

### Sequential

Tasks execute in a predetermined order; each stage processes inputs, makes tool calls as needed, and passes results to the next stage.
- **Use when**: tasks naturally break into distinct stages with clear dependencies and genuinely different work per stage — trading some latency for higher accuracy by focusing each agent narrowly.
- **Avoid when**: a single agent handles the whole task effectively, or agents need to collaborate rather than hand off linearly.
- **Pro tip**: try a single-agent prompt first; only split into sequential steps if one agent can't handle it reliably.

### Parallel

Independent tasks distribute across multiple agents executing simultaneously (a fan-out/fan-in pattern), then results are merged — agents don't hand off work, they operate autonomously and contribute to an aggregated outcome.
- **Use when**: work divides into independent subtasks that benefit from simultaneous processing, or multiple perspectives on the same problem are needed; also enables separation of concerns across engineers/teams.
- **Avoid when**: agents need cumulative context or must build on each other's work, resource constraints (API quotas) make concurrency inefficient, or there's no clear strategy for resolving contradictory results.
- **Pro tip**: design the aggregation strategy (majority vote, confidence averaging, deference to the most specialized agent) *before* implementing — otherwise you collect conflicting outputs with no resolution path.

### Evaluator-Optimizer

Two agents run an iterative cycle: one generates content, another evaluates it against specific criteria, and the generator refines based on feedback — continuing until a quality threshold or max-iteration count is hit. Separating generation and evaluation lets each agent specialize in a distinct cognitive task.
- **Use when**: quality criteria are clear and measurable enough for consistent AI evaluation, and the gap between first-attempt and final quality justifies the extra tokens/latency.
- **Avoid when**: first-attempt quality already meets the bar, the task is real-time/simple/routine, evaluation criteria are too subjective, or a deterministic tool (e.g., a linter) already solves it.
- **Pro tip**: set explicit stopping criteria (max iterations, quality thresholds) upfront — without guardrails, the evaluator keeps finding minor issues while quality plateaus well before iteration stops.
- **Cross-reference (April 2026)**: [[MultiAgentSystem]]'s companion coordination-patterns taxonomy names this same mechanic "generator-verifier" (a generator produces output, a verifier accepts/returns feedback, looping to a max-iteration cap), framed from a multi-agent-architecture lens rather than a workflow-shape lens. See [[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]].

## Choosing and Combining Patterns

Try the task as a single agent call first; if that meets the quality bar, stop there. If not, identify *where* it falls short — that indicates which pattern to reach for. Patterns are building blocks, not mutually exclusive templates: a sequential workflow can incorporate parallel processing at a bottleneck stage, or add an evaluator-optimizer loop as quality standards tighten, without requiring a full rewrite. Default to sequential; move to parallel only when latency is the bottleneck and tasks are independent; add evaluator-optimizer loops only when the quality gain is measurable.

These three patterns describe **static workflows** — pre-built by a human developer using the Claude Agent SDK or `claude -p`. As of May 2026, [[DynamicWorkflows|dynamic workflows]] let Claude write and orchestrate its own harness on the fly, composing these and additional patterns (classifier routing, fan-out/synthesis, adversarial verification, tournaments, parallel competition, agentic loops, quarantine, model selection) into custom JavaScript harnesses tailored to the specific task — a runtime evolution of the static workflow paradigm.

## Related

- [[MultiAgentSystem]] — the broader question of *when* to use multiple agents at all; this concept covers the *shape* once multiple agents are chosen
- [[ClaudeCodeSubagents]] — Claude Code's subagent mechanism, usable to implement any of these three patterns
- [[DynamicWorkflows]] — the runtime evolution of static workflows, letting Claude compose these and additional patterns dynamically
- [[summary-2026-03-05 - Common workflow patterns for AI agents—and when to use them]] — source article
- [[summary-2026-04-10 - Multi-agent coordination patterns Five approaches and when to use them]] — names the same evaluator-optimizer mechanic "generator-verifier" under a coordination-pattern taxonomy
- [[summary-2026-06-02 - A harness for every task dynamic workflows in Claude Code]] — follow-up article cataloging dynamic workflow patterns
