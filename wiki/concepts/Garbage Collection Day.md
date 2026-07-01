---
title: "Garbage Collection Day"
type: concept
tags: [agentic-engineering, code-quality, process, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Garbage Collection Day is a weekly practice (Fridays) where every engineer on the team takes every bit of slop observed during the week and figures out ways to categorically eliminate it from ever happening again. It closes the loop between human review feedback and automated prompt injection into agents.

## Key Information
- Practice from Ryan Lopopolo's team at OpenAI
- Held every Friday — the entire team's job is to eliminate slop patterns
- Process: identify durable classes of failures that agents and humans make repeatedly → figure out why time is spent on them → devise a solution to systematically eliminate the class of misbehavior → observe, refine, and iterate
- Outputs include: documentation updates, new lint rules, new reviewer agent prompts, test assertions about code structure
- Transforms synchronous human time spent on code review feedback into durable, automated guardrails
- Example: noticing agents forget retries and timeouts on network code → write docs, create a bespoke lint rule checking every fetch call → durably solved
- Enables the team to progressively reduce slop and increase agent autonomy over time

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[Reviewer Agents]] — CI automation that Garbage Collection Day feeds into
- [[NonFunctional Requirements Specification]] — what gets encoded during GC Day
- [[Slop]] — what GC Day eliminates
- [[ContinuousImprovement]] — related concept
