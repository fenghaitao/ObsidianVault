---
title: "GoodAgentTasks"
type: concept
tags: [agents, workflow, task-design, best-practices]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Good agent tasks are tasks with specific properties that make them suitable for AI agents. Mario Zechner defines these as: well-scoped (agent can find everything needed), having an evaluation function, non-mission-critical, boring/repetitive, reproduction cases for user issues, and rubber ducking.

## Key Information
- Mario Zechner's properties for good agent tasks:
  - **Scope**: "If you can scope it in such a way that the agent is guaranteed to find all the things it needs to find to do a good job, you're done."
  - **Evaluation function**: "If you can give it a function to evaluate how well it did the job, even better."
  - **Hill climbing / auto research**: tasks where the agent can iteratively improve
  - **Non-mission-critical**: "let it wipe"
  - **Boring stuff**: repetitive tasks where errors are tolerable
  - **Reproduction cases**: user issues with partial information — "I don't spend any mornings anymore doing that"
  - **Rubber duck**: when you don't have a human nearby to talk through problems
- Workflow: "You evaluate. You take what's reasonable, most of it isn't, and then finalize."
- Contrasts with critical code which must be read line by line and written by hand

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[MarioZechner]] — originator
- [[SlowingDownWithAgents]] — the broader philosophy
- [[CompoundingBooboos]] — what happens when agents are used for bad tasks
- [[AgentCodeReviewLimitations]] — why review agents aren't the answer
- [[AIasJuniorDeveloper]] — related mental model from Brendan O'Leary
- [[ResearchPlanImplement]] — related structured workflow
