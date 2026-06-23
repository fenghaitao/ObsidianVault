---
title: "VercelAgentBrowser"
type: entity
tags: [tool, vercel, browser-automation, testing, end-to-end, validation]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now).md"
last_updated: 2026-06-20
---

## Definition

The Vercel Agent Browser CLI is a browser-automation tool that lets a coding agent spin up a real browser and test a web application the way a user would — clicking through flows, filling forms, observing results. [[ColeMedin]] uses it as the **end-to-end self-validation** layer of his agentic build process and calls it "a big upgrade over other tools I've used in the past, like the Playwright or Puppeteer MCP servers."

## Key Information

- **Purpose**: autonomous end-to-end testing. After the implementation phase, the agent drives the browser through every user journey defined in the plan (e.g. register an account, purchase tokens, chat with the agent, confirm token deductions), finds issues, and fixes them — so by the time control returns to the human, everything is genuinely tested.
- **Headed vs headless**: runs headless by default; can run **headed** so a human can watch the agent click through journeys live.
- **Where it fits**: it's the most powerful layer of [[ValidationGates]] — Cole insists validation (lint, type-check, unit tests, and especially e2e) be defined **upfront in the plan** so the agent self-validates before reporting done. It catches the "derpy glitches" and real integration bugs that no plan, however clear, fully prevents.
- **Model quirk**: Opus 4.6 frequently *skipped* the e2e step for Cole unless explicitly demanded (Opus 4.5 ran it automatically) — a reminder that prompts/commands often need tuning when the underlying model changes.

### The validation micro-loop

Per `summary-self-healing-e2e-validation`, within each user journey the agent runs a tight loop: **take a snapshot** (to understand the current page) → **query the database** to verify state → **interact** with an element → **re-verify** the resulting record → **screenshot** (the agent image-analyzes UI quality; humans review the screenshots after). Cole's `/e2e-test` skill **auto-installs** the CLI, making it drop-in on any frontend codebase.

## Related

- [[ValidationGates]] — the e2e layer this tool powers
- [[ClaudeCode]] — the agent that drives it
- [[AgentTeams]] — implementation by a team, validation by this tool
- [[ColeMedin]] — advocate
- [[summary-20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)]] — primary source
- [[summary-20260226 - This One Command Makes Coding Agents Find All Their Mistakes (Use it Now)]] — the /e2e-test skill built on this CLI
