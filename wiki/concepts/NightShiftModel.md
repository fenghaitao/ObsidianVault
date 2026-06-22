---
title: "NightShiftModel"
type: concept
tags: [pattern, agent-automation, delegation, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260512 - How I build agents that work the night shift.md, raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md, raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

The Night Shift model is a three-part design pattern for delegating recurring business tasks to AI agents that run automatically on schedules. Instead of the human opening a chat and prompting, the agent shows up, does the work, and surfaces only what needs human attention. The name comes from Brian Casel running most agents overnight while he sleeps.

## Key Information

### The Three Parts

1. **Shared Interface** — one source of truth both human and agent can read/write. Can be as simple as a markdown file with checkboxes, or a custom app with UI (for human) + API (for agent).
2. **Human-in-the-Loop** — short, focused review sessions (2-20 minutes). Review agent output, leave comments, approve, check boxes. Then close and return to other work.
3. **Agent with Skill on Recurring Schedule** — the agent runs a skill (step-by-step markdown instructions) on a schedule (daily, weekly, etc.). Each run, it picks up where it left off, acts on latest feedback, pushes work forward, and surfaces new items for review.

### Real Examples

- **SEO meta-tag review**: agent checks all pages on builder methods site every 2 weeks, fixes suboptimal titles/meta descriptions via API, sends a report.
- **GitHub PR review**: agent reviews open pull requests on open-source tools, makes merge/close recommendations, drafts comments. Brian checks a checkbox to approve.
- **Content ideation**: Claude Co-work agent runs every morning at 6 AM, follows content development skill, submits new content ideas to [[SparkDrop]] via API.
- **Intake processing**: agent captures all published content and daily work into Dropbox, summarizes nightly.

### Platform Agnosticism

The pattern works on any agent platform: Brian has built it on [[OpenClaw]], [[HermesAgent]], [[ClaudeCowork]], and [[ClaudeCode]]. The skills (markdown files) are portable.

### Heuristic for Finding Candidates

"Have I done this before? Will I need to do it again?" If yes to both, it's a candidate for the Night Shift.

## Related

- [[BrianCasel]] — creator of the pattern
- [[AgentPlatformPortability]] — the strategy behind platform independence
- [[AgentSkills]] — the reusable instructions
- [[InternalTools]] — the custom apps used as interfaces
- [[HumanInTheLoop]] — the review role
- [[SparkDrop]] — a Night Shift-powered app
- [[BrainDown]] — the report viewer
- [[ClaudeCowork]] — one scheduling platform
- [[HermesAgent]] — another scheduling platform
