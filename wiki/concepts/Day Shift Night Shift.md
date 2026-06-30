---
title: "Day Shift Night Shift"
type: concept
tags: [ai, workflow, planning, implementation, automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
The Day Shift / Night Shift is Matt Pocock's metaphor for his AI coding workflow: the "day shift" is when the human plans, aligns, and prepares work (Grill Me, PRD, Kanban board), and the "night shift" is when AI agents implement the prepared work AFK (away-from-keyboard).

## Key Information
- Day shift = human-in-the-loop activities: idea exploration, Grill Me sessions, PRD creation, Kanban board setup, human review of plans
- Night shift = AFK activities: AI agents pick up issues from the Kanban board, implement with TDD, run feedback loops, create commits
- The day shift queues up work for the night shift to process
- This allows the human to spend focused time on planning and then step away while AI does the implementation
- The night shift can run sequentially (one agent at a time) or in parallel (multiple agents on independent issues)
- The separation means humans don't need to watch AI code in real-time
- QA and code review happen after the night shift completes, creating a feedback loop back to the Kanban board

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — workflow creator
- [[AFK Tasks]] — what the night shift processes
- [[Ralph Loop]] — the night shift agent
- [[Kanban Board for AI Tasks]] — the work queue
- [[Grill Me]] — day shift activity
- [[PRD (Product Requirements Document)]] — day shift output
- [[Sandcastle]] — library for running the night shift
- [[HumanInTheLoopWorkflows]] — day shift pattern
