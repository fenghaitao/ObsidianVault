---
title: "AgentSkills"
type: concept
tags: [agent-instructions, automation, reusable]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md, raw/03-transcripts/Brian Casel/Channel Only/20260512 - How I build agents that work the night shift.md, raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

Agent skills are reusable markdown files containing step-by-step instructions that AI agents follow to complete specific tasks. They are the portable unit of agent automation — write once, run on any platform, on any schedule.

## Key Information

### Structure (Brian Casel's Pattern)

- Main `SKILL.md`: the overall process with multiple phases.
- `steps/` folder: individual detailed instructions for each phase.
- Skills can reference each other (e.g., content ideation skill calls the front-end design skill).
- Skills can include interview steps where the agent asks the human clarifying questions.

### Examples from Brian's Collection

- **Content ideation**: research → generate sparks → pitch → develop drafts → schedule.
- **PR review**: check GitHub → review code → make merge/close recommendation → draft comment.
- **SEO meta-tag review**: scan all pages → identify suboptimal tags → fix via API → write report.
- **Daily synthesis**: read journal/code logs → summarize yesterday → surface items needing attention.
- **Intake processing**: capture all published content and work logs → file in Dropbox → create summaries.
- **App marketing page**: analyze codebase → interview Brian → design page → implement.
- **Plan videos from build**: analyze build work → extract concepts → draft video outline.
- **Starter kit generator**: analyze codebase → build PRD → extract design system → create prompts.

### Portability

Skills are platform-agnostic markdown files. Brian has ported the same skills across [[OpenClaw]], [[HermesAgent]], [[ClaudeCowork]], and [[ClaudeCode]]. This is the foundation of [[AgentPlatformPortability]].

### Contrast with Claude Skills

While [[ClaudeSkills]] is Anthropic's specific implementation (folder + SKILL.md + progressive disclosure), "agent skills" is the broader concept of reusable agent instructions that predates and extends beyond any single platform.

## Related

- [[BrianCasel]] — primary practitioner
- [[NightShiftModel]] — the pattern skills enable
- [[AgentPlatformPortability]] — why skills are portable
- [[ClaudeSkills]] — Anthropic's specific implementation
- [[ProgressiveDisclosure]] — the loading pattern
