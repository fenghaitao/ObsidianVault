---
title: "ParallelAgenticDevelopment"
type: concept
tags: [concept, parallel, git-worktrees, claude-code, agentic-coding, scaling]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260423 - Parallel Claude Code + Git Worktrees： This Setup Will Change How You Ship.md"
last_updated: 2026-06-20
---

## Definition

Parallel agentic development is [[ColeMedin]]'s system for running **many coding-agent sessions simultaneously** (10x output, not 2x) without them overwriting each other's work. The core enabler is **git worktrees** (one isolated codebase copy per agent); the surrounding system makes each agent self-sustaining enough that the human doesn't become the bottleneck.

## Key Information

### The five pillars

1. **Issue is the spec** — a GitHub issue / Jira ticket is the *input to implementation*; the **pull request** is the *input to validation*. A fan-out: one session creates a batch of issues, then many agents implement them in parallel.
2. **Git worktrees** — each agent works in its own duplicated codebase. Native in [[ClaudeCode]] (`claude --worktree <name>` / `-w`, created under `.claude/worktrees/`); scriptable for agents without native support.
3. **Per-worktree plan / build / validate** — point each session at its issue; use whatever your normal process is ([[PIVLoop]], skills/commands, Spec Kit, BMAD). Each outputs a PR.
4. **Review in a fresh context window** — never review in the implementing session (bias — "a kid grading their own homework"; "the reviewer should never see the writer's chat"). A `/review-pr` command `/clear`s, data-mines the PR, compares to the issue, and spins specialized [[SubAgent]]s. Optional **cross-model** review via the Codex plugin ([[AdversarialDev]]-style, different blind spots).
5. **Self-healing layer** — fix the *system* that allowed a bug by evolving the [[AILayer]] ([[SystemEvolution]]); shrinks the human-bottleneck over time.

### The engineering problems (end-to-end parallel validation)

Static analysis isn't enough — agents must start the app and use it. Running many instances at once surfaces:

| Problem | Solution |
|---|---|
| **Port conflicts** | Startup command derives a **unique port from the worktree name** (base 4000 → 4161, 4107, …). |
| **Dependency installs** | Install `node_modules` up front per worktree (setup script). |
| **Database isolation** | A **[[Neon]] branch per worktree** (copies tables + data) — "a worktree for the database"; or **SQLite per worktree** (free/local). |
| **Token blowout** | Switch models (`/model`); cheap models (Haiku/Sonnet) for analysis/research/review; per-sub-agent model. |
| **PR pileup** | Reduce the human bottleneck; persistent fixing is the signal to invest in the self-healing layer. |

A `w.sh` / `w.ps1` script bundles worktree creation + dependency install + Neon branch, and works in any coding agent.

### Relationship to other patterns

- **vs [[AgentTeams]]** — Agent Teams is the in-tool parallelism, but Cole finds it "not very reliable" for true parallel dev; the worktree system is his preferred, more deterministic approach.
- **[[Archon]]** ships worktree/isolation support out of the box (Cole's open-source harness builder).
- Pillars 4–5 are really about *validation throughput* so the human can review many PRs without becoming the bottleneck.

## Related

- [[ClaudeCode]] — native worktrees, `/model`, Codex plugin review
- [[Neon]] — database branching for per-worktree DB isolation
- [[AgentTeams]] — the less-reliable in-tool alternative
- [[AdversarialDev]] — cross-model / fresh-context PR review
- [[SystemEvolution]] — the self-healing pillar
- [[SubAgent]] — used in review and analysis
- [[Archon]] — harness builder with worktree support
- [[PIVLoop]] — the per-worktree build process
- [[ColeMedin]] — articulator
- [[summary-parallel-claude-code-worktrees]] — primary source
