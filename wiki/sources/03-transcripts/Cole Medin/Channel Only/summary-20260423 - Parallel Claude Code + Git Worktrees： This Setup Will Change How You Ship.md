---
title: "summary-20260423 - Parallel Claude Code + Git Worktrees： This Setup Will Change How You Ship"
type: source
tags: [source, original-material, parallel-agents, git-worktrees, claude-code, neon]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260423 - Parallel Claude Code + Git Worktrees： This Setup Will Change How You Ship.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] lays out a playbook for **[[ParallelAgenticDevelopment|parallel agentic development]]** — running many [[ClaudeCode]] sessions at once to 10x output — built around **git worktrees** for isolation. He frames it as **five pillars** (issue-as-spec, worktrees, per-worktree plan/build/validate, fresh-context PR review, self-healing) plus the **real engineering problems** that block end-to-end parallel validation (port conflicts, dependency installs, database isolation, token blowout, PR pileup). His [[Archon]] harness builder ships much of this out of the box.

## Key Points

- **Why parallel**: spinning up 5 agents without a system means they "step on each other's toes" (overwrite changes). The fix centers on **git worktrees** — each agent gets its own local copy of the codebase. ("10x is easier than 2x" — forces you to build a self-sustaining system.) Claude **Agent Teams** is "not very reliable" for true parallel dev; the worktree system is Cole's preferred approach.
- **Pillar 1 — Issue is the spec**: a GitHub issue (or Jira ticket) is the *input to implementation*; the **pull request** is the *input to validation*. Fan-out pattern: one session creates a batch of issues → many agents implement in parallel.
- **Pillar 2 — Git worktrees**: native in Claude Code (`claude --worktree <name>` / `-w`; creates `.claude/worktrees/<name>/` with a duplicated codebase). For agents without native support, a script creates them.
- **Pillar 3 — Plan/build/validate per worktree**: point each session at its issue ("use the GitHub CLI to view issue N and plan it") using whatever your usual process is (skills/commands, Spec Kit, BMAD). Output = a PR.
- **Pillar 4 — Review in a fresh context window**: never let an agent review its own work in the implementing session (bias — "a kid grading their own homework"); "the reviewer should never see the writer's chat." A `/review-pr` command `/clear`s context, data-mines the PR, compares it to the issue, and spins specialized sub-agents. **Cross-model review**: the **Codex plugin for Claude Code** + a `/codex-adversarial-review` command runs Codex over Claude's branch in a separate session (different blind spots). Compare issue↔PR to catch plan→implementation deviation.
- **Pillar 5 — Self-healing layer**: when a bug appears, fix the *system* that allowed it — evolve the [[AILayer]] (rules/skills/workflows). This is [[SystemEvolution]]; reduces the human-bottleneck over time.
- **Engineering problems for end-to-end parallel validation** (in his linked repo as a reference to point your agent at):
  - **Port conflicts** — a startup command derives a **unique port from the worktree name** (base 4000 → e.g. 4161, 4107) so all instances run simultaneously.
  - **Dependency installs** — install `node_modules` up front per worktree (script) so the agent stays focused and runs faster.
  - **Database isolation** — a **[[Neon]] branch per worktree** (copies tables + data from main) gives "a worktree for the database," so parallel agents don't corrupt prod or each other; **SQLite-per-worktree** is the free/local alternative. A `w.sh`/`w.ps1` setup script creates the worktree + Neon branch (works in any coding agent).
  - **Token blowout** — switch models (`/model`) for cheap tasks (Haiku/Sonnet for analysis/research/review), and assign cheaper models per sub-agent/skill.
  - **PR pileup** — reduce the human bottleneck; if you're spending lots of time fixing, that's the signal to invest in the self-healing layer.

## Related

- [[ParallelAgenticDevelopment]] — the five-pillar system this defines
- [[ClaudeCode]] — native worktrees, `/model`, Codex plugin
- [[Neon]] — database branching per worktree
- [[AgentTeams]] — the less-reliable in-tool alternative to this system
- [[AdversarialDev]] — cross-model PR review in separate sessions
- [[SystemEvolution]] — pillar 5, the self-healing layer
- [[Archon]] — Cole's harness builder that ships worktree/isolation support
