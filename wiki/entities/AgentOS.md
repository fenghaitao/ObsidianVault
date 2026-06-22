---
title: "AgentOS"
type: entity
tags: [tool, framework, standards, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260122 - Agent OS v3： Leaner & Smarter for Building in 2026.md]
last_updated: 2026-06-22
---

## Definition

Agent OS is Brian Casel's free open-source framework for defining and managing coding standards in AI-powered development. Version 3 (2026) was stripped down by 70% to focus on three gaps vanilla Claude Code doesn't address: discovering/documenting standards from legacy codebases, enhancing spec shaping, and maintaining profiles for different project types.

## Key Information

- Free and open-source at buildermethods.com/agent-os.
- Philosophy: don't reinvent what Claude Code already does well. Strip away overlaps, keep only gap-fillers.
- Three core features: (1) Discover Standards — analyzes codebase for unique patterns, interviews for reasoning, documents as concise standards; (2) Enhanced Spec Shaping — standards-aware clarifying questions during plan mode, saves plans to persistent spec folders; (3) Profiles — different standards sets for different project types.
- Standards indexed in YAML with one-line descriptions — agents read descriptions first, inject only relevant standards (progressive disclosure pattern).
- "Inject standards" command works anywhere: conversations, skill creation, spec planning.
- Standards vs Skills: standards are conventions applied differently per task; skills are process-oriented tasks run the same way.
- Integrates with Claude Code's native plan mode — enhances, doesn't replace.

## Related

- [[BrianCasel]] — creator
- [[SpecDrivenDevelopment]] — the methodology
- [[ClaudeCode]] — the execution surface
- [[ClaudeSkills]] — complementary concept
- [[ProgressiveDisclosure]] — the loading pattern
- [[DesignOS]] — companion framework for new projects
