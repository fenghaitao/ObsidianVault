---
title: "summary-2025-12-18 - Skills for organizations, partners, the ecosystem"
type: source
tags: [source, skills, admin, ecosystem, open-standard]
sources: ["raw/01-articles/claude/2025-12-18 - Skills for organizations, partners, the ecosystem.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic expanded [[ClaudeCodeSkills|Skills]] (introduced in October 2025) with organization-wide admin management, a directory of partner-built skills, easier creation/editing tools, and publication of Agent Skills as an open, cross-platform standard.

## Key Points

- **Org-wide management**: Claude Team/Enterprise admins provision skills centrally from admin settings; admin-provisioned skills are enabled by default for all users, though individuals can still toggle them off.
- **Easier authoring**: describe what's wanted and Claude helps build the skill, or write instructions directly; upload skill folders or use skill-creator for complex workflows; Claude can also edit existing skills, and new previews show full skill contents before enabling.
- **Skills directory**: a growing collection of partner-built skills (Notion, Canva, Figma, Atlassian, and others) at claude.com/connectors; admins can provision these org-wide, giving teams instant workflows for tools they already use with no custom development.
- **Open standard**: Anthropic published **Agent Skills** at agentskills.io — modeled on the same portability philosophy as [[ModelContextProtocol|MCP]] — so the same skill works across Claude and other AI platforms, with early ecosystem adoption already underway.
- **Access requirements**: skills require Code Execution and File Creation enabled; available via Claude Apps (Settings > Capabilities > Skills), Claude Code (plugin directory or repository check-in), and the Claude Developer Platform (`/v1/skills` endpoint).

## Related

- [[ClaudeCodeSkills]] — the feature this article expands with org-wide management and the open standard
- [[ModelContextProtocol]] — the precedent portable-standard this article's "open standard" framing draws on
