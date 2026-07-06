---
title: "summary-2026-03-23 - Put Claude to work on your computer"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-03-23 - Put Claude to work on your computer.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic has extended Claude Cowork and Claude Code with a new "computer use" capability that lets Claude directly point, click, and navigate a user's screen — opening files, using the browser, and running dev tools — when no dedicated connector exists for the task, without any setup required. It works alongside Dispatch, a recently launched feature that lets people assign Claude tasks from their phone and pick up finished work later on desktop, enabling autonomous end-to-end workflows (e.g., a morning briefing built while commuting, or IDE changes/tests/a pull request completed while the user is away). Claude prefers precise tools like connectors to Slack or Google Calendar first, falling back to direct browser/mouse/keyboard/screen control, and always requests explicit permission before touching a new application. Anthropic frames this as an early research preview with safety work already built in — automatic in-model activation scanning to catch prompt-injection-driven misuse, a user override to stop Claude at any point, and some apps blocked by default — while cautioning that computer use is slower and less reliable than Claude's coding/text abilities and recommending it be limited to trusted apps and non-sensitive data for now. It launches for Claude Pro and Max subscribers on macOS and Windows, requiring the desktop app to be enabled and running.

## Key Points

- Computer use lets Claude control a local computer (point/click/navigate open apps, browser, dev tools) as a fallback when no connector/tool exists for a task — no setup required.
- Available now in research preview for Claude Pro and Max subscribers, on macOS and Windows, via the desktop app.
- Claude prioritizes precise integrations (e.g., Slack, Google Calendar connectors) before resorting to full screen control; it will scroll, click to open, and explore as needed.
- Always asks permission before accessing a new application; some apps are off-limits by default given the sensitivity of screen/keyboard/mouse control.
- Safety measures include automatic scanning of internal model activations to detect prompt-injection-style misuse, plus a user-initiated stop-at-any-time control.
- Pairs with Dispatch (launched the prior week in Claude Cowork, now also in Claude Code), which lets users assign tasks from their phone and later review completed work on desktop — e.g., automatically checking email each morning, pulling weekly metrics, or spinning up a Cowork/Code session for a report or PR.
- Explicitly framed as early and imperfect: complex tasks may need a second try, and screen-based interaction is slower than direct integrations; shared as a research preview to learn where it works and where it falls short, echoing the same approach Anthropic took with Claude Cowork.

## Related

- [[ClaudeCowork]] — product gaining the new computer use capability
- [[ClaudeCode]] — product gaining the new computer use capability
- [[Dispatch]] — the phone-based task assignment feature paired with computer use
- [[ComputerUse]] — the underlying capability this article introduces into Cowork/Code
- [[PromptInjection]] — the safety risk mitigated via in-model activation scanning
- [[ClaudeMax]] — plan tier with access to the feature
- [[Anthropic]] — the company shipping the feature
