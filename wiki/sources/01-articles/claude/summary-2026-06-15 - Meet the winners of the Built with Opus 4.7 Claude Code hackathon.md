---
title: "summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon"
type: source
tags: [source, claude-blog, hackathon]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic profiles six winning projects from its "Built with Opus 4.7" virtual hackathon, demonstrating how Claude Code enables builders from diverse backgrounds -- including a physician, a self-taught electronics repairer, a CS educator in Chile, a full-stack developer, a carpenter's son with no programming experience, and two industrial engineers -- to ship ambitious, production-quality software in just five days. The projects span medical training (Medkit), electronics repair (Wrench Board), computer science education (Maieutic), interactive play (Virtual Puppet Theater), home repair (MaestrIA), and factory maintenance (ARIA). Common themes include spec-first planning, evaluation-driven development, using Claude as a thought partner rather than just a code generator, and the collapsing barrier between having an idea and shipping it.

## Key Points

- Medkit, built by Bedirhan Keskin, is a gamified medical training tool using Claude Managed Agents to simulate patient encounters; already gaining traction with three medical faculties and a pharma company in Istanbul.
- Wrench Board, built by self-taught repairer Alexis Chapellier, uses Opus 4.7's visual schematic understanding to create unified electrical graphs from schematics and boardviews, diagnosing electronics issues step-by-step.
- Maieutic, built by CS educator Paula Vásquez-Henríquez, is an IDE designed to make students slow down -- requiring plain-language specs before coding, locking autocomplete, and using Intent-Diff Review to compare specs against code.
- Virtual Puppet Theater, built by Rene Hangstrup Møller, uses Opus 4.7's spatial reasoning with MediaPipe hand tracking and Three.js to create real-time interactive puppet shows from webcam input.
- MaestrIA, built by Benjamin Torralbo (no prior programming experience), provides home repair diagnostics by injecting a JSON file of 17 diagnostic rules distilled from his master carpenter father's 30 years of experience.
- ARIA (Adaptive Runtime Intelligence), winning Best Use of Claude Managed Agents, uses five agents to continuously monitor factory machines, generating custom diagnostics and repair plans from manufacturer PDFs and live signals.
- Builders consistently emphasized planning before coding (Paula spent two days on specs), evaluation-driven development (Benjamin's 9-dimension eval was the "first commit"), and treating Claude as a thought partner rather than just a code generator.
- Claude Managed Agents handled infrastructure (sandboxed execution, session persistence, MCP dispatching) so builders could focus on product, with ARIA's team noting it was "the difference between shipping in five days and shipping in five weeks."

## Related

- [[Claude4.7Opus]] -- the model used across all projects
- [[ClaudeCode]] -- the primary development environment
- [[ClaudeManagedAgents]] -- infrastructure for agent-based projects
- [[ClaudeDesign]] -- used for brainstorming and planning phases
- [[Superpowers]] -- skills framework used by Alexis for structured brainstorming
- [[Medkit]] -- medical training simulation tool
- [[WrenchBoard]] -- electronics repair diagnostic tool
- [[Maieutic]] -- CS education IDE
- [[VirtualPuppetTheater]] -- interactive puppet show app
- [[MaestrIA]] -- home repair diagnostic app
- [[ARIA]] -- industrial maintenance AI system
