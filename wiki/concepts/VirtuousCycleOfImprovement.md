---
title: "VirtuousCycleOfImprovement"
type: concept
tags: [methodology, improvement, evals, data, cycle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
The Virtuous Cycle of Improvement is the specific feedback loop for LLM applications where evals define objectives, data collection captures real user interactions, and improvements from that data feed back into better evals. It was the central framework of the 2024 AI Engineer Summit keynote, represented visually as a cycle with evals and data at the center.

## Key Information
- Central diagram of the keynote, credited to co-author Hamel Hussein
- The cycle: evals define what the system should do → data is collected from production → data analysis reveals gaps → improvements are made → evals are refined
- Evals are not "convenient weird bespoke metrics" — they are objectives, expressions of what we want our system to do
- The core reason to create evals and collect data is to drive this loop forward
- This loop is the through-line connecting all three sections of the keynote: strategic (why), operational (how to organize teams), and tactical (specific techniques)
- Has deep historical roots: Toyota's Kaizen → Lean Startup Build-Measure-Learn → DevOps monitoring → MLOps iteration → LLM virtuous cycle
- The warning: don't get lost in building the loop infrastructure without "bending metal" (delivering actual user value)

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[ContinuousImprovement]] — the broader concept this operationalizes
- [[DataFlywheel]] — the same concept from a data-centric perspective
- [[HamelHussein]] — created the diagram and presented the framework
- [[EvalEngineering]] — the practice of building the evals that anchor the cycle
- [[ToyotaProductionSystem]] — historical origin of the cycle concept
