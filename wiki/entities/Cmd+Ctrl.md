---
title: "Cmd+Ctrl"
type: entity
tags: [tool, coding-agents, mobile, remote, open-source, agent-orchestration, agent-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl.md"]
last_updated: 2026-06-30
---

## Definition
Cmd+Ctrl (Command and Control) is an open-source system built by Michael Richman that provides a single-pane-of-glass mobile, web, and watch interface for monitoring, interacting with, and launching AI coding agent sessions across multiple platforms from anywhere.

## Key Information
- Built by [[MichaelRichman]] at [[Bitly]] to solve the problem of interacting with coding agents outside the terminal or IDE.
- Available on iPhone, Android, web, and Apple Watch.
- Coding-tool agnostic: works with Claude Code, Codex, Cursor, Gemini, GitHub Copilot, and Open Code.
- Cross-machine: aggregates agent sessions running on local machines and cloud VMs into a single UI.
- Architecture: daemon layer (open source) runs alongside each agent platform → control plane API aggregates all agents → UI layer for interaction.
- The daemon monitors agent lifecycle: when an agent is blocked, needs help, or completes, it communicates up to the control plane.
- Key features: subscribe to sessions for push notifications, view session history, overview dashboard with stand-up-style summaries, start new sessions from mobile.
- Sessions are organized into sections: subscribed (push notifications), on-my-radar (keep an eye on), recent (last 24 hours), and the rest (thousands of historical sessions).
- The daemon layer is open source, allowing any agent framework to plug in and be accessible through the same UI.
- Predates similar solutions: Anthropic's remote control/teleportation and Cursor's mobile solution were released after Cmd+Ctrl was built.

## Related
- [[MichaelRichman]] — creator
- [[Bitly]] — company where it was built
- [[FOMAT (Fear of Missing Agent Time)]] — the problem it solves
- [[Agent Control Plane]] — architectural pattern used
- [[Remote Agent Interaction]] — core capability
- [[Agent Choreography]] — workflow it enables
- [[Agent Session Management]] — key feature
- [[ClaudeCode]] — supported agent platform
- [[Codex]] — supported agent platform
- [[Cursor]] — supported agent platform
- [[Gemini]] — supported agent platform
- [[GitHubCopilot]] — supported agent platform
- [[OpenCode]] — supported agent platform
- [[Anthropic]] — later released competing remote control features
- [[summary-20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl]]
