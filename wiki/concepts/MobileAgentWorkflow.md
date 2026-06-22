---
title: "MobileAgentWorkflow"
type: concept
tags: [workflow, mobile, claude-code, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260326 - Claude Code on Mobile： The Complete Guide.md]
last_updated: 2026-06-22
---

## Definition

Mobile agent workflow is the practice of starting, monitoring, and continuing AI coding agent sessions from a mobile device. It encompasses multiple scenarios from simple session handoff to full remote machine access, enabling builders to ship features from anywhere.

## Key Information

### Four Scenarios (Brian Casel's Framework)

1. **Remote Control**: start on desktop, enable remote control, continue on mobile — simplest, requires desktop initiation.
2. **Cloud-based new session**: start a new Claude Code session in the cloud from mobile app — path of least friction, but no local files/skills.
3. **New project from scratch**: create GitHub repo via mobile browser, authorize in Claude app, start building — full project initiation from phone.
4. **Power user full remote**: Termius + Tailscale + TMux — SSH into home machine, run `claude remote control`, connect via Claude mobile app — full local access.

### Key Tools

- **Tailscale**: secure network connecting all devices; phone can reach home machine from anywhere.
- **Termius**: terminal app for phone that SSHes into remote machines.
- **TMux**: keeps terminal sessions alive if mobile connection drops.

### Limitations

- Cloud-based sessions lack access to local files, skills, and configurations.
- Server mode requires pre-configuration on the desktop machine.
- GitHub mobile app can't create repos (use mobile browser).

## Related

- [[BrianCasel]] — practitioner
- [[ClaudeCode]] — the agent
- [[ServerMode]] — the remote access pattern
- [[Tailscale]] — networking tool
- [[AgentMultitasking]] — the broader workflow
