---
title: "summary-20260622 - How to build your own CRM (start to finish)"
type: source
tags: [source, brian-casel, internal-tools, spec-driven-development, crm]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260622 - How to build your own CRM (start to finish).md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel demonstrates building a custom CRM from scratch using Claude Code, his Build New Rails starter template, and his PRD Creator skill. The core argument: the most useful business skill isn't coding, it's building the exact tool your business needs instead of renting bloated SaaS. He walks through the full spec-driven workflow: shaping a PRD with scope decisions (in/out), defining a data model, breaking work into 5 milestones, using plan mode for implementation planning, and iterative refinement. Key insight: for internal tools, hard-code specifics rather than building complex configuration UIs.

## Key Points

- Commercial CRM tools are bloated for everyone and perfect for no one; building your own lets you match your exact workflow.
- The PRD Creator skill automates the planning process: high-level scope, data model, feature-level in/out decisions, milestone breakdown.
- Plan mode is used even after PRD creation — the PRD defines what to build, plan mode defines how to code it.
- Milestone logs pass context between sessions: each milestone writes a log that the next milestone reads.
- For internal tools, hard-code business-specific details (pipeline stages, fields) rather than building custom configuration UIs.
- Small refinements at the end of each milestone (app name, UI tweaks) are normal and quick.
- Regression testing is built into the workflow: Claude re-runs the full test suite after each change.
- The entire CRM (contacts, deals, Kanban, activity log, to-dos) was built in under an hour of human attention.

## Related

- [[BrianCasel]] — creator and author
- [[PRDCreator]] — the skill used for planning
- [[BuildNew]] — the Rails starter template
- [[SpecDrivenDevelopment]] — the overarching methodology
- [[MilestoneBasedBuilding]] — breaking work into buildable chunks
- [[InternalTools]] — the category of software being built
- [[ClaudeCode]] — the coding agent used
