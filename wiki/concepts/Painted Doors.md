---
title: "Painted Doors"
type: concept
tags: [testing, agents, quality, bugs]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
"Painted doors" is a term used by Replit to describe features in agent-generated code that appear complete and functional on the surface but are actually broken — for example, buttons without event handlers, or mock data displayed instead of real database data. They erode user trust in coding agents.

## Key Information
- Replit's internal evaluations found over 30% of individual features are broken on first pass.
- Nearly every application built by an agent has at least one broken feature or painted door.
- They are hard for users to find because users don't systematically test every button and field.
- Particularly damaging for non-technical users who are "shocked" when they discover broken functionality.
- Solved through autonomous testing (verification in the agentic loop) using Playwright-based browser testing.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Verification in Agentic Loops]] — solution
- [[Autonomous Coding Agents]] — context
- [[Browser-based Autonomous Testing]] — detection method
