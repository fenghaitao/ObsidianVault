---
title: "State Machine Gates"
type: concept
tags: [agentic-engineering, state-machine, agent-harness, enforcement, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

State machine gates are mandatory checkpoints between stages in an agent pipeline that enforce verification before the next stage can begin. Unlike prompt-based instructions, state machine gates are enforced by deterministic code outside the AI model's control.

## Key Information

- Implemented in Case (Nick Nisi's agent harness) using a TypeScript state machine built on Pi
- Five stages with gates between each: Implementer → Gate → Verifier → Gate → Reviewer → Gate → Closer → Gate → Retrospective
- The verifier must confirm the implementation works before the reviewer can review
- If the reviewer finds issues, the state machine routes back to the implementer — the reviewer cannot proceed
- The closer cannot work until all previous gates are satisfied, and must provide evidence of completion
- The retrospective agent runs last and cannot be skipped
- Key advantage: the AI model cannot decide to skip a step or reorder stages — the state machine enforces the sequence deterministically
- This is the architectural implementation of "enforce, don't instruct"
- Contrast with prompt-based pipelines where the agent can "decide not to" run verification

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — implemented in Case
- [[Case]] — agent harness using state machine gates
- [[Enforce Dont Instruct]] — the principle this implements
- [[EvidenceBased Verification]] — what the gates enforce
- [[Retrospective Agent]] — the final stage in the state machine
- [[InhabitingTheStateMachine]] — related concept
- [[Harness Engineering]] — the broader discipline
