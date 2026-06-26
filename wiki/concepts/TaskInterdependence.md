---
title: "TaskInterdependence"
type: concept
tags: [developer-productivity, ai, delegation, context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md"]
last_updated: 2026-06-25
---

## Definition
Task Interdependence is the principle that when subtasks depend on each other's outputs and context, delegating individual subtasks to AI may not save time because the human must maintain context across all subtasks to complete the overall task reliably.

## Key Information
- If AI can complete subtask A but not subtask B, it may still not make sense to delegate A because the human needs to know how A was completed to reliably complete B
- Developers need to maintain context as they work through interdependent subtasks
- This is one hypothesis for why AI tools didn't speed up developers in METR's RCT: delegating parts of a complex issue breaks the developer's mental model
- Contrasts with benchmark tasks that are typically isolated and self-contained

## Related
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[RandomizedControlledTrial]] — study where task interdependence was observed
- [[Context Management]] — related concept for maintaining coherence
- [[AIReliability]] — compounding factor: unreliable AI on interdependent tasks is especially costly
