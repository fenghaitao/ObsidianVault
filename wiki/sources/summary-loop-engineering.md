---
title: "summary-loop-engineering"
type: source
tags: [source, original-material, loop-engineering, harness, archon, autonomy]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!.md"]
last_updated: 2026-06-21
---

## Core Summary

[[ColeMedin]] gives a skeptical-but-practical take on **"loop engineering"** — the emerging buzzword (from Boris Cherny of [[ClaudeCode]]: "I don't prompt Claude anymore, I write loops"; and Peter Steinberger of [[OpenClaw]]) where you design loops that prompt agents 24/7 instead of prompting manually. Cole's verdict: there are good ideas, but it's overhyped, **token-hungry**, and unreliable without a tight system — so **fold it into [[HarnessEngineering]]**, it "doesn't deserve its own buzzword." He then shows how he extracts the good parts with [[Archon]] and an experimental loop dashboard.

## Key Points

- **What loop engineering is** (simple at core): an orchestrator agent you minimally prompt sets up loops via a "loop skill." Claude Code primitives:
  - **`/loop`** — run a prompt on an interval (e.g. every 5 min: check for new GitHub issues and handle them) while the terminal stays open.
  - **`/goal`** — define done-criteria and force the agent to work until met (akin to a [[RalphLoop]]).
  - **`/routines`** — scheduled jobs (e.g. hourly: wake up, read a spec, do the next task).
- **Three downsides**:
  1. **Not the best results** — Boris's claim of "tens of thousands of agents" (via "Daisy") is hyperbole/impractical; great for POCs/exploration, not Cole's primary driver.
  2. **Cost** — the orchestrator reasons, spins up workers, prompts them, re-reasons on results, dispatches the next wave; lots of context-passing. A simple app cost **1M+ tokens** in one run.
  3. **Single-session bloat** — `/loop` in Claude Code keeps looping *in the same session* → [[ContextRot]]. You need work distributed across sessions that communicate.
- **Cole's fixes via [[Archon]]** (loop engineering done right):
  - **Deterministic workflows** — take decisions *away* from the agent except where reasoning is truly needed (let it write code, but don't let it decide which tests pass). Workflow file enforces process; e.g. `fix-github-issue` extracts issue → classifies bug-vs-feature (dynamic) → research → implement → validate → PR.
  - **Session-per-step + handoff docs** (not one bloated `/loop` session).
  - **Per-node model selection / mix providers** — cheap models (Haiku, MiniMax M3, Kimi K2.7) for classify/explore; Claude Code to implement; Codex to review. (Single-model-for-everything is part of why naive loops are so expensive.)
  - **Durability** — runs/logs in [[Neon]] Postgres; resume a workflow after a crash/cancel from the exact step.
  - **Parallelism + isolation** — fix many GitHub issues at once with git worktrees + Neon DB branches + port handling (see [[ParallelAgenticDevelopment]]); add **[[HumanInTheLoop]]** nodes so it pauses for review instead of running for a day and returning "crap."
- **Experimental loop dashboard** (open-source): orchestrator reads external **state in a DB** → dispatches workers → workers update state → repeat; durability via Neon; cost/decision **observability**; driven by **[[Pi]]** on Kimi K2.7 (cheap, elevated by the harness); HITL between rounds. Deployable to the cloud via **[[Retool]]** (React import, Neon connection, permission groups / audit trails, approve-and-resume).
- **Bottom line**: loop engineering is real and promising for autonomy, but only with durability, observability, deterministic process, cost control (mixed providers), and human-in-the-loop — i.e. it's just [[HarnessEngineering]].

## Related

- [[LoopEngineering]] — the concept this video defines (and deflates)
- [[HarnessEngineering]] — what loop engineering folds into
- [[Archon]] — Cole's deterministic-workflow answer
- [[RalphLoop]] — `/goal` is a Ralph-style loop
- [[ClaudeCode]] — `/loop`, `/goal`, `/routines`, loop skill
- [[Pi]] — drives the dashboard loop on Kimi K2.7
- [[Retool]] — deploy the control dashboard to the cloud
- [[ContextRot]] — the single-session-loop failure mode
