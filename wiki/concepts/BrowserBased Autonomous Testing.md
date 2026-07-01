---
title: "Browser-based Autonomous Testing"
type: concept
tags: [testing, browser, agents, automation, quality-assurance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
Browser-based autonomous testing is a methodology where AI agents test web applications by interacting with them through a browser, either via computer use (screenshot-based interaction) or browser use (DOM-based programmatic interaction). Replit uses Playwright code generation as its primary approach.

## Key Information
- Two main categories: computer use (model directly interacts via screenshots, expensive and slow) and browser use (simulates UI, interacts via DOM abstractions).
- Tool-based browser use (e.g., Stagehand) provides generic tools (click, fill forms) but struggles with the long tail of idiosyncratic interactions.
- Replit's approach: generate Playwright code directly, which is more expressive, creates reusable regression tests, and is roughly an order of magnitude cheaper and faster than computer use.
- Replit uses a layered approach: programmatic interactions (database, logs, API calls, DOM clicks) as primary, with computer use as fallback via screenshots.
- Enables agents to gather all feedback autonomously, breaking the human feedback bottleneck.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Verification in Agentic Loops]] — parent concept
- [[Playwright]] — key tool
- [[Stagehand]] — alternative tool
- [[Computer Use]] — fallback approach
- [[Painted Doors]] — problem this solves
