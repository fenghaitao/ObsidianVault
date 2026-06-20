---
title: "AgentTeams"
type: concept
tags: [concept, claude-code, multi-agent, parallel, orchestration, anthropic]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"
last_updated: 2026-06-20
---

## Definition

Agent Teams is an experimental [[ClaudeCode]] feature (released with **Opus 4.6**, early 2026) in which a **lead agent** spawns multiple teammate agents that work in parallel **and communicate with each other** over a shared task list. It is the natural escalation of [[SubAgent]]s — the same parallelism, plus inter-agent coordination — and [[ColeMedin]] frames it as a strong signal of where [[AgenticEngineering]] is heading (likely the norm within ~6 months).

## Key Information

### The distinction from [[SubAgent]]s

| | Sub-agents | Agent Teams |
|---|---|---|
| Parallel execution | Yes | Yes |
| Communication | **None** — each reports back to the main agent only | **Teammate↔teammate and teammate↔lead** messaging |
| Coordination | Main agent aggregates results | Shared task list; agents claim tasks and negotiate ("you take these, I'll take those") |

This communication is the whole point — a fleet that coordinates without the human facilitating it.

### Downsides (as of early 2026)

- **Non-deterministic** — you hand a lot of control to the lead agent to figure out coordination, losing predictability.
- **Token-heavy** — communication + shared-task-list management add overhead (though Cole found it less extreme than its reputation: ~16% of a session limit for a full feature build).
- **No observability** — there's no dashboard showing which agent claimed which task or what messages were sent. You can only *ask* the lead "how have the agents been communicating?" and get decent meta-reasoning. Cole expects Anthropic to add observability (possibly buildable with hooks).
- **Experimental/unreliable** — not yet ready for production-grade software on its own.

### The contract-first pattern (making it work)

Claude Code by itself uses Agent Teams poorly because parallel work has **blockers** (e.g. the database schema must exist before the backend agent can do anything). Cole's `build with agent team` command imposes a **contract-first approach**:

1. The lead agent first defines the **contracts** between front-end, back-end, and database (interfaces, schemas, API shapes).
2. Those contracts are passed into each teammate's prompt.
3. Only *then* are the agents spawned in parallel — so they can work simultaneously without stepping on each other.

The command takes a structured-plan path plus an optional agent count (omit it to let Claude Code decide based on the plan).

### Operational setup

- Enable via `.claude/settings.local.json` (`experimental agent team = 1`).
- Run inside **tmux**; on Windows use **WSL** (Agent Teams / sub-agents don't run well natively). Not supported in [[Kiro]].
- Cole pairs the team (implementation) with autonomous end-to-end validation by the lead agent via the [[VercelAgentBrowser]] CLI.

## Related

- [[SubAgent]] — the predecessor; Agent Teams adds communication
- [[ClaudeCode]] — the host
- [[AgenticEngineering]] — the discipline this points toward
- [[AgentHarness]] — related multi-agent orchestration (Agent Teams is the in-tool version)
- [[VercelAgentBrowser]] — validation paired with team builds
- [[ColeMedin]] — articulator
- [[summary-agent-teams-live-build]] — primary source
