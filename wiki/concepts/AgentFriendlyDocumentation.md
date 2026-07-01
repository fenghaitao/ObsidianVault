---
title: "AgentFriendlyDocumentation"
type: concept
tags: [documentation, agents, platform-engineering, agents.md, skills]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Agent-friendly documentation is documentation structured and delivered in ways that AI coding agents can efficiently consume, discover, and apply. It goes beyond human-readable prose to include machine-consumable formats, agent-specific instruction files, and API-accessible documentation endpoints.

## Key Information
- Juan Herreros Elorza identifies documentation as "crucially important" for agent-ready platforms — agents need structured, discoverable documentation, not scattered wiki pages
- Three documentation strategies:
  1. **Co-located docs**: keep documentation next to the code it documents (effective for smaller repos)
  2. **Centralized docs**: for platform teams, maintain a central documentation hub agents can browse and discover
  3. **API-accessible docs**: provide specific documentation bits over API rather than requiring agents to parse full HTML pages
- Agent-specific documentation files: agents.md, CLAUDE.md, cursor_instructions.md — describe how an agent should build, test, deploy, and verify in a specific repository
- Skills as codified conventions: markdown documents that tell the agent "when you do this type of task, you should do it like that"
- General agent instructions can apply across systems, with project-specific overrides
- The documentation problem was already bad for humans ("many of us have written documentation, put it somewhere, and then were unable to find it") — agents make it worse because they cannot compensate with tribal knowledge

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[AgentReadyPlatform]] — the goal state
- [[AgentsDotMd]] — agent-specific project configuration files
- [[Skills]] — reusable agent playbooks
- [[AgentFriendlyDocumentation]] — structured documentation approach
- [[PlatformEngineering]] — parent discipline
- [[ContextEngineering]] — related practice for curating agent context
