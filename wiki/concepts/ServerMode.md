---
title: "ServerMode"
type: concept
tags: [claude-code, remote, mobile]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260326 - Claude Code on Mobile： The Complete Guide.md]
last_updated: 2026-06-22
---

## Definition

Server mode is a Claude Code remote control configuration where a project is made available for remote connections without an active session. Running `claude remote control` in a project directory puts it in server mode, allowing new sessions to be started from mobile that run on the local machine with full access to files, skills, and configurations.

## Key Information

- Activated by running `claude remote control` in a project directory (not inside an active Claude Code session).
- Allows mobile-initiated sessions that run on the local machine with full local access.
- Contrast with cloud-based sessions: server mode gives access to local files, skills, and configs.
- Requires pre-configuration — you must set it up before leaving your desk.
- Power user workaround: SSH into home machine via Termius + Tailscale, run `claude remote control`, then connect from Claude mobile app.

## Related

- [[ClaudeCode]] — the tool
- [[MobileAgentWorkflow]] — the broader pattern
- [[Tailscale]] — networking enabler
- [[Termius]] — terminal enabler
- [[BrianCasel]] — practitioner
