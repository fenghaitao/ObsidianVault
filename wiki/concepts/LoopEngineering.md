---
title: "LoopEngineering"
type: concept
tags: [concept, harness, autonomy, loops, claude-code, buzzword]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!.md"
last_updated: 2026-06-21
---

## Definition

Loop Engineering is the (2026) practice of **designing loops that prompt your agents for you** — having an orchestrator wake agents on intervals/goals/schedules to work 24/7 — instead of prompting manually. Popularized by **Boris Cherny** ([[ClaudeCode]] lead: "I don't prompt Claude anymore, I write loops") and **Peter Steinberger** ([[OpenClaw]]). [[ColeMedin]]'s position: useful ideas, but overhyped, token-hungry, and unreliable without a tight system — best **folded into [[HarnessEngineering]]** ("it doesn't deserve its own buzzword").

## Key Information

### The Claude Code primitives

- **`/loop`** — run a prompt on an interval (e.g. every 5 min: handle new GitHub issues) while the terminal is open.
- **`/goal`** — define done-criteria; force the agent to work until met (a [[RalphLoop]]-style loop).
- **`/routines`** — scheduled jobs (e.g. hourly: read a spec, do the next task).

An orchestrator you minimally prompt sets these up via a built-in "loop skill"; you describe the goal at a high level and it writes the loop (e.g. `/loop work through plan.md one task at a time`).

### The three downsides

1. **Not best-in-class results** — claims like "tens of thousands of agents at once" are hyperbole; good for POCs/exploration, not the highest-quality path.
2. **Cost** — orchestrator reasoning + worker fan-out + repeated context-passing burns tokens fast (a simple app: **1M+ tokens** in one run).
3. **Single-session bloat** — `/loop` keeps looping in the *same* session → [[ContextRot]]; you need work distributed across communicating sessions.

### Doing it right (fold into [[HarnessEngineering]])

Cole's mitigations (via [[Archon]] and an experimental loop dashboard):
- **Deterministic workflows** — remove decisions from the agent except where reasoning is required; enforce process in a workflow file.
- **Session-per-step + handoff docs** instead of one bloated loop session.
- **Mix providers per node** for cost (cheap models like Haiku / MiniMax M3 / Kimi K2.7 for classify/explore; Claude Code to implement; Codex to review) — see [[CrossProviderWorkflow]].
- **Durability** — persist run state to a DB ([[Neon]]) so loops resume after a crash.
- **Observability** — a dashboard tracking decisions and cost.
- **Isolation + [[HumanInTheLoop]]** — git worktrees + DB branches for parallel safety ([[ParallelAgenticDevelopment]]); HITL checkpoints so it doesn't "run for a day and return crap."

### Relationship to other concepts

Loop engineering is essentially the **multi-session orchestration** layer of [[HarnessEngineering]] / [[AgentHarness]] with a 24/7-autonomy framing. `/goal` ≈ [[RalphLoop]]; the reliability/cost fixes are standard harness engineering.

## Related

- [[HarnessEngineering]] — where loop engineering belongs
- [[AgentHarness]] — the multi-session artifact
- [[RalphLoop]] — `/goal`-style loops
- [[Archon]] — deterministic-workflow answer to naive loops
- [[CrossProviderWorkflow]] — per-node model mixing for cost
- [[ParallelAgenticDevelopment]] — isolation for parallel loop workers
- [[ContextRot]] — the single-session-loop failure mode
- [[ClaudeCode]] — `/loop`, `/goal`, `/routines`
- [[Pi]], [[Retool]] — dashboard drive + deployment
- [[ColeMedin]] — articulator (skeptic)
- [[summary-20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!]] — primary source
