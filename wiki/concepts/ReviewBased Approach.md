---
title: "Review-Based Approach"
type: concept
tags: [ai, coding-agents, workflow, software-engineering, iteration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban.md"]
last_updated: 2026-06-29
---

## Definition
The Review-Based Approach is a strategy for working with AI coding agents where the engineer provides a brief prompt and lets the agent run, then iterates through multiple review cycles to refine the output. It prioritizes quick starts over upfront planning at the cost of more back-and-forth.

## Key Information
- Articulated by Louis Knight-Webb as one of two fundamental approaches to working with AI coding agents
- Characteristics: YOLO a brief prompt ("Let's add a contact form to the webpage"), let the agent run, then go back and forth correcting styles and figuring things out
- Benefit: quick to start, minimal upfront investment
- Cost: more review time, more rounds of back-and-forth with the agent, context-switching overhead
- Best suited for: frontend feature development where there are many stateful edge cases (interactions, animations, styles, functionality) that are hard to spec upfront
- Less suited for: backend work, migrations, and refactoring where plan-based approaches are more efficient
- Knight-Webb argues you should always prefer the plan-based approach when possible because switching back and forth with an agent giving half-delivered work is very time-consuming
- Contrasts with the [[PlanBased Approach]] where comprehensive upfront planning reduces downstream review cycles

## Related
- [[summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban]] — source
- [[Louis KnightWebb]] — articulated the concept
- [[PlanBased Approach]] — the preferred alternative strategy
- [[Plan and Review Shift]] — the broader paradigm this fits into
- [[Plan vs Review Matrix]] — framework for choosing between approaches
- [[VibeCoding]] — related approach emphasizing feel over specification
- [[YOLOMode]] — the "just send it" mentality
