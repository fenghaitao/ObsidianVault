---
title: "ClaudeCodeSkills"
type: concept
tags: [claude-code, skills, automation, context]
sources: [raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md, raw/03-transcripts/Claude/Claude Code Skills/02 - Troubleshooting skills.md, raw/03-transcripts/Claude/Claude Code Skills/03 - Sharing skills.md, raw/03-transcripts/Claude/Claude Code Skills/04 - How skills compare to other Claude Code features.md, raw/03-transcripts/Claude/Claude Code Skills/05 - Configuration and multi-file skills.md, raw/03-transcripts/Claude/Claude Code Skills/06 - Creating your first skill.md]
last_updated: 2026-06-23
---

## Definition

Claude Code skills are markdown-based instruction files that teach Claude specialized, task-specific knowledge once and have it applied automatically when relevant. They load on demand via description matching, keeping only a name and description in the context window until activated.

## Key Information

- **Automatic activation:** Claude matches user requests against available skill descriptions and activates matching ones without manual invocation.
- **Context efficiency:** only the skill name and description stay in context; full content loads on demand when activated.
- **Storage locations:** personal skills in `~/.claude/skills` (follow you across projects); project skills in `.claude/skills/` (shared via version control).
- **Comparison to other mechanisms:**
  - CLAUDE.md: loads into every conversation (persistent); skills load on demand (task-specific).
  - Slash commands: require manual typing; skills activate automatically.
  - MCP: tools load into context; skills only load name/description.
- **Use cases:** code review standards, commit message formats, brand guidelines, documentation formats, any repeated explanation to Claude.

### Sharing and Distribution

- **Project sharing:** commit to `.claude/skills` in repo; team gets them automatically on pull.
- **Plugin distribution:** create a `skills` directory in a plugin project; distribute via marketplace for community use.
- **Enterprise deployment:** admins deploy via managed settings; enterprise skills take highest priority and override all others with the same name.
- **Priority hierarchy:** enterprise > personal > project > plugins. Use descriptive names to avoid conflicts.

### Sub-agents and Skills

- Built-in agents (explorer, plan, verify) cannot access skills at all.
- Custom sub-agents only get skills explicitly listed in the `skills` field of their `agent.md` file.
- Skills load when the sub-agent starts, not on demand. Only list skills always relevant to the sub-agent's purpose.

### Advanced Configuration

- **`allowed-tools`:** restricts which tools Claude can use when the skill is active (e.g., read-only for security-sensitive workflows).
- **`model`:** specifies which Claude model to use for the skill.
- **Progressive disclosure:** keep `skill.md` under 500 lines; link to supporting files in `references/`, `scripts/`, `assets/` that load only when needed.
- **Scripts:** execute without loading contents into context; only output consumes tokens.
- **Description quality:** answer "what does this skill do" and "when should Claude use it"; add trigger phrases matching how users phrase requests.

## Related

- [[summary-01 - What are skills]] — source summary
- [[summary-02 - Troubleshooting skills]] — troubleshooting guide
- [[summary-03 - Sharing skills]] — sharing and distribution
- [[summary-04 - How skills compare to other Claude Code features]] — comparison with other mechanisms
- [[summary-05 - Configuration and multi-file skills]] — advanced configuration
- [[summary-06 - Creating your first skill]] — creation tutorial
- [[ClaudeCode]] — the tool skills extend
- [[CLAUDE-md]] — the persistent alternative
- [[ModelContextProtocol]] — similar tool integration mechanism
