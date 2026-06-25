---
title: "CLAUDE.md"
type: concept
tags: [claude-code, instructions, memory, configuration]
sources: []
last_updated: 2026-06-25
---

## Definition

CLAUDE.md is the instruction file pattern used by Claude Code to persist project-level rules, conventions, and preferences across sessions. It is human-managed (unlike Auto Memory, which is Claude-managed). Acts as the "system prompt" for the agent — defines coding conventions, design system rules, testing requirements, and workflow preferences.

## Key Information

- Human-managed instruction file, distinct from Auto Memory (Claude-managed)
- Read by Claude Code at the start of every session
- Used by Brian Casel to enforce design system rules: "always check the design system first, don't invent ad-hoc hex values"
- Used by Cole Medin for spec-driven development workflows
- Part of the "filesystem as configuration" pattern — no API, no dashboard, just a markdown file

## Related

- [[ClaudeCode]] — the tool that reads it
- [[AutoMemory]] — the Claude-managed counterpart
- [[DesignSystem]] — enforced through CLAUDE.md directives
- [[SpecDrivenDevelopment]] — methodology using CLAUDE.md
