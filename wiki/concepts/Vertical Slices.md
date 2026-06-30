---
title: "Vertical Slices"
type: concept
tags: [ai, software-engineering, architecture, feedback, task-decomposition]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Vertical Slices are thin, end-to-end pieces of functionality that cross all layers of a software system (database, API, frontend). In AI coding, they are the preferred way to structure tasks so that each completed slice produces integrated, testable feedback.

## Key Information
- Contrasts with horizontal slices: building layer by layer (all database first, then all API, then all frontend)
- Horizontal slicing delays integrated feedback until the final phase, meaning bugs in layer integration are discovered late
- AI naturally gravitates toward horizontal coding because it's easier to reason about one layer at a time
- A good vertical slice includes: schema changes, service creation, and a minimal frontend representation
- Vertical slices enable the AI to get feedback on its entire flow during or at the end of each task
- Matt Pocock explicitly instructs his "PRD to Issues" skill to use vertical slices, and will correct the AI if it proposes horizontal slices
- Example correction: "The first slice is too horizontal" when the AI proposed creating the gamification service alone without frontend changes
- Vertical slices are the implementation of the Traceable Bullets concept from The Pragmatic Programmer

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — advocates for vertical slices
- [[Traceable Bullets]] — the theoretical foundation
- [[Kanban Board for AI Tasks]] — where vertical slices are used
- [[Feedback Loops as AI Speed Limit]] — why integrated feedback matters
- [[Deep Modules]] — complementary architecture pattern
- [[Task Decomposition]] — related concept
