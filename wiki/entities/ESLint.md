---
title: "ESLint"
type: entity
tags: [tool, linting, javascript, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
ESLint is a static code analysis tool for JavaScript/TypeScript. In the Claude Agent SDK context, it exemplifies how the bash tool lets agents discover and use project-specific tooling without needing custom tools for each use case.

## Key Information
- Used as an example of how Claude Code via bash can discover a project's linting setup and run it
- The agent can run `npm run lint` if a lint script exists, or even offer to install ESLint if none is configured
- Demonstrates the power of bash over custom tools: instead of building a "lint tool," the agent uses the existing ecosystem

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[BashTool]] — the mechanism enabling ESLint usage
- [[ClaudeCode]] — the agent that uses ESLint via bash
