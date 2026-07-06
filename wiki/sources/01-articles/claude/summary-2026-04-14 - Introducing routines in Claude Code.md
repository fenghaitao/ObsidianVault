---
title: "summary-2026-04-14 - Introducing routines in Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-14 - Introducing routines in Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced "routines" in Claude Code (research preview, April 14, 2026): a Claude Code automation configured once — prompt, repo, and connectors — that then runs repeatedly on a schedule, from an API call, or in response to an event, executing on Claude Code's web infrastructure so it doesn't depend on a laptop being open. Routines formalize what developers previously stitched together themselves with cron jobs, custom infrastructure, and MCP servers, and existing `/schedule` CLI tasks are automatically treated as scheduled routines. Three trigger mechanisms are supported: time-based schedules (hourly/nightly/weekly cadences), API-triggered calls (each routine gets its own endpoint and auth token, returning a session URL), and GitHub repository event subscriptions (one session opened per matching PR, with follow-up comments/CI failures fed into that same session). Routines are available to Claude Code users on Pro, Max, Team, and Enterprise plans with Claude Code on the web enabled, created via claude.ai/code or `/schedule` in the CLI. Usage draws down subscription limits like interactive sessions, with additional daily caps (Pro: 5/day, Max: 15/day, Team/Enterprise: 25/day) and the option to run extra routines via extra usage.

## Key Points

- A routine = prompt + repo + connectors, configured once, then triggered repeatedly — runs on Claude Code's cloud/web infrastructure, not the local machine.
- Three trigger types: (1) recurring schedule (e.g. "Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR"), (2) API call (POST a message to a routine's dedicated endpoint + auth token, get back a session URL — e.g. reading an alert payload and posting a triage summary to #oncall), (3) GitHub repo event subscription (e.g. flagging PRs touching `/auth-provider` and posting summaries to #auth-changes; Claude opens one session per matching PR and continues feeding it updates like comments and CI failures).
- Existing `/schedule` CLI tasks are now surfaced as scheduled routines — no separate migration needed.
- Anthropic plans to expand webhook-based routines to more event sources beyond GitHub in the future.
- Availability: Pro, Max, Team, and Enterprise plans, gated on Claude Code on the web being enabled; create via claude.ai/code or `/schedule` in the CLI.
- Daily routine-run limits: Pro up to 5/day, Max up to 15/day, Team/Enterprise up to 25/day; routines consume subscription usage like interactive sessions, and extra usage can cover runs beyond the daily caps.
- Anomaly: the raw source is scraped marketing-page boilerplate — several sentences are duplicated verbatim (e.g. the opening description repeats twice), a "common patterns have emerged" sentence is left as a dangling fragment with no actual list following it, and the page ends with unrelated newsletter-signup boilerplate ("Get the developer newsletter..."). No prompt-injection-style content was present, just page-scrape artifacts; nothing beyond noting this was needed.

## Related

- [[ClaudeCode]] — the product routines ship within
- [[ClaudeCodeRoutines]] — existing concept page on Claude Code routines/scheduled automation, extended with this article's research-preview launch details
