---
title: "WrenchBoard"
type: entity
tags: [hackathon, electronics-repair, claude-code, diagnostics, schematics]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Wrench Board is an AI-powered diagnostic tool for electronics repair, built by Alexis Chapellier. It helps independent technicians figure out complex repairs by ingesting schematics and boardviews, creating a unified electrical graph, reasoning over it, and guiding the technician to the exact pad to probe.

## Key Information

- **Creator**: Alexis Chapellier, a self-taught electronics repairer from Reignier-Ésery, France, who previously created RepairMind (an AI-powered management platform for repair shops).
- **How it works**: Users drop in a schematic and a boardview and describe the symptoms. The agent creates a unified electrical graph, reasons over it, points to the exact pad to probe, reads measurements, and updates its hypotheses until it diagnoses the issue.
- **Development approach**: Prototyped in [[ClaudeDesign]], separating the app's responsibilities (design, schematic ingestion, boardview, diagnostic agent) and producing first a spec and then a plan for each one. Executed in Claude Code's multi-agent mode, benchmarking at every step by running five or six agents in parallel during debugging, with one dedicated agent per domain.
- **Key capability**: Relies on Opus 4.7's ability to understand visual schematics. Alexis knew it was working when he asked the model to trace a power path on a motherboard and watched the boardview light up step by step.
- **Next phase**: Building a community of electronics repairers and experts to enrich the tool with field experience.
- **URL**: [wrenchboard.cloud](https://wrenchboard.cloud/)

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[ClaudeDesign]] — used for prototyping and planning
- [[Claude4.7Opus]] — model providing visual schematic understanding
- [[Superpowers]] — skills framework used for structured brainstorming
