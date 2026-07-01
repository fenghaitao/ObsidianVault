---
title: "Plan vs Review Matrix"
type: concept
tags: [ai, coding-agents, workflow, decision-framework, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban.md"]
last_updated: 2026-06-29
---

## Definition
The Plan vs Review Matrix is a decision framework for choosing between plan-based and review-based approaches when working with AI coding agents. It maps work type (feature development vs. migrations/refactoring) against domain (frontend vs. backend) to determine the optimal strategy.

## Key Information
- Articulated by Louis Knight-Webb at AIE CODE 2026
- The matrix has four quadrants:
  - **Frontend + Feature Development**: Review-based approach preferred. Too many stateful edge cases (interactions, animations, styles, functionality) to spec everything upfront. Better to be in the loop with the agent.
  - **Backend + Feature Development**: Plan-based approach works well. Can do test-driven development. Spec out the work upfront.
  - **Frontend + Migrations/Refactoring**: Plan-based approach works. Structural changes can be fully specified.
  - **Backend + Migrations/Refactoring**: Plan-based approach strongly preferred. Should not be in the loop with the agent at all — fully test-driven.
- The matrix emerged from Knight-Webb's attempt to systematize when each approach makes sense
- The key differentiator is whether the work domain has too many stateful, visual, or interactive edge cases to fully specify upfront
- The matrix complements the broader principle: "Spending 5 minutes of planning saves you 30 minutes of reviewing AI-generated code" — but only when planning is feasible

## Related
- [[summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban]] — source
- [[Louis KnightWebb]] — articulated the framework
- [[PlanBased Approach]] — one strategy in the matrix
- [[ReviewBased Approach]] — the alternative strategy
- [[Plan and Review Shift]] — the broader paradigm the matrix serves
- [[TDD with AI]] — technique that enables plan-based approaches
