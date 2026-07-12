---
title: "Agent Heartbeat"
type: concept
tags: [AI, agent, OpenClaw, scheduling, automation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

The agent heartbeat is OpenClaw's scheduling mechanism that makes agents feel proactive and alive. It is essentially a cron job system: agents wake up on a schedule (every 30 minutes, every hour, or at specific times) to check their to-do list and execute tasks.

## Key Information

- Two modes of task management:
  1. **Time-based schedule:** Specific cron jobs (e.g., "every morning at 8am, sweep the CRM")
  2. **Heartbeat polling:** Every 30 minutes or hour, check if there's work to do
- This is what creates the illusion of proactivity: "I woke up and my OpenClaw did so much work for me overnight" — really, it was a scheduled midnight task
- Examples from Claire Vo:
  - Sam wakes up every morning and does the PLG sweep of the CRM
  - Finn pings at 3pm every day: "Which of you are picking up which kids?"
  - Sage every Monday: "Have you remembered to post on LinkedIn about your course?"
  - Sam at the end of each week: CRM cleanup, QBR prep
- The heartbeat is what makes OpenClaw feel "alive" — it's not waiting for you to prompt it; it's checking in proactively
- Technically simple: just periodic checks against a task list
- "It works on a schedule. You can say every 3 hours, I want you to do XYZ"

## Why It Matters

- The heartbeat is one of the two key features (along with the soul) that make OpenClaw feel alive and proactive
- It transforms the agent from a reactive tool into a proactive teammate
- It handles the "I forgot" problem — the agent remembers to check on things even when you don't

## Related

- [[OpenClaw]] — the platform
- [[Agent Soul - Identity]] — the other key feature
- [[Proactive Agents]] — the broader concept
- [[Agent Tasking Systems]] — how tasks are managed
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
