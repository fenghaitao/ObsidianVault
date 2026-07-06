---
title: "Diode Computers"
type: entity
tags: [company, electrical-engineering, pcb-design, ai-partnership]
sources: ["raw/01-articles/claude/2025-12-12 - Making Claude a better electrical engineer.md"]
last_updated: 2026-07-04
---

## Definition

Diode Computers designs and manufactures custom circuit boards with AI, turning PCB (printed circuit board) design into a software problem the way Claude Code turns software engineering into an agentic task.

## Key Information

- Develops **Zener**, a Starlark-based domain-specific language for describing PCB schematics, and **pcb**, which uses Zener to automate on top of KiCad.
- Electrical engineers use [[ClaudeCode]] to auto-generate PCB reference designs in Zener from unstructured chip documentation, ready to fab in hours.
- Partnered with [[Anthropic]] to train reference-design generation improvements into Claude Sonnet 4.5 and later models, using a custom testbench grading higher-level component requirements rather than brittle exact-value assertions.
- In a blind evaluation, Diode's electrical engineers preferred Claude Sonnet 4.5's reference designs over Opus 4.1 and Sonnet 4 8 out of 10 times.

## Related

- [[ClaudeCode]] — the tool Diode's engineers use for reference-design generation
- [[Anthropic]] — partner on the training initiative
- [[summary-2025-12-12 - Making Claude a better electrical engineer]] — source article
