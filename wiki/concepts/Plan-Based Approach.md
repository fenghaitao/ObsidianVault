---
title: "Plan-Based Approach"
type: concept
tags: [ai, coding-agents, workflow, planning, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban.md"]
last_updated: 2026-06-29
---

## Definition
The Plan-Based Approach is a strategy for working with AI coding agents where the engineer invests significant time upfront creating comprehensive specifications, plans, and interrogating the model before letting it generate code. The investment in planning reduces downstream review time and iteration cycles.

## Key Information
- Articulated by Louis Knight-Webb as one of two fundamental approaches to working with AI coding agents
- Characteristics: writing comprehensive plan documents (markdown), using spec frameworks, interrogating the model until all possible questions are exhausted
- Benefit: less time reviewing work because edge cases are eliminated upfront and the model has maximum context
- Cost: more time spent planning upfront
- "Spending 5 minutes of planning saves you 30 minutes of reviewing AI-generated code"
- Best suited for: backend feature development (can do test-driven development), migrations, and refactoring work
- Less suited for: frontend feature development (too many stateful edge cases, interactions, animations, styles to spec everything)
- When the plan-based approach works, the engineer should not need to be in the loop with the agent at all — the work should be fully test-driven
- Contrasts with the [[Review-Based Approach]] where minimal upfront planning is followed by multiple review cycles

## Related
- [[summary-20260502 - Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban]] — source
- [[Louis Knight-Webb]] — articulated the concept
- [[Review-Based Approach]] — the alternative strategy
- [[Plan and Review Shift]] — the broader paradigm this fits into
- [[Plan vs Review Matrix]] — framework for choosing between approaches
- [[SpecificationDrivenDevelopment]] — related formal methodology
- [[TDD with AI]] — test-driven development with AI, a plan-based technique
