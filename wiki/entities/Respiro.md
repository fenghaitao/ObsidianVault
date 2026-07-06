---
title: "Respiro"
type: entity
tags: [ios-app, hackathon, claude-code, health-wellness, multi-agent, non-technical-builder]
sources: ["raw/01-articles/claude/2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks.md"]
last_updated: 2026-07-04
---

## Definition

Respiro is an iOS stress-management app built by Kostiantyn Vlasenko, a project manager at [[MythicalGames|Mythical Games]] with no prior coding experience, using [[ClaudeCode]]. Unlike fixed-schedule mindfulness apps, Respiro detects stress signals from personal devices in real time and intervenes with a guided breathing exercise (e.g., box breathing) at the moment of stress.

## Key Information

- Originated from the **Built With Opus 4.6 Claude Code Hackathon** (Cerebral Valley, February 2026); went from idea to a full-featured, App Store-ready product in just under six weeks.
- Live on the [[AppleAppStore|Apple App Store]] with hundreds of users.
- **Architecture**: 15+ specialized subagents built and orchestrated personally by Vlasenko — including a TCA architect agent, a Swift developer agent, a Metal specialist agent, and a code-reviewer agent — running in parallel across modules. Vlasenko drew directly on his project-management background, treating subagent orchestration as analogous to managing a human team. See [[MultiAgentSystem]] and [[ClaudeCodeSubagents]].
- **Pivot**: the initial MVP was React Native; became untestable because Vlasenko had no Android device to test on, so Claude Code rewrote the app in Swift from scratch in a few hours.
- Claude also guided third-party integrations (Apple Developer Program, [[Sentry]] for logging, Amplitude for analytics with full funnels/retention tracking) via screenshot-driven, [[ComputerUse|vision-capability]]-assisted walkthroughs, and suggested a practitioner-referral growth strategy (reaching out to psychologists/mindfulness practitioners) that Vlasenko successfully executed.
- Next release planned to add voice-guided practices and motion exercises, from a roadmap Claude helped write.

## Related

- [[ClaudeCode]] — the tool used for the entire build, architecture through shipping
- [[MultiAgentSystem]] — Respiro's 15+ subagent architecture as a production orchestrator-subagent example
- [[ClaudeCodeSubagents]] — subagent orchestration pattern applied here
- [[AppleAppStore]] — distribution platform
- [[MythicalGames]] — creator's employer, later influenced by this project
- [[Sentry]] — logging integration
- [[summary-2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks]] — source article
