---
title: "summary-20260326 - Claude Code on Mobile： The Complete Guide"
type: source
tags: [source, brian-casel, claude-code, mobile, remote-work]
sources: ["raw/03-transcripts/Brian Casel/Channel Only/20260326 - Claude Code on Mobile： The Complete Guide.md"]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel provides a complete guide to using Claude Code from mobile devices, covering four scenarios: continuing a desktop session via remote control, spawning new cloud-based sessions, creating new projects from scratch (including GitHub repo creation), and the power-user setup for full remote access to a home machine via Termius + Tailscale + TMux.

## Key Points

- **Scenario 1 (Remote Control)**: start session on desktop, run `remote control`, continue on mobile. Can set config to always-on.
- **Scenario 2 (Cloud-based new session)**: start a new Claude Code session in the cloud from the mobile app. Works with authorized GitHub repos. Creates PRs automatically. Limitation: no access to local files/skills.
- **Scenario 3 (New project from scratch)**: create a GitHub repo via mobile browser, authorize it in Claude app, start building. Can use GitHub templates.
- **Scenario 4 (Power user - full remote)**: Termius (terminal app) + Tailscale (secure network) + TMux (persistent sessions). SSH into home machine from phone, run `claude remote control`, then connect via Claude mobile app. Gives full access to local files, skills, and configs.
- Claude Code on the web (cloud) is the path of least friction but lacks local file/skill access.
- Server mode (`claude remote control` without an active session) lets you start new sessions remotely.
- The GitHub mobile app can't create repos; use mobile browser instead.

## Related

- [[BrianCasel]] — creator and author
- [[ClaudeCode]] — the tool
- [[MobileAgentWorkflow]] — the concept
- [[Tailscale]] — networking tool
- [[Termius]] — terminal app
- [[TMux]] — session persistence
- [[ServerMode]] — the remote access pattern
