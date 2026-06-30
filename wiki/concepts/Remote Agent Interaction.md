---
title: "Remote Agent Interaction"
type: concept
tags: [concept, agents, mobile, remote, workflow, notifications]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl.md"]
last_updated: 2026-06-30
---

## Definition
Remote Agent Interaction is the capability to monitor, respond to, and launch AI coding agent sessions from mobile devices, web browsers, or any platform outside the native terminal/IDE environment. It addresses FOMAT by decoupling the human's location from their ability to engage with agents.

## Key Information
- Core capability of [[Cmd+Ctrl]], the system built by [[MichaelRichman]].
- Encompasses three activities: monitoring session state, responding to agent prompts/questions, and launching new agent sessions.
- Delivered via mobile apps (iPhone, Android), web interface, and Apple Watch.
- Key feature: push notifications when an agent completes or needs input — you don't have to guess when to check back.
- Enables starting sessions from bed or on the go — Michael Richman starts his day issuing prompts from his phone before reaching his dev machine.
- Sessions started remotely appear in the terminal for seamless continuation; responses from the terminal appear in the mobile UI.
- Works across all configured agent platforms (Claude Code, Codex, Cursor, Gemini, GitHub Copilot, Open Code).
- The need for remote interaction grows as agent task durations extend from minutes to hours to days.
- Validated by industry: Anthropic released remote control and teleportation features, and Cursor released a mobile solution shortly after Cmd+Ctrl was built.
- Represents a shift from the assumption that coding agents are interacted with only at a desk, to the assumption that agents are always-available resources needing always-available human oversight.

## Related
- [[MichaelRichman]] — introduced the concept and built Cmd+Ctrl
- [[Cmd+Ctrl]] — the system implementing remote agent interaction
- [[FOMAT (Fear of Missing Agent Time)]] — the problem remote interaction solves
- [[Agent Choreography]] — the workflow remote interaction enables
- [[Agent Control Plane]] — architectural pattern enabling remote interaction
- [[Agent Notifications]] — the push notification mechanism
- [[Agent Session Management]] — tracking sessions accessible from anywhere
- [[Anthropic]] — released competing remote control features
- [[Cursor]] — released competing mobile solution
- [[summary-20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl]]
