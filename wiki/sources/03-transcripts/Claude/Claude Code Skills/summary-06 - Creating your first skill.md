---
title: "summary-creating-your-first-skill"
type: source
tags: [source, claude-code, skills, tutorial, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/06 - Creating your first skill.md]
last_updated: 2026-06-23
---

## Core Summary

Creating a skill involves making a directory with a `skill.md` file containing YAML frontmatter (name, description) and instructions. Claude Code scans four locations at startup (enterprise, personal, project, plugins), loading only names and descriptions. When a user request semantically matches a skill description, Claude asks for confirmation before loading the full content. Priority hierarchy for name conflicts: enterprise > personal > project > plugins. To update, edit `skill.md` and restart Claude Code. To remove, delete the directory.

## Key Points

- **Creation:** create a directory named after the skill inside the skills directory, then create `skill.md` with YAML frontmatter (name, description) and instructions after the second `---`.
- **Startup scan:** Claude Code scans enterprise paths, personal `~/.claude/skills`, project `.claude/skills`, and installed plugins. Only names and descriptions are loaded, not full content.
- **Matching:** Claude compares user requests against skill descriptions semantically; if intent overlaps, it asks for confirmation before loading the full skill.
- **Priority hierarchy:** enterprise (managed settings) > personal (home directory) > project (repo `.claude/skills`) > plugins.
- **Conflict avoidance:** use descriptive names (e.g., "front-end PR review" instead of "review") to avoid enterprise or higher-priority overrides.
- **Updates:** edit `skill.md` and restart Claude Code for changes to take effect.

## Related

- [[ClaudeCodeSkills]] — the skills system
- [[summary-01 - What are skills]] — introduction to skills
- [[summary-05 - Configuration and multi-file skills]] — advanced configuration
- [[ClaudeCode]] — the tool skills extend
