---
title: "SpecDrivenDevelopment"
type: concept
tags: [methodology, planning, ai-coding, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md, raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md, raw/03-transcripts/Brian Casel/Channel Only/20260611 - Claude Fable： Build me an app.md]
last_updated: 2026-06-22
---

## Definition

Spec-driven development is a methodology for building software with AI where the human shapes a clear written plan (spec or PRD) before any code is written, then directs AI agents to build it in structured milestones. It contrasts with vibe coding by front-loading decision-making to reduce guesswork, re-prompting, and design drift.

## Key Information

### The Core Loop

1. **Raw idea** — a rough concept or feature list.
2. **Shape into a spec/PRD** — define scope (in/out), data model, integrations, feature-level details, verification criteria.
3. **Break into milestones** — sequenced buildable chunks, each self-contained and testable.
4. **Build milestone by milestone** — hand off each to a coding agent with clear context and success criteria.
5. **Review and refine** — check output, make small tweaks, then move to next milestone.

### Why It Works

- Front-loads the decisions that prevent AI from guessing (and drifting).
- The PRD serves as a single source of truth across multiple coding sessions.
- Milestones keep context windows clean and prevent projects from going off the rails.
- Milestone logs pass context between sessions without carrying forward stale conversation.
- Plan mode (in Claude Code) translates requirements into implementation plans — the PRD says what, plan mode says how.

### Contrast with Vibe Coding

| Vibe Coding | Spec-Driven Development |
|---|---|
| Prompt, hope, fix, re-prompt | Shape, plan, build, verify |
| AI guesses what you want | AI follows a clear written plan |
| Works for prototypes | Works for production tools |
| High re-prompting overhead | Less re-prompting, more shipping |

### Brian Casel's Implementation

Brian uses his [[PRDCreator]] skill to automate the planning Q&A, producing a PRD broken into ~5 milestones. Each milestone gets a `prompt.md` that instructs the agent to read the PRD, build only that milestone, and write a milestone log. He uses plan mode for implementation planning even after the PRD is complete.

## Related

- [[BrianCasel]] — primary advocate
- [[PRDCreator]] — the skill that automates planning
- [[MilestoneBasedBuilding]] — the chunking strategy
- [[VibeCoding]] — what this replaces
- [[ProductArchitect]] — the human role
- [[VerificationCriteria]] — the definition-of-done pattern
- [[PRPFramework]] — Cole Medin's related two-pass methodology
- [[cole-vs-brian-planning-methodologies]] — synthesis comparing Cole's and Brian's planning approaches
- [[ClaudeCode]] — primary execution surface
