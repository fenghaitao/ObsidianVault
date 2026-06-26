---
title: "Reviewer Agents"
type: concept
tags: [ai, agentic-engineering, code-review, ci, automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Reviewer agents are AI agents that run in CI on every push, reviewing proposed code patches against documented standards of what "good" looks like. They surface P2-or-above issues that would block a PR from merging, replacing synchronous human code review with automated, persona-based review.

## Key Information
- Practice from Ryan Lopopolo's team at OpenAI
- Run on every push in CI, checking proposed patches against documentation of acceptable code
- Organized by persona: front-end architect, reliability engineer, security engineer, scalability engineer, product-minded engineer
- Each persona's review agent is primed with documentation describing what "good" looks like from that perspective
- Example: a security/reliability review agent checks that network code has timeouts and retries
- Output: comments on the PR that the implementation agent must address before proposing for merge
- Enables humans to step back from low-signal code review and focus on higher-leverage activities
- Continuously improved via Garbage Collection Day — as new slop patterns are identified, reviewer agent prompts are updated
- Key insight: senior engineers give good code reviews; reviewer agents should do the same

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[Garbage Collection Day]] — feeds improvements into reviewer agents
- [[Persona-oriented Documentation]] — what reviewer agents are primed with
- [[Non-functional Requirements Specification]] — what reviewer agents enforce
- [[AgenticEngineering]] — broader paradigm
