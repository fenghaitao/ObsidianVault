---
title: "AFK Tasks"
type: concept
tags: [ai, workflow, automation, agents, implementation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
AFK (Away-From-Keyboard) Tasks are implementation tasks that can be fully delegated to an AI agent without human supervision. They contrast with human-in-the-loop tasks (like planning and alignment) that require active human participation.

## Key Information
- Matt Pocock divides all AI coding tasks into two categories: human-in-the-loop and AFK
- Planning and alignment (Grill Me sessions) must be human-in-the-loop — they require human judgment and decision-making
- Implementation can be turned into AFK tasks once the plan is clear and the issues are well-defined
- AFK tasks are what the "night shift" processes while the human is away
- The Kanban board classifies each issue with a type: AFK or human-in-the-loop
- AFK tasks are processed by the Ralph Loop: pick next AFK task, implement with TDD, run feedback loops, repeat
- The AFK agent prompt includes: work on AFK issues only, if all AFK tasks complete output "no more tasks," pick the next task based on priority (critical bug fixes, then dev infrastructure, then trace bullets, then polishing)
- This separation creates the "day shift / night shift" workflow: human plans during the day, AI implements overnight

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — workflow creator
- [[Day Shift Night Shift]] — the workflow pattern
- [[Ralph Loop]] — the agent that processes AFK tasks
- [[Kanban Board for AI Tasks]] — where AFK tasks are defined
- [[HumanInTheLoopWorkflows]] — the complementary category
- [[Sandcastle]] — library for running AFK agent loops
- [[AgenticLoop]] — related concept
