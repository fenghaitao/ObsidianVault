---
title: "ClaudeCowork"
type: entity
tags: [tool, agent-platform, anthropic, claude, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md, raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

Claude Co-work is Anthropic's agent platform that runs within the Claude desktop app (and on dedicated machines). It features scheduled recurring tasks, dispatch for mobile interaction, and uses Claude Opus models. Brian Casel uses it for high-stakes creative jobs where output quality matters most.

## Key Information

- Part of Anthropic's Claude ecosystem; accessible via Claude desktop app's "Co-work" tab.
- Key feature: scheduled tasks — recurring background jobs that run automatically.
- Limited to 15 scheduled tasks (vs. Hermes's unlimited cron jobs).
- Dispatch feature: chat with Co-work agents from the Claude mobile app.
- Brian runs Co-work on a dedicated Mac mini (separate from his daily driver) for 24/7 operation.
- Used for category 2 jobs: high-creative, high-stakes tasks (writing, design, coding, content ideation).
- Uses Claude Opus models under Brian's Claude Max subscription plan.
- As of June 2026, Anthropic changed pricing: Max plan only covers Claude's own tools (Claude Code, Claude Co-work), not third-party platforms.
- Brian's content development agent runs every morning at 6 AM via Co-work, following his content development skill and interacting with [[SparkDrop]] via API.

## Related

- [[BrianCasel]] — user
- [[Anthropic]] — creator
- [[ClaudeCode]] — companion tool for day-to-day coding
- [[HermesAgent]] — companion platform for routine jobs
- [[AgentPlatformPortability]] — the strategy
- [[NightShiftModel]] — the pattern running on Co-work
- [[SparkDrop]] — the app agents interact with
