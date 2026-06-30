---
title: "Heartbeat Loop"
type: concept
tags: [ai, agents, automation, loop, monitoring, telegram]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
The Heartbeat Loop is one of Chris Parsons' specialized Ralph loops. Every 15 minutes, it fires up Claude on a VPS, checks his calendar and other items, and sends Telegram messages with relevant updates.

## Key Information
- Runs every 15 minutes on Chris Parsons' VPS
- Fires up Claude, checks calendar and other items
- Sends updates via Telegram messages
- Similar to what OpenClaw does with its heartbeat mechanism
- Part of Parsons' layered loop system: morning loop (daily planning), worker loop (continuous execution), heartbeat loop (periodic check-ins)
- Keeps Parsons informed throughout the day without him having to actively check

## Related
- [[ChrisParsons]] — creator and user
- [[Ralph Loop]] — the general pattern
- [[Morning Loop]] — daily briefing loop
- [[Worker Loop]] — continuous execution loop
- [[OpenClaw]] — similar heartbeat mechanism
- [[Telegram]] — notification channel
- [[Everything is a Loop]] — the underlying philosophy
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
