---
title: "AgentRoutines"
type: concept
tags: [ai, agents, automation, templates, paperclip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
Agent routines are reusable, templated tasks in Paperclip that can be grouped by project or agent and run either on a schedule or manually with template variables. They serve as parameterized prompt templates, eliminating the need for prompt folders or copy-paste workflows.

## Key Information
- Paperclip feature for creating reusable task templates with variables
- Can be grouped by project or agent for organizational clarity
- Support scheduling (cron-like) for recurring tasks or manual execution on demand
- Template variables allow parameterization — e.g., a "create PR" routine with a `{branch}` variable
- Example routines from Paperclip's own usage:
  - Create a Discord message of everything merged into master today
  - Write the release changelog
  - Create a single PR in a specified branch
  - Process Twitter bookmarks into strategy reports
- Routines can incorporate skills — e.g., a PR routine that uses the Greptile skill for code review
- Overlap with skills conceptually, but routines are more about workflow orchestration while skills are about capability loading
- Dotta Bippa uses routines to process Twitter bookmarks for ideas to improve Paperclip

## Related
- [[Paperclip]] — the orchestrator implementing routines
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[Skills]] — complementary concept; routines can invoke skills
- [[AgentOrgChart]] — routines grouped by agent or project within the org chart
- [[Greptile]] — skill used within Paperclip's PR review routine
