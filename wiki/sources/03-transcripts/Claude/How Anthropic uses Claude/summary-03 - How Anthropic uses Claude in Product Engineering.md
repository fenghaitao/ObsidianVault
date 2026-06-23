---
title: "How Anthropic Uses Claude in Product Engineering"
type: source
tags: [anthropic, product-engineering, claude-code, playwright-mcp, frontend]
sources: [raw/03-transcripts/Claude/How Anthropic uses Claude/03 - How Anthropic uses Claude in Product Engineering.md]
last_updated: 2026-06-23
---

## Core Summary

An Anthropic product engineer describes using Claude Code with the Playwright MCP to implement an Excel rendering feature for Claude.ai. As a backend engineer working on frontend code, Claude Code helped onboard onto an unfamiliar codebase, read the design spec, preview the unimplemented feature via Playwright, implement changes, and iteratively validate them. The key theme is Claude Code enabling engineers to work across stack boundaries and focus on higher-level system design and strategy rather than implementation details.

## Key Points

- **Excel renderer implementation:** Claude Code read the design doc, previewed the unimplemented feature via Playwright MCP, implemented code changes, and validated iteratively.
- **Cross-stack capability:** Backend engineer successfully implemented a frontend feature by letting Claude Code handle codebase onboarding and implementation.
- **Playwright MCP integration:** Claude Code starts the app, takes screenshots of the current state, implements changes, and validates visually — closing the development loop.
- **Focus shift:** Engineers can focus on system-level decisions, strategy, trade-offs, and cross-team coordination rather than implementation mechanics.
- **"Dream bigger":** Claude Code removes language and stack proficiency barriers, opening possibilities previously limited by individual skill sets.

## Related

- [[Anthropic]] — the company using Claude internally
- [[ClaudeCode]] — the tool used for implementation
- [[ModelContextProtocol]] — Playwright MCP for browser automation
