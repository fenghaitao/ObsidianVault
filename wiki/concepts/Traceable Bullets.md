---
title: "Traceable Bullets"
type: concept
tags: [ai, software-engineering, feedback, vertical-slices, pragmatic-programmer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Traceable Bullets is a concept from The Pragmatic Programmer (Hunt & Thomas) that Matt Pocock applies to AI coding. It refers to building thin vertical slices of functionality that cross all layers of a system, providing immediate integrated feedback — like tracer rounds that show where you're aiming in the dark.

## Key Information
- Origin: anti-aircraft gunners at night. Normal bullets are invisible; traceable bullets have phosphorescence so every sixth round shows a visible line in the sky, providing feedback on aim
- In software: instead of building layer by layer (horizontal), build thin slices that go through all layers, giving feedback on the entire flow
- AI loves to code horizontally: phase 1 = database/schema, phase 2 = API, phase 3 = frontend. This delays feedback until phase 3
- Vertical slices mean each issue produces something reviewable and testable end-to-end
- Without traceable bullets, AI is "coding blind" until it reaches later phases
- The concept transforms the way Pocock thinks about getting AI to pick its own tasks
- Each vertical slice should include: some schema changes, some service creation, and a minimal frontend representation
- Example: "Award points for lesson completion visible on dashboard" is a good vertical slice because it crosses database, service, and UI layers

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — applies the concept to AI coding
- [[Vertical Slices]] — the implementation pattern
- [[Kanban Board for AI Tasks]] — where traceable bullets are used
- [[Feedback Loops as AI Speed Limit]] — why feedback matters
- [[The Pragmatic Programmer]] — source book
- [[Outrunning Your Headlights]] — related Pragmatic Programmer concept
