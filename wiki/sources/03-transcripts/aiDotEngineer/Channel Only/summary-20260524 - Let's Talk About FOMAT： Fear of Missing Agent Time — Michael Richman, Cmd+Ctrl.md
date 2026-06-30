---
title: "summary-20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl"
type: source
tags: [source, transcript, ai-engineering, coding-agents, agent-orchestration, mobile, remote, productivity]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Let's Talk About FOMAT： Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl.md"]
last_updated: 2026-06-30
---

## Core Summary
Michael Richman, engineering leader at Bitly, introduces FOMAT (Fear of Missing Agent Time) — the anxiety of being away from your dev machine when an AI coding agent needs input, blocks on a question, or completes a task. He presents Cmd+Ctrl (Command and Control), an open-source system he built that provides a single-pane-of-glass mobile/web interface for monitoring, interacting with, and launching AI coding agent sessions across multiple platforms (Claude Code, Codex, Cursor, Gemini, GitHub Copilot) from anywhere. He argues that as agent task durations grow from minutes to hours to days, the traditional "flow state" of deep individual focus transforms into agent choreography — orchestrating multiple parallel agents — and remote interaction becomes critical.

## Key Points
- FOMAT manifests in two forms: having an idea for an agent task while away from your dev machine, and realizing an agent has been blocked waiting for input while you stepped away.
- Current coding agent tasks take 5–45 minutes, but as agents improve, task windows will stretch to hours and days, making "check back in a bit" infeasible.
- Cmd+Ctrl addresses four needs: remote session interaction, session management across agents, push notifications for agent state changes, and launching new sessions from anywhere.
- The system consists of a daemon layer (open source) running alongside each agent platform, a control plane API aggregating all agents, and a UI (mobile, web, watch).
- Cmd+Ctrl is coding-tool agnostic: it works with Claude Code, Codex, Cursor, Gemini, GitHub Copilot, and Open Code. The daemon layer is open source so any agent framework can plug in.
- It aggregates agents across machines — sessions running on a local Mac and a cloud VM both appear in the same UI.
- Key mobile features: subscribing to sessions for push notifications, viewing session history, an overview dashboard with stand-up-style summaries of recent sessions, and starting new sessions from mobile.
- The new "flow" in the agentic world is agent choreography: moving between parallel agents, unblocking one, redirecting another — the elegance comes from the orchestration and results.
- Managing multiple agent sessions has high cognitive load and is exhausting. Time away from agents is when the best ideas often emerge.
- Systems that let you reach agents during breaks, from anywhere, are how we truly alleviate FOMAT.
- Anthropic recently released remote control and teleportation features; Cursor released a mobile solution 2 days before this talk — validating the need for the space.
- AgentCraft (presented earlier the same day) was noted as a gaming-inspired take on similar session management challenges.

## Related
- [[MichaelRichman]] — speaker, engineering leader at Bitly, creator of Cmd+Ctrl
- [[Bitly]] — the link shortener company
- [[Cmd+Ctrl]] — the system for remote agent interaction
- [[ClaudeCode]] — coding agent supported by Cmd+Ctrl
- [[Codex]] — coding agent supported by Cmd+Ctrl
- [[Cursor]] — coding agent/IDE supported by Cmd+Ctrl
- [[Gemini]] — coding agent supported by Cmd+Ctrl
- [[GitHubCopilot]] — coding agent supported by Cmd+Ctrl
- [[OpenCode]] — coding agent supported by Cmd+Ctrl
- [[Anthropic]] — released remote control and teleportation features
- [[AgentCraft]] — gaming-inspired agent orchestrator presented same day
- [[MattPocock]] — referenced on the importance of time away from agents
- [[SimonWillison]] — referenced for his interview on Lenny's Podcast about AI productivity
- [[LennyPodcast]] — hosted Simon Willison interview on AI productivity
- [[FOMAT (Fear of Missing Agent Time)]] — core concept introduced in this talk
- [[Agent Choreography]] — the new form of flow in the agentic world
- [[Remote Agent Interaction]] — interacting with agents from mobile or web
- [[Agent Control Plane]] — centralized aggregation layer for multiple agent platforms
- [[Agent Session Management]] — tracking sessions across platforms and machines
- [[Agent Idleness]] — agents blocked waiting for human input
- [[Agent Parallelism]] — running multiple agents simultaneously
- [[Agent Orchestration]] — coordinating multiple agents
- [[aiDotEngineer]] — conference/YouTube channel hosting the talk
