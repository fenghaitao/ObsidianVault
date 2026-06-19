---
title: "Zapier"
type: entity
tags: [tool, automation, integrations, mcp, second-brain]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
last_updated: 2026-06-20
---

## Definition

Zapier is a workflow-automation platform connecting thousands of apps. In [[ColeMedin]]'s [[SecondBrain]], he uses the Zapier [[ModelContextProtocol]] server to connect his agent to Gmail, Google Calendar, Slack, and Asana — wrapped as a [[ClaudeSkills|skill]] (via his MCP-to-Skill pattern) to avoid context bloat.

## Key Information

- **Used via its MCP server** — Zapier exposes a Model Context Protocol server giving access to its huge integration catalog.
- **Wrapped as a skill, not mounted directly** — Cole's [[SecondBrain]] uses the MCP-to-Skill pattern: the Zapier MCP's ~20 tools would bloat the context window if mounted directly ([[ProgressiveDisclosure]] problem). Wrapping it as a [[ClaudeSkills|skill]] keeps the tool descriptions dormant until needed.
- **Permission control** — Zapier lets you select which individual tools are exposed. Cole restricts his second brain to *read* operations (it can check his calendar and Asana tasks, but he doesn't grant send/write by default) — a [[LethalTrifecta]]-conscious choice.
- **Connects the second brain to where Cole works** — Gmail, Calendar, Slack, Asana. So the agent can pull a meeting from Calendar or a task from Asana and tie it to research in [[Obsidian]].

## Related

- [[SecondBrain]] — where Cole uses Zapier
- [[ModelContextProtocol]] — Zapier's integration mechanism
- [[ClaudeSkills]] — Cole wraps the Zapier MCP as a skill
- [[ProgressiveDisclosure]] — why wrapping-as-skill beats mounting-directly
- [[LethalTrifecta]] — why Cole restricts Zapier to read-only
- [[ColeMedin]] — user
- [[summary-second-brain-with-claude-code-obsidian-skills]] — primary source
