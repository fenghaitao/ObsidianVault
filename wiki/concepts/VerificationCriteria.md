---
title: "VerificationCriteria"
type: concept
tags: [quality, testing, ai-coding, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260611 - Claude Fable： Build me an app.md, raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md]
last_updated: 2026-06-22
---

## Definition

Verification criteria (or "definition of done") is a checklist pattern used in spec-driven development where each milestone explicitly states what must be true for the work to be considered complete. The AI agent uses this checklist to self-check its work before declaring done.

## Key Information

- Included in the PRD for each milestone: "Milestone N is done when [list of verifiable conditions]."
- Gives the AI agent a concrete standard to self-validate against, reducing the need for human re-prompting.
- Brian Casel observed that Claude Fable was particularly good at self-checking when given clear verification criteria.
- Works alongside automated testing: the agent runs the test suite, but verification criteria cover functional/behavioral correctness that tests may miss.
- Example: "User can create a contact with name, company, email. Contact appears in list view. Search filters by name. Mobile layout is responsive."
- Part of the broader shift from vibe coding (hope it works) to professional building (verify it works).

## Related

- [[SpecDrivenDevelopment]] — the methodology it supports
- [[MilestoneBasedBuilding]] — where criteria are defined per milestone
- [[PRDCreator]] — the skill that generates them
- [[ValidationGates]] — Cole Medin's related concept
- [[BrianCasel]] — advocate
