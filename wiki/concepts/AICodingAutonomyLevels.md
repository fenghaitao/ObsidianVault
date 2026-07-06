---
title: "AICodingAutonomyLevels"
type: concept
tags: [concept, autonomy, dan-shapiro, harness-engineering, dark-factory]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why).md"
last_updated: 2026-07-06
---

## Definition

A five-level framework, authored by [[DanShapiro]] and popularized by [[ColeMedin]], mapping how much an engineer delegates to an AI coding assistant onto the SAE five-levels-of-vehicle-automation analogy (a company created this driving-automation scale in 2013). Each level trades hands-on-keyboard control for autonomy, and — per Cole — the "best" level isn't the most autonomous one; it's the one your system (harness) can currently support reliably.

## Key Information

### The five levels

| Level | Name | Car analogy | What the agent does |
|---|---|---|---|
| 0 | Spicy autocomplete | Fully manual driving | Reference/search tool only; never writes a line that ships without you typing it yourself |
| 1 | Coding intern | Cruise control | Writes boilerplate: repo setup, package installs, unit tests, simple refactors |
| 2 | Junior developer | Highway autopilot | Handles some tasks autonomously (pair-programming), but not trusted broadly — most engineers are here by default |
| 3 | Developer | Waymo with a safety driver | All coding delegated to the agent; human still owns planning and final validation ([[ColeMedin]]'s recommended sweet spot) |
| 4 | Engineering team | — | Larger units of work (an epic/PRD/spec) delegated; human sets high-level direction up front and validates a batch of PRs at the end; reliability starts to tank without a mature system |
| 5 | Dark factory | Spaceship with no driver's wheel | Spec in, shipped code out; no human review before production — see [[DarkFactory]] |

### Level 3 as the sweet spot

Cole has operated at Level 3 for over a year (he reports not having written a line of code himself in that time). The key insight: full coding delegation is safe *because* it's sandwiched between human-led planning and human-led validation, not because the agent is fully trusted end-to-end. This is the same idea underlying his [[PIVLoop]] (extended to "R-PIV" — Research-Plan-Implement-Validate — in this video).

### Why not jump straight to Level 4/5

Reliability at Levels 4–5 depends entirely on having a proven, trustworthy [[AILayer]]/harness first — one that's been refined through repeated [[SystemEvolution]] cycles at Level 3. Skipping ahead without that foundation is what tanks reliability. Cole's advice: stay at Level 3 long enough to build the muscle and the system, then graduate levels only as your system demonstrably earns the trust.

## Related

- [[DarkFactory]] — Level 5 in depth
- [[ConductorVsOrchestrator]] — Google's parallel two-mode framing of the same underlying spectrum
- [[PIVLoop]] — the loop that operates Level 3; extended here to R-PIV
- [[HarnessEngineering]] — the system that determines which level is safe to operate at
- [[SystemEvolution]] — the mechanism for graduating levels over time
- [[DanShapiro]] — framework author
- [[ColeMedin]] — popularizer/analyst
- [[summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)]] — primary source
