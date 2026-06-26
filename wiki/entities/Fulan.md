---
title: "Fulan"
type: entity
tags: [tool, ai, personal-ai, read-only]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md"]
last_updated: 2026-06-26
---

## Definition
Fulan is a read-only personal AI system built by Šimon Podhajský that ingests six data sources with read access only, analyzes cognitive exhaust fumes, and outputs insights to a separate Obsidian vault for human review.

## Key Information
- Built by Šimon Podhajský, Head of AI at Waypoint
- Three-zone architecture: read-only sources, analysis workspace, separate output vault
- Six read-only data sources: email, journal, browser history, task manager, CRM, and others
- The AI never writes back to source systems — all outputs go to a separate Obsidian vault (or any separate system)
- Powers a weekly reflection feature inspired by David Allen's Getting Things Done methodology
- Uses Claude skills, Python scripts, and the Anthropic API for structured output generation
- Cross-source queries combine data from Vivaldi browser (SQLite reading history) and Clay CRM (contacts) to suggest discussion partners
- Runs within Claude Code with auto-mode or dangerous disk permissions for bash operations

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[ŠimonPodhajský]] — creator
- [[Waypoint]] — company
- [[ReadOnlyAI]] — design philosophy
- [[CognitiveExhaustFumes]] — concept the system analyzes
- [[CrossSourceSignal]] — core value proposition
