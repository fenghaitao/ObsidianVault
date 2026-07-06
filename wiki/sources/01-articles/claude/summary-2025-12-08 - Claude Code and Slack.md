---
title: "summary-2025-12-08 - Claude Code and Slack"
type: source
tags: [source, claude-code, slack, integration]
sources: ["raw/01-articles/claude/2025-12-08 - Claude Code and Slack.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic added the ability to delegate coding tasks to [[ClaudeCode]] directly from [[Slack]] (beta, research preview): tagging @Claude on a bug report or feature request automatically spins up a Claude Code on the web session using surrounding channel/thread context, posts status updates back to the thread, and links to the session and an option to open a PR — all without leaving Slack.

## Key Points

- Builds on the existing Claude app for Slack, relaying tasks to [[ClaudeCode|Claude Code on the web]] rather than introducing a new integration surface.
- When @Claude is mentioned, Claude determines whether the message is a coding task (or the user can manually specify one), gathers context from recent channel/thread messages, and auto-selects which authenticated repository to run the task against.
- Use cases: bug investigation/fixes as soon as reported, quick code reviews/modifications from team feedback, and collaborative debugging using error reproductions or user reports shared in-thread.
- **Requirements**: the Claude Slack app installed via the Slack App Marketplace, plus access to Claude Code on the web (since that's where sessions actually run).

## Related

- [[ClaudeCode]] — the tool sessions are delegated to (via Claude Code on the web)
- [[Slack]] — the platform this integration extends
