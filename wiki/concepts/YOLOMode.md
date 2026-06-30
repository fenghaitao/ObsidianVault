---
title: "YOLOMode"
type: concept
tags: [claude-code, permissions, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-29
---

## Definition
YOLO mode is a Claude Code setting that skips permission confirmations for tool executions, allowing the agent to operate without user approval for each action. It represents a trade-off between speed and security.

## Key Information
- A workshop attendee asked about statistics on YOLO mode usage; Thariq Shihipar noted Anthropic internally doesn't use it due to higher security posture
- Represents the permissioning layer of the Swiss cheese defense — YOLO mode removes one layer of defense
- The existence of YOLO mode highlights the spectrum of autonomy vs. control in agent design

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ClaudeCode]] — where YOLO mode exists
- [[SwissCheeseDefense]] — the security model YOLO mode relaxes`r`n- [[Review-Based Approach]] — the "YOLO a prompt and iterate" strategy for AI coding agents
