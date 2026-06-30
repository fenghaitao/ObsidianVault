---
title: "Cron Creator"
type: concept
tags: [claude-code, tool, automation, scheduling, cron]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
The Cron Creator is a Claude Code tool that enables scheduling recurring agent tasks using standard cron syntax (five stars). It is the underlying mechanism that powers the Loop Command.

## Key Information
- Claude Code built-in tool for scheduling recurring tasks
- Uses standard five-star cron syntax (minute, hour, day of month, month, day of week)
- Powers the `loop` command in Claude Code
- Enables patterns like "every minute," "every hour," "every morning at 6am"
- Used by Chris Parsons for his morning loop (6am daily briefing), heartbeat loop (every 15 minutes), and continuous ticket implementation loops
- Sessions with cron tasks last about 3 days before needing refresh

## Related
- [[Loop Command]] — the user-facing command that uses it
- [[ClaudeCode]] — the tool it's part of
- [[Ralph Loop]] — the pattern it enables
- [[ChrisParsons]] — heavy user
- [[Morning Loop]] — one scheduled use case
- [[Heartbeat Loop]] — one scheduled use case
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
