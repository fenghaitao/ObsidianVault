---
title: "summary-20260216 - My Multi-Agent Team with OpenClaw"
type: source
tags: [source, brian-casel, openclaw, multi-agent, setup]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260216 - My Multi-Agent Team with OpenClaw.md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel details his complete OpenClaw multi-agent setup: a dedicated Mac mini M4, four agents (Claw/sysadmin, Bernard/developer, Val/marketer, Gumbo/assistant), Slack bots for communication, OpenRouter for model cost optimization, a custom-built HQ dashboard, and a Dropbox-based shared file system with security isolation. He spent $600 on hardware and blew past $200 in API tokens in the first two days before optimizing.

## Key Points

- OpenClaw runs on a dedicated Mac mini M4 ($600) — not a daily driver, not a VPS. Brian prefers screen sharing for visual management.
- Security: dedicated email, dedicated GitHub user, separate Dropbox account with shared folders only — like onboarding a human employee.
- Four agents with distinct roles: Claw (sysadmin, Opus), Bernard (developer, Opus), Val (marketer, Sonnet), Gumbo (assistant, Sonnet).
- All agents share one workspace for shared memory and brain folder access.
- Communication: Slack bots with threaded replies (tried Telegram first, found markdown support lacking).
- API costs: uses OpenRouter to centralize and optimize model selection per task. Claude Max plan stays for personal use only.
- Custom HQ dashboard: Rails app for task management, scheduling, token tracking, execution logs.
- Use cases: content capture/repurposing, development backlog, glue work automation, reporting/trends.
- OpenClaw is "still very early, very raw" but the concept of autonomous agents with defined roles is "here to stay."

## Related

- [[BrianCasel]] — creator and author
- [[OpenClaw]] — the platform
- [[AgentTeams]] — the multi-agent pattern
- [[AgentPlatformPortability]] — the strategy
- [[NightShiftModel]] — the delegation pattern
- [[BrainDown]] — the markdown tool
