---
title: "summary-what-are-skills"
type: source
tags: [source, claude-code, skills, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md]
last_updated: 2026-06-23
---

## Core Summary

Skills are markdown files (or folders of instructions, scripts, and resources) that teach Claude how to do something once, and Claude applies that knowledge automatically when relevant. Unlike CLAUDE.md (which loads into every conversation) and slash commands (which require manual invocation), skills load on demand based on description matching. Only the name and description stay in context; the full skill loads when activated. Personal skills live in `~/.claude/skills`; project skills in `.claude/skills/` (shared via version control). Use skills for specialized, task-specific knowledge: code review standards, commit message formats, brand guidelines.

## Key Points

- Skills are automatic and task-specific: Claude matches user requests against skill descriptions and activates matching ones.
- Only the skill name and description consume context window space; the full content loads on demand.
- **Personal skills** (`~/.claude/skills`): follow you across all projects; for preferences, commit message style, documentation format.
- **Project skills** (`.claude/skills/` in repo root): shared via version control; for team standards, brand guidelines.
- **vs. CLAUDE.md:** CLAUDE.md loads into every conversation (persistent context); skills load on demand (task-specific context).
- **vs. Slash commands:** slash commands require manual typing; skills activate automatically.
- Rule of thumb: if you find yourself explaining the same thing to Claude repeatedly, it's a skill waiting to be written.

## Related

- [[ClaudeCode]] — the tool skills extend
- [[CLAUDE-md]] — the persistent alternative to skills
- [[summary-the-claude-md-file]] — related source on CLAUDE.md
