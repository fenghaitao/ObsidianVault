---
title: "summary-night-shift-agents"
type: source
tags: [source, brian-casel, night-shift, agent-skills, automation]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260512 - How I build agents that work the night shift.md]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel introduces the "Night Shift" model: a three-part design pattern for delegating recurring business tasks to AI agents. Part 1 is a shared interface (markdown file or custom app with API). Part 2 is the human-in-the-loop dropping in for short review sessions. Part 3 is an agent with a skill running on a recurring schedule. He demonstrates two real examples: an SEO meta-tag review agent and a GitHub pull request review agent. The core insight: stop asking "how can I do this faster?" and start asking "who can I delegate this to?"

## Key Points

- The Night Shift has three parts: (1) shared interface — one source of truth both human and agent can read/write, (2) human-in-the-loop — short focused review sessions, (3) agent with skill on recurring schedule.
- The interface can be as simple as a markdown file with checkboxes, or a custom app with UI + API.
- Example 1 (SEO): agent reviews all pages on builder methods site, finds suboptimal meta titles/descriptions, fixes them via API, sends a report. Runs every 2 weeks.
- Example 2 (GitHub PRs): agent reviews open pull requests on open-source tools, makes merge/close recommendations, drafts comments. Brian checks a checkbox to approve.
- The agent posts comments on GitHub that appear to come from Brian — but are agent-drafted.
- The pattern is platform-agnostic: Brian has built it on OpenClaw, Claude Code, and Claude Co-work.
- Scheduling options: custom tasks dashboard (Brian's), Claude Co-work's built-in scheduler, OpenClaw's cron system.
- Heuristic for finding candidates: "Have I done this before? Will I need to do it again?" If yes to both, delegate to an agent.
- Brian's custom tasks dashboard is available as a build kit in Builder Methods Pro.

## Related

- [[BrianCasel]] — creator and author
- [[NightShiftModel]] — the core pattern
- [[AgentSkills]] — the reusable instructions agents follow
- [[HumanInTheLoop]] — the review role
- [[InternalTools]] — the custom apps used as interfaces
- [[AgentPlatformPortability]] — the pattern works across platforms
- [[ClaudeCowork]] — one scheduling option
- [[OpenClaw]] — another scheduling option
- [[BrainDown]] — the markdown report viewer
