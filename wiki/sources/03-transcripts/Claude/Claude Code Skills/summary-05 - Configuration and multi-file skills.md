---
title: "summary-configuration-and-multi-file-skills"
type: source
tags: [source, claude-code, skills, configuration, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/05 - Configuration and multi-file skills.md]
last_updated: 2026-06-23
---

## Core Summary

Advanced skill configuration goes beyond name and description. Optional fields include `allowed-tools` (restricts which tools Claude can use when the skill is active) and `model` (specifies which Claude model to use). For larger skills, use progressive disclosure: keep essential instructions in `skill.md` (under 500 lines) and link to supporting files (references, scripts, assets) that Claude reads only when needed. Scripts in the skill directory can execute without loading their contents into context -- only the output consumes tokens.

## Key Points

- **Required fields:** `name` (lowercase, numbers, hyphens, max 64 chars, matches directory name) and `description` (max 1024 chars, most important field for matching).
- **`allowed-tools`:** restricts which tools Claude can use when the skill is active; omit for normal permission model. Useful for read-only or security-sensitive workflows.
- **`model`:** specifies which Claude model to use for the skill.
- **Progressive disclosure:** keep `skill.md` under 500 lines; put detailed reference material in separate files that Claude reads only when needed. Like a table of contents rather than the whole document.
- **Directory structure:** `scripts/` for executable code, `references/` for additional documentation, `assets/` for images/templates/data.
- **Scripts:** execute without loading contents into context; only output consumes tokens. Tell Claude to run the script, not read it. Useful for environment validation, data transformations, operations more reliable as tested code than generated code.
- **Description quality:** answer two questions: what does this skill do, and when should Claude use it. Add keywords matching how users phrase requests.

## Related

- [[ClaudeCodeSkills]] — the skills system
- [[summary-01 - What are skills]] — introduction to skills
- [[ContextWindow]] — the memory constraint progressive disclosure manages
