---
title: "Agent Control Plane"
type: concept
tags: [concept, agents, architecture, orchestration, control-plane, daemon]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl.md"]
last_updated: 2026-06-30
---

## Definition
An Agent Control Plane is an architectural pattern where a centralized aggregation layer monitors and manages AI coding agent sessions across multiple agent platforms and machines, providing a single interface for session awareness, interaction, and lifecycle management regardless of where or on what framework agents are running.

## Key Information
- Introduced as the architecture behind [[Cmd+Ctrl]], built by [[MichaelRichman]].
- Three-layer architecture:
  1. **Daemon layer** (open source): runs alongside each agent platform (Claude Code, Cursor, Codex, Gemini, Open Code), monitoring agent lifecycle — when an agent is blocked, needs help, or completes.
  2. **Control plane API**: aggregates all agents regardless of which machine they run on (local dev machine, cloud VM, or both) or which framework they use.
  3. **UI layer**: mobile, web, and watch interfaces that talk to the control plane API for session interaction and notifications.
- The daemon is open source, enabling any agent framework to plug into the control plane.
- Key capability: cross-machine aggregation — sessions on a local Mac and a cloud VM appear in the same unified UI.
- Coding-tool agnostic by design: works with Claude Code, Codex, Cursor, Gemini, GitHub Copilot, and Open Code.
- Contrasts with the default approach of interacting with each agent through its native terminal/IDE interface, which fragments session awareness across multiple windows and tabs.
- Related to the broader concept of [[Agent Orchestration]], but focused specifically on the control and monitoring layer rather than task decomposition and coordination.

## Related
- [[MichaelRichman]] — introduced the pattern via Cmd+Ctrl
- [[Cmd+Ctrl]] — the system implementing the agent control plane
- [[Agent Orchestration]] — related but distinct: task coordination vs. session management
- [[Remote Agent Interaction]] — the user-facing capability enabled by the control plane
- [[Agent Session Management]] — the session tracking feature of the control plane
- [[Agent Notifications]] — push notifications driven by control plane state changes
- [[Agent Daemon Pattern]] — the daemon component of the architecture
- [[ClaudeCode]] — agent platform supported by the control plane
- [[Codex]] — agent platform supported by the control plane
- [[Cursor]] — agent platform supported by the control plane
- [[Gemini]] — agent platform supported by the control plane
- [[GitHubCopilot]] — agent platform supported by the control plane
- [[OpenCode]] — agent platform supported by the control plane
- [[summary-20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl]]
