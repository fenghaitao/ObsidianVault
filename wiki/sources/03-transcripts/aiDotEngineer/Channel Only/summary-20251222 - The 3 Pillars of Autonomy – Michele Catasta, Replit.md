---
title: "summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit"
type: source
tags: [source, transcript, aiDotEngineer, autonomy, coding-agents, replit]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Core Summary
Michele Catasta, from Replit, presents the three pillars for building fully autonomous coding agents for non-technical users: frontier model capabilities, verification (autonomous testing to eliminate "painted doors"), and context management (via sub-agent orchestration and state offloading). He argues that true autonomy means the agent makes all technical decisions independently, decoupling autonomy from long runtimes, and that parallelism with the core loop as orchestrator is the next frontier for improving user experience.

## Key Points
- Autonomy should not be conflated with long runtimes; an autonomous agent can be fast when given a narrow scope.
- Replit targets a "Waymo experience" where non-technical users sit in the back seat with no access to the steering wheel, unlike the "Tesla FSD" supervised autonomy model.
- Over 30% of individual features built by agents are broken on first pass ("painted doors"), eroding user trust.
- Autonomous testing via Playwright code generation is an order of magnitude cheaper and faster than computer-use approaches, and creates reusable regression test suites.
- Context management through sub-agent orchestration improved Replit's memories-per-compression from ~35 to ~45-50, enabling long-horizon tasks within 200K token windows.
- The next evolution is the core loop as orchestrator for parallel agents, where task decomposition and parallelism are determined on the fly rather than by the user.

## Related
- [[MicheleCatasta]] — Speaker, Replit
- [[Replit]] — Company building autonomous coding agents
- [[Three Pillars of Autonomy]] — Framework for agent autonomy
- [[Autonomous Coding Agents]] — Category of AI coding tools
- [[Painted Doors]] — Broken features in agent-generated code
- [[Verification in Agentic Loops]] — Autonomous testing methodology
- [[Context Management]] — Techniques for managing agent context
- [[Sub-agent Orchestration]] — Pattern for agent architecture
- [[Parallel Agents]] — Running multiple agents concurrently
- [[Core Loop as Orchestrator]] — Architecture for parallel agent coordination
- [[Playwright]] — Browser automation library used for testing
- [[Browser-based Autonomous Testing]] — Testing methodology for web apps
