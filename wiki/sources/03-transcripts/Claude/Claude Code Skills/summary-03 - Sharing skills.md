---
title: "summary-sharing-skills"
type: source
tags: [source, claude-code, skills, sharing, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/03 - Sharing skills.md]
last_updated: 2026-06-23
---

## Core Summary

Skills become more valuable when shared across teams. Three sharing methods: (1) commit to repository in `.claude/skills` for automatic team access, (2) distribute as plugins via marketplace for cross-project community use, (3) enterprise deployment through managed settings for mandatory organization-wide standards (highest priority, overrides all others). Sub-agents don't inherit skills automatically: built-in agents can't access skills at all, and custom sub-agents only get skills explicitly listed in their `agent.md` skills field. Skills load when the sub-agent starts, not on demand.

## Key Points

- **Project sharing:** commit skills to `.claude/skills` in the repo; team gets them on next pull. Best for team coding standards and project-specific workflows.
- **Plugin distribution:** create a `skills` directory in a plugin project; distribute via marketplace. Best for community-shareable, non-project-specific functionality.
- **Enterprise deployment:** admins deploy via managed settings; enterprise skills take highest priority and override personal, project, and plugin skills with the same name. For mandatory standards, security, compliance.
- **Sub-agents and skills:** built-in agents (explorer, plan, verify) cannot access skills. Custom sub-agents only get skills explicitly listed in the `skills` field of their `agent.md` file. Skills load at sub-agent start, not on demand.
- Pattern: different sub-agents get different skills (e.g., front-end reviewer vs. back-end reviewer).

## Related

- [[ClaudeCodeSkills]] — the skills system
- [[summary-01 - What are skills]] — introduction to skills
- [[ClaudeCode]] — the tool skills extend
