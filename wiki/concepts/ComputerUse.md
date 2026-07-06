---
title: "ComputerUse"
type: concept
tags: [ai-agent, computer-use, automation, claude-cowork, claude-code]
sources: [raw/01-articles/claude/2026-03-23 - Put Claude to work on your computer.md, "raw/01-articles/claude/2026-05-13 - Best practices for computer and browser use with Claude.md"]
last_updated: 2026-07-04
---

## Definition

Computer use is a capability that lets Claude directly perceive and control a user's desktop — pointing, clicking, and navigating open applications, the browser, and dev tools — to complete tasks when no dedicated connector or tool exists, without requiring any setup.

## Key Information

- Launched (research preview) in [[ClaudeCowork]] and [[ClaudeCode]] on 2026-03-23, for Claude Pro and Max subscribers on macOS and Windows; requires the desktop app enabled and running.
- **Tool-priority order**: Claude reaches for the most precise tool first (e.g., connectors to Slack or Google Calendar); only when no connector exists does it fall back to direct browser/mouse/keyboard/screen control, scrolling and clicking to explore as needed.
- Always asks for explicit user permission before accessing a new application; some apps are off-limits by default.
- **Safeguards**: automatic scanning of internal model activations to detect prompt-injection-style misuse in real time (see [[PromptInjection]]); a user override to stop Claude at any point.
- Explicitly early-stage: slower than direct integrations, complex tasks may need a second attempt; Anthropic recommends starting with trusted apps and avoiding sensitive data.
- Pairs with [[Dispatch]]: since computer use lets Claude act autonomously on-screen, a task assigned remotely via Dispatch can be completed end-to-end while the user is away (e.g., a morning briefing, or IDE changes + tests + PR).
- **Best practices (May 2026)**: pre-downscale screenshots to the API's internal limits before sending — the single highest-impact fix for click accuracy, since oversized images get silently downscaled server-side while coordinates are still returned in the developer-declared display space. 4.6-family limit: 1568px long edge / ~1.15MP; [[Claude4.7Opus|Opus 4.7]] supports 2576px / ~3.75MP. Recommended defaults: 1280x720 for the 4.6 family, 1080p for Opus 4.7. Place text instructions before the image in the content array. For small targets (checkboxes, tray icons), enable the `enable_zoom` tool option, enlarge UI targets, or prefer keyboard navigation over clicking.
- **Model choice for clicking**: Sonnet 4.6 is the recommended default (best balance of precision, reasoning, cost); Opus 4.7 narrows the precision gap with Sonnet while adding stronger reasoning and higher-resolution input; Haiku 4.5 for latency-sensitive workloads. See [[AdaptiveThinking]] for effort-level tuning specific to computer-use tasks (medium effort is the general sweet spot; max is not recommended).
- **"Teach Mode"**: a workflow-recording pattern (used internally in [[ClaudeInChrome]]) where a human demonstration — screenshots, click coordinates/selectors, optional voice narration — is captured as a reusable `SavedWorkflow` and replayed adaptively as context on future requests, rather than replayed as literal coordinate playback. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-2026-03-23 - Put Claude to work on your computer]] — source summary
- [[ClaudeCowork]] — first product to ship computer use
- [[ClaudeCode]] — second product to ship computer use
- [[Dispatch]] — phone-based task assignment paired with computer use
- [[BrowserUseAgent]] — related, narrower agent pattern (browser-only perception/action) that computer use generalizes beyond the browser
- [[PromptInjection]] — primary safety risk; mitigated here via activation scanning
- [[ClaudeMax]] — plan tier with access
- [[Anthropic]] — developer of the capability
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — best-practices deep dive (resolution limits, effort tuning, prompt injection defenses, context management, Teach Mode)
