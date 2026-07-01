---
title: "Human-in-the-Loop Orchestration"
type: concept
tags: [agents, orchestration, human-review, workflow]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Human-in-the-loop orchestration is the practice of maintaining human review at intermediate steps during parallel agent workflows, rather than only reviewing the final output. The goal is ~90% automation with human approval gates at key checkpoints, achieving an order-of-magnitude productivity lift while maintaining quality control.

## Key Information
- The goal is not 100% automation but ~90% — still an order-of-magnitude productivity lift.
- Humans must review not just the final collated result but intermediate outputs from each agent.
- In the verifier-fixer pipeline, each fixer produces a PR ready for human approval before unblocking dependent batches.
- The typical git workflow: start a new branch → add high-level context (micro-agent) → put scaffolding in place → dispatch agents → accumulate work → review intermediate PRs → rip out scaffolding → merge.
- For beginners, 3-5 concurrent agents is recommended; more than that becomes hard to track mentally.
- At scale, hundreds or thousands of agents can run concurrently, with PRs sent to individual teams for review rather than one person reviewing everything.
- Human review also applies to context sharing: agents may try to push unimportant information to shared files, requiring human filtering.
- The workflow mirrors managing a team of engineers: decompose work, dispatch, review outputs, iterate.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Agent Orchestration]] — broader practice
- [[HumanInTheLoopWorkflows]] — related workflow pattern
- [[VerifierFixer Pipeline]] — pipeline with built-in human review
- [[Task Decomposition]] — prerequisite for effective review
- [[Context Sharing Between Agents]] — also benefits from human review
