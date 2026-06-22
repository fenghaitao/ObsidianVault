---
title: "ClaudeDesign"
type: entity
tags: [tool, design, anthropic, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260424 - Where Claude Design actually fits.md]
last_updated: 2026-06-22
---

## Definition

Claude Design is Anthropic's visual design tool that runs Claude Code under the hood in a visual canvas interface. It supports high-fidelity mockups, animations, slide decks, and design systems. Brian Casel evaluates it as useful for marketing assets and visual ideation, but not as an idea-to-ship tool or design layer for existing codebases.

## Key Information

- Runs Claude Code under the hood in a visual harness with a large canvas.
- Supports: high-fidelity mockups, animations, slide decks (with speaker notes and presentation mode), design systems.
- "Tweaks" feature: toggle design options (fonts, colors) dynamically — but may embed tweaking logic into exported code.
- Export options: PDF, Canva, standalone HTML, handoff to Claude Code (via URL link).
- Design systems can be created from descriptions or by analyzing a GitHub repo.
- Brian's verdict: not for production app design (handoff is disjointed — no spec, no plan, no tech stack context). Good for: (1) visual ideation during shaping phase, (2) on-brand marketing assets (animations, slide decks).
- For production design, Brian prefers a living design system in the codebase via [[DesignSystem]] and CLAUDE.md.

## Related

- [[BrianCasel]] — evaluator
- [[Anthropic]] — creator
- [[ClaudeCode]] — the engine underneath
- [[DesignSystem]] — Brian's preferred approach for production
- [[DesignDrift]] — the problem design systems solve
- [[VisualIdeation]] — the valid use case
