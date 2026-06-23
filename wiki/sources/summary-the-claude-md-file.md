---
title: "summary-the-claude-md-file"
type: source
tags: [source, claude-code, claude-md, memory, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md]
last_updated: 2026-06-23
---

## Core Summary

The CLAUDE.md file provides Claude Code with persistent project memory, acting as an onboarding script that is automatically read at the start of every session. Without it, Claude must re-explore the codebase and make assumptions. It lives at the project root, is shareable via version control, and its contents are appended to every prompt. A hierarchy exists: project-level CLAUDE.md, user-level CLAUDE.md (personal preferences across all projects), and Claude can save corrections to memory on request.

## Key Points

- CLAUDE.md is a markdown file at the project root; Claude Code reads it automatically every session.
- Contents are appended to every user prompt, giving Claude persistent context about the project.
- Use `/init` to have Claude generate a CLAUDE.md based on the codebase.
- Typical contents: tech stack, commands (dev server, test, lint), code style preferences, architectural conventions.
- Hierarchy: project-level CLAUDE.md (shared via version control), user-level CLAUDE.md (personal, across all projects), and memory saved on request.
- Recommended workflow: start without a CLAUDE.md, note where you constantly course-correct, then add only those items to keep the file compact.
- The difference between a frustrating and productive Claude Code session often comes down to CLAUDE.md context.

## Related

- [[ClaudeCode]] — the tool that reads CLAUDE.md
- [[summary-your-first-claude-code-prompt]] — prompting best practices
- [[ContextWindow]] — related memory constraint concept
