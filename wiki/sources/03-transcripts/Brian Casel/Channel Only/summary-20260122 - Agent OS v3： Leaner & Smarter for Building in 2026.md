---
title: "summary-20260122 - Agent OS v3： Leaner & Smarter for Building in 2026"
type: source
tags: [source, brian-casel, agent-os, standards, spec-driven-development]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260122 - Agent OS v3： Leaner & Smarter for Building in 2026.md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel releases Agent OS v3, stripped down by 70% from previous versions. The philosophy: don't reinvent what Claude Code already does well. Agent OS now focuses on three gaps: discovering and documenting coding standards from legacy codebases, enhancing spec shaping with standards-aware questions, and maintaining profiles for different project types. It integrates with Claude Code's native plan mode rather than replacing it.

## Key Points

- Agent OS v3 reduced footprint by 70% — removed everything that overlaps with Claude Code's native features.
- Three core features: (1) Discover Standards — analyzes codebase for unique/opinionated patterns, interviews you for reasoning, documents as concise standards; (2) Enhanced Spec Shaping — standards-aware clarifying questions during plan mode, saves plans to persistent spec folders; (3) Profiles — different standards sets for different project types (Laravel, marketing site, internal tools).
- Standards are indexed in YAML with one-line descriptions — agents read descriptions first, then inject only relevant standards (similar to Claude Skills progressive disclosure).
- "Inject standards" command works anywhere: during conversations, skill creation, or spec planning.
- Standards vs Skills: standards are conventions/patterns applied differently per task; skills are process-oriented tasks run the same way every time.
- For legacy codebases: Agent OS surfaces undocumented patterns so agents understand the "why" behind the code.
- Free and open-source at buildermethods.com/agent-os.

## Related

- [[BrianCasel]] — creator
- [[AgentOS]] — the framework
- [[SpecDrivenDevelopment]] — the methodology
- [[ClaudeCode]] — the execution surface
- [[ClaudeSkills]] — the complementary concept
- [[ProgressiveDisclosure]] — the loading pattern
