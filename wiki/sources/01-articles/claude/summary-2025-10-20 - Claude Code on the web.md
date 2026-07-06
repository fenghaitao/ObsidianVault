---
title: "summary-2025-10-20 - Claude Code on the web"
type: source
tags: [source, claude-code, cloud, sandboxing, mobile]
sources: ["raw/01-articles/claude/2025-10-20 - Claude Code on the web.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic launched Claude Code on the web (research preview), letting developers delegate coding tasks from a browser instead of a terminal. Sessions connect to GitHub repositories and run in isolated, Anthropic-managed cloud sandboxes with real-time progress tracking and steering, enabling multiple parallel tasks across repositories with automatic PR creation. The same capability shipped to the iOS app for on-the-go use. An update on November 12, 2025 expanded availability to Team and Enterprise premium-seat users (on by default, admin-toggleable), in addition to Pro and Max.

## Key Points

- Best suited for answering codebase/repo-mapping questions, bugfixes and routine well-defined tasks, and backend changes verifiable via test-driven development.
- Each session runs in an isolated sandbox with network and filesystem restrictions; git interactions go through a secure proxy service scoping repository access rather than exposing raw credentials.
- Custom network configuration lets teams choose which domains the sandbox can reach (e.g., allowing npm registry access to run tests).
- Cloud sessions share rate limits with all other Claude Code usage.
- Available on iOS as an early preview alongside the web interface.

## Related

- [[ClaudeCode]] — the tool this feature extends to browser and mobile
- [[Sandboxing]] — the isolation architecture underlying cloud sessions
- [[ClaudeIOSApp]] — mobile app now supporting Claude Code sessions
- [[GitHub]] — repository platform Claude Code on the web connects to
