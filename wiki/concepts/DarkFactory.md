---
title: "DarkFactory"
type: concept
tags: [concept, autonomy, dark-factory, orchestration, dan-shapiro]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260507 - AI YouTube Is Only Claude Hype Now.md"
last_updated: 2026-07-06
---

## Definition

The dark factory is Level 5 of [[AICodingAutonomyLevels]]: a fully autonomous software pipeline where a spec goes in and shipped, production code comes out, with **no human review step at all** — not even a "driver's seat" to grab control from if something goes wrong. It's the ceiling of AI-coding autonomy, and per [[ColeMedin]] the dream end-state for a mature harness, but also the riskiest, since a single bad assumption in the spec (or an agent stalling on a handoff) can propagate into many bad production deployments unnoticed.

## Key Information

### Required components

A dark factory isn't just "AI writes code" — it's a system with distinct agents/stages, each handling one part of the pipeline:

1. **Planning agent** — takes one task (split from the larger spec) and produces a structured plan artifact, same shape as the planning step in a normal [[PIVLoop]].
2. **Code-generation agent** — executes the plan, produces a pull request.
3. **Validation layer** — reviews the PR; kept in a *separate context* from the implementation step to avoid the bias of an agent reviewing its own work (see [[AdversarialDev]] for the same principle applied to human-supervised workflows).
4. **Deployment system** — ships to production autonomously, potentially runs regression tests; no human in the loop at this stage, unlike Level 4.
5. **Orchestration layer** — the highest-level agent: splits the spec into individual tasks, manages handoffs between the other agents, and prevents duplicate work or agents stalling while waiting on inputs that never arrive.

### Failure modes

Because there's no human catching problems, failures compound silently:
- **Cascading failures** — one bad assumption or wrong task split propagates through the rest of the pipeline.
- **Evaluation gaming** — agents optimizing for what their eval measures rather than the actual intent.
- **Stalled handoffs** — an agent waiting on an input from another agent that crashed or never produced it.

### Deterministic vs. agentic nodes

Not every stage needs LLM reasoning. Formatting code, running a linter, or triggering a deployment can be handled with plain deterministic code rather than an agent call — see [[DeterministicVsAgenticNodes]]. [[Stripe]]'s "Stripe Minions" system is cited as an example of mixing both node types deliberately.

### Real-world status

Reports of production dark factories are mostly rumor-level; [[StrongDM]] is cited as one company that reportedly runs one successfully, even for banking-grade code. Cole ran his own "Dark Factory experiment" live on stream using [[Archon]] — a codebase handed entirely to AI agents with no human allowed to review or write code — describing it as a real but still-rough attempt, with "a million things" still needed to make it truly reliable.

### Relationship to earning autonomy

Per [[ColeMedin]], you don't design a dark factory from scratch — you earn your way to it by operating reliably at Level 3 ([[AICodingAutonomyLevels]]) for long enough that [[SystemEvolution]] has hardened the [[AILayer]], then layering the orchestration system on top as its own additional engineering effort.

## Related

- [[AICodingAutonomyLevels]] — the five-level framework Dark Factory is the ceiling of
- [[DeterministicVsAgenticNodes]] — the code-vs-LLM mix inside a dark factory pipeline
- [[SystemEvolution]] — the mechanism by which a harness earns the trust needed for Level 5
- [[AgentOrchestration]] — the general pattern the orchestration layer is a specific application of
- [[StrongDM]] — cited production example
- [[Stripe]] — deterministic/agentic node example ("Stripe Minions")
- [[Archon]] — Cole's own Dark Factory experiment tooling
- [[DanShapiro]] — framework author
- [[ColeMedin]] — analyst; ran his own Dark Factory experiment
- [[summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)]] — primary source
- [[summary-20260507 - AI YouTube Is Only Claude Hype Now]] — Cole's own Dark Factory experiment, first mentioned
