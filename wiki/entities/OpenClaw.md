---
title: "OpenClaw"
type: entity
tags: [AI, agent, open-source, tool, platform]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"]
last_updated: 2026-07-11
---

## Definition

OpenClaw is an open-source AI agent framework (formerly called Clawbot, then moldbot) created by Peter. It runs locally on a user's machine and gives AI models "hands" — the ability to execute actions on a computer, access the web, read and send emails, manage calendars, and perform tasks autonomously on a schedule. Jensen Huang called it "the new computer" and noted it is the fastest growing open source project in history.

## Key Information

- Open-source AI agent harness that runs on a local machine (Mac, cloud VM, etc.)
- Built on a coding harness named Pi (similar to Claude Code or Codex under the hood)
- Uses a command-line tool that writes and runs code and talks to users through an LLM
- Agents have identity (soul file), heartbeat (scheduled tasks), and memory
- Agents work on a schedule (cron jobs) — checking every 30 minutes for tasks
- Web search via Brave (default), Exa, or Perplexity APIs
- Browser use via dedicated Chrome profiles (each agent can have its own color-coded profile)
- Communication channels: Telegram, WhatsApp, iMessage, email, Slack
- Jensen Huang: "Every company in the world needs to have a cloud strategy. OpenClaw is the new computer."
- Fastest growing open source project in history, surpassing Linux
- Maintainers have done significant work to harden against prompt injection
- Security posture: "personal by default," designed for single-user trust relationships
- Agents are sandboxed by default; you must explicitly open up access
- One-line install command from openclaw.ai

## Key Features

- **Soul (identity.md):** Defines who the agent is, its personality, operating principles. Pre-seeded with concepts like "be helpful, have opinions, be resourceful before asking."
- **Heartbeat:** Scheduled tasks — agents can run on a cron-like schedule, checking every 30 minutes or at specific times.
- **Memory:** Persistent memory of past interactions and user preferences.
- **Tools:** Access to email, calendar, web search, browser, code execution, file system operations.
- **Onboarding interview:** When first created, the agent asks "Who am I? Who are you?" and conducts an interview to build its identity.
- **Multi-agent:** Multiple agents can run on the same machine, sharing tools and workspace if permitted.

## Practical Setup Tips (from Claire Vo)

- Use a clean/separate machine (Mac Mini, old laptop, cloud VM), not your daily work computer
- Create a separate Gmail account and local admin account for the agent
- Use the good models (Opus 4.6, Sonnet 4.6, GPT-5.4) — better security and experience
- Telegram is the most beginner-friendly communication channel
- Turn on screen sharing and remote login on the Mac Mini for headless operation
- Install Claude Code on the same machine as a "god mode administrator" to fix configuration issues
- OpenClaw files live in a hidden `~/.openclaw` folder (Command+Shift+Period in Finder to reveal)

## Challenges

- Setup is painful and time-consuming (8+ hours for initial install)
- Browser use is unreliable across all AI products, not just OpenClaw
- Agents can lose access to email and need re-authentication
- Memory issues and context overload
- The web is "hostile to agents" due to anti-bot mechanisms
- "It's not hands-off" — requires ongoing maintenance

## Related

- [[Peter - OpenClaw]] — the developer/maintainer
- [[Claire Vo]] — power user running 9 agents
- [[Jessie Janes]] — homeschooling mom and OpenClaw power user
- [[Claude Code]] — used as admin for OpenClaw
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
- [[Agent Soul - Identity]] — concept
- [[Agent Heartbeat]] — concept
- [[Agent Team Management]] — concept
- [[Progressive Trust with AI]] — concept
