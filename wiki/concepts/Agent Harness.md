---
title: "Agent Harness"
type: concept
tags: [agentic-engineering, harness-engineering, agent-architecture, workos, case]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

An agent harness is a structured system that wraps AI coding agents with deterministic enforcement, verification gates, and self-improvement mechanisms. The harness, not the agent's prompts, controls the workflow — ensuring agents prove their work rather than claim it.

## Key Information

- Nick Nisi's Case is a concrete example: built on Pi with a TypeScript state machine, five specialized agents, and mandatory verification gates
- Key distinction from prompt-based systems: the harness uses code (not prompts) to enforce behavior. The AI model cannot decide to skip steps
- Core components of a harness:
  - Multiple specialized agents (implementer, verifier, reviewer, closer, retro)
  - State machine gates that enforce sequence and prevent skipping
  - Evidence-based verification at each stage (cryptographic hashes, video evidence)
  - Memory system that learns from failures and improves over time
  - Retrospective analysis that identifies patterns and updates memory
- Philosophy: when the agent fails, fix the harness, not the code. Every failure is a bug in the harness
- Contrast with skills-based approaches: harnesses enforce; skills suggest
- Nick's workflow: he hasn't written code in ~8 months — he scales work by improving the harness and reviewing agent output
- "Your job was never really about writing code. It was always about building these systems, and now we just have a better abstraction to understand that"

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — built Case as a harness
- [[Case]] — concrete harness implementation
- [[Harness Engineering]] — the broader discipline
- [[AgentHarness]] — related concept from Ryan Lopopolo
- [[State Machine Gates]] — the enforcement mechanism
- [[Evidence-Based Verification]] — the proof mechanism
- [[Retrospective Agent]] — the self-improvement mechanism
- [[Enforce Dont Instruct]] — the guiding principle
- [[Pi (coding agent)]] — the underlying agent harness Case is built on
