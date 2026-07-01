---
title: "Kanban Board for AI Tasks"
type: concept
tags: [ai, workflow, planning, parallelization, kanban, task-decomposition]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
In Matt Pocock's AI coding workflow, a Kanban Board is a set of independently grabbable issues with blocking relationships, created from a PRD. Unlike sequential multi-phase plans, the Kanban board forms a directed acyclic graph (DAG) that enables parallel execution by multiple AI agents. In Demand-Driven Context, the Knowledge Base Kanban applies the same concept to documentation gaps.

## Key Information
- Created after the PRD step using a "PRD to Issues" skill that breaks the PRD into vertical slices
- Each issue has blocking relationships: "this one needs to be done before this one"
- The DAG structure means issues without blockers can be grabbed simultaneously by independent agents
- Contrasts with sequential multi-phase plans (phase 1, phase 2, phase 3) which can only be worked on by one agent at a time
- Issues are classified as AFK (away-from-keyboard) or human-in-the-loop
- The Kanban board allows continuous addition of new issues discovered during QA
- Pocock's "PRD to Issues" skill: locates the PRD, explores the codebase, drafts vertical slices, quizzes the user, creates issue files
- Issues can be stored as GitHub issues (Pocock's preference) or local markdown files
- A simple plan might have 3 phases: phase 1 (one task), phase 2 (two parallel tasks), phase 3 (one task that depends on all prior)
- **Demand-Driven Context**: The Context Gap Scanner produces a Knowledge Base Kanban — a board of documentation gaps organized by critical/high/medium priority. "Just like Jira tickets, we finish it. We actually have to document these missing pieces." This transforms the abstract problem of "we need better documentation" into concrete, actionable tickets.

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[MattPocock]] — workflow creator
- [[PRD (Product Requirements Document)]] — input to the Kanban board
- [[Traceable Bullets]] — the vertical slice methodology
- [[Vertical Slices]] — how issues are structured
- [[AFK Tasks]] — task classification
- [[Ralph Loop]] — the agent that processes the board
- [[Parallel Agents]] — multi-agent execution
- [[Sandcastle]] — Pocock's library for parallel agent loops
- [[Task Decomposition]] — related concept
- [[DAGvsLoopArchitecture]] — directed acyclic graph vs sequential
- [[Knowledge Base Kanban]] — Demand-Driven Context's documentation gap board
- [[Context Gap Scanner]] — produces the Knowledge Base Kanban
- [[DemandDriven Context]] — methodology using Kanban for knowledge gaps
