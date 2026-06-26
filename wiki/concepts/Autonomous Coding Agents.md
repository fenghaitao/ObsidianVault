---
title: "Autonomous Coding Agents"
type: concept
tags: [ai, coding, agents, autonomy, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
Autonomous coding agents are AI systems that can independently write, test, and deploy software with minimal human intervention. Replit's approach targets a "Waymo experience" where non-technical users can create software without making technical decisions, as opposed to the "Tesla FSD" model of supervised autonomy.

## Key Information
- Evolved through generations: completions/assistance → React-based agents → native tool calling agents → autonomous agents (capable of 1+ hour tasks).
- Key challenge: non-technical users cannot provide the technical feedback agents need to make progress.
- Over 30% of individual features built by agents are broken on first pass ("painted doors").
- True autonomy means the agent makes all technical decisions independently; it should not be conflated with long runtimes.
- Autonomy can be scoped: narrow tasks can be completed autonomously and quickly; broad tasks may take hours.
- The goal is to maximize "reducible runtime" — the span where the user doesn't need to make technical decisions.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Three Pillars of Autonomy]] — design framework
- [[Replit Agent]] — example product
- [[Painted Doors]] — common failure mode
- [[Verification in Agentic Loops]] — key enabler
