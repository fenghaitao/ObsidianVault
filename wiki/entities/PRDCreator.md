---
title: "PRDCreator"
type: entity
tags: [tool, agent-skill, planning, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md, raw/03-transcripts/Brian Casel/Channel Only/20260518 - You don't need to learn to code anymore.md, raw/03-transcripts/Brian Casel/Channel Only/20260611 - Claude Fable： Build me an app.md]
last_updated: 2026-06-22
---

## Definition

PRD Creator is a free open-source agent skill created by Brian Casel that automates the planning phase of software development. It walks the user through a structured Q&A process to shape a Product Requirements Document (PRD), then breaks the work into buildable milestones with handoff prompts for coding agents.

## Key Information

- Available at buildermethods.com/tools and via the Claude Code plugin marketplace as "BM PRD Creator."
- Works with Claude Code, Codex, Cursor, Anti-Gravity, and other coding agents.
- Process flow: core purpose → in-scope features → out-of-scope features → tech stack → integrations → data model → feature-level details → milestone breakdown.
- Output: a `build_plan/` folder with `PRD.md` (or `.html`) and numbered milestone folders, each containing a `prompt.md` for handoff.
- Milestones are sequenced by dependency order and balanced for buildable size.
- Each milestone prompt instructs the agent to read the PRD for context, build only that milestone, and write a milestone log for the next milestone to reference.
- Bridges the experience gap: asks the questions an experienced product designer would ask, so even non-technical builders can produce professional specs.
- Designed to work with plan mode — the PRD defines what to build, plan mode defines how to code it.

## Related

- [[BrianCasel]] — creator
- [[SpecDrivenDevelopment]] — the methodology it supports
- [[MilestoneBasedBuilding]] — the approach it enables
- [[BuildNew]] — companion starter template
- [[ClaudeCode]] — primary target coding agent
- [[VerificationCriteria]] — the definition-of-done pattern it uses
