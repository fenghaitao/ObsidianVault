---
title: "Browser Use"
type: concept
tags: [testing, browser, agents, automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
Browser use is a testing approach where an agent simulates the user interface and interacts with a web application through DOM abstractions, as opposed to computer use which relies on screenshots. It is a middle-ground approach between full computer use and programmatic testing.

## Key Information
- Simulates the user interface rather than directly rendering and screenshotting it.
- Relies on accessing the DOM through abstractions.
- Tool-based implementations (e.g., Stagehand) expose generic tools like create tab, click, fill forms.
- Limitation: difficult to enumerate all interaction types; the generic tool set covers ~99% of cases but misses idiosyncratic interactions.
- Replit chose to go beyond this approach by generating Playwright code directly for more expressiveness and reusability.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[BrowserBased Autonomous Testing]] — parent concept
- [[Computer Use]] — alternative approach
- [[Stagehand]] — example tool
- [[Playwright]] — more expressive alternative
