---
title: "HermesAgent"
type: entity
tags: [tool, agent-platform, automation, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md, raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

Hermes Agent is a personal AI agent platform that runs on a local machine (similar to OpenClaw). Brian Casel uses it as his primary platform for routine, recurring background jobs, running on a dedicated Mac mini with Discord as the chat interface.

## Key Information

- Conceptually similar to [[OpenClaw]] — a personal AI agent running on your machine.
- Brian chose Hermes over OpenClaw for reliability: less buggy, easier setup, more reliable.
- Runs on a dedicated Mac mini for 24/7 availability.
- Chat interface: Discord (multi-channel, threaded conversations, good markdown support, emoji reactions).
- Previously tried Telegram (weak markdown) and Slack (loses thread context).
- Model: uses OpenAI GPT models via $20/month subscription for routine jobs.
- Cron job system: unlimited recurring scheduled tasks, each associated with a skill.
- Brian's agent "Gumbo" runs daily synthesis, weekly/monthly summaries, SEO health checks, PR reviews, intake processing, content capture.
- Each cron job delivers updates to dedicated Discord channels.
- Ported his skills from OpenClaw to Hermes easily since skills are platform-agnostic markdown files.

## Related

- [[BrianCasel]] — user
- [[OpenClaw]] — predecessor platform
- [[ClaudeCowork]] — companion platform for creative jobs
- [[AgentPlatformPortability]] — the strategy behind using multiple platforms
- [[NightShiftModel]] — the pattern running on Hermes
- [[AgentSkills]] — the reusable instructions
