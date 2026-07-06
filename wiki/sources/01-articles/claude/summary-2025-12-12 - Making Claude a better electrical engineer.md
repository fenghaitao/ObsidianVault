---
title: "summary-2025-12-12 - Making Claude a better electrical engineer"
type: source
tags: [source, electrical-engineering, domain-partnership, model-training]
sources: ["raw/01-articles/claude/2025-12-12 - Making Claude a better electrical engineer.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic partnered with [[DiodeComputers|Diode Computers]] to improve Claude's ability to auto-generate printed circuit board (PCB) reference designs in Diode's Zener language, training measurable gains into Claude Sonnet 4.5 and later models — a template for how Anthropic collaborates with domain experts on specialized, agentic tasks with clear success/failure criteria.

## Key Points

- **The task**: reference designs — the ancillary components (resistors, capacitors, inductors) a chip needs to operate — traditionally require synthesizing hundreds of pages of sparse documentation; [[ClaudeCode]] is already used to auto-generate these in Zener (Diode's Starlark-based PCB description language) before human review, but the novel domain-specific environment left room for improvement.
- **Agentic setup**: Claude is given chip documentation as input, plus tools to read/write files and run bash commands, the Zener compiler, language docs, and a few examples — nothing else — and must produce a full configurable schematic expressing all operating modes.
- **Grading via testbench**: instead of brittle absolute assertions ("a 20uF capacitor between power and ground"), a custom testbench encodes higher-level requirements ("at least 22uF of capacitance"), giving an accurate but not overly restrictive success signal.
- **Results**: in a blind head-to-head evaluation across Claude Opus 4.1, Sonnet 4, and Sonnet 4.5, Diode's electrical engineers preferred Sonnet 4.5's reference designs 8 out of 10 times, crediting better pickup of documentation nuances and better adherence to Diode's toolchain conventions.
- **Generalizable model**: improvements are trained into publicly released Claude models, benefiting all users (Claude Code, claude.ai, custom Claude-powered systems) — Anthropic frames any domain with clear agentic success/failure criteria and deep subject-matter expertise as a candidate for this kind of partnership.
- Written with Diode Computers (Davide Asnaghi, Lenny Khazan) and Anthropic (Connor Jennings, David Hershey, Nicholas Marwell).

## Related

- [[DiodeComputers]] — Anthropic's partner in this initiative
- [[ClaudeCode]] — the tool electrical engineers use to generate reference designs
