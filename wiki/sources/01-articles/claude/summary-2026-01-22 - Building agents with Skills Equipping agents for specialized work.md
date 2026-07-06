---
title: "summary-2026-01-22 - Building agents with Skills Equipping agents for specialized work"
type: source
tags: [source, skills, agent-architecture, progressive-disclosure]
sources: ["raw/01-articles/claude/2026-01-22 - Building agents with Skills Equipping agents for specialized work.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic explains why it stopped building domain-specific agents (a coding agent, a research agent, a finance agent, each with its own scaffolding) and converged on one general-purpose agent (Claude Code, using code as an interface for almost any digital work) equipped with Skills for domain expertise instead — because general capability isn't the same as expertise, much like a math genius isn't the same as an experienced tax professional.

## Key Points

- **Three-tier progressive disclosure**: metadata (name/description from YAML frontmatter, ~50 tokens) is always visible; the full SKILL.md loads (~500 tokens) only once Claude decides a skill is relevant; a `references/` directory of supporting docs loads (2,000+ tokens) only on further demand. This lets an agent carry hundreds of skills without overwhelming its context window.
- **Files as the universal primitive**: skills are plain files — versionable with Git, storable in Google Drive, shareable with a team — which is why skill authorship isn't limited to engineers; product managers, analysts, and domain experts already build their own.
- **Code over traditional tools**: a real example — Claude kept writing the same script to apply Anthropic's brand styling to slides, so it was saved as a reusable script (`apply_template.py`) referenced by the skill's documentation, rather than re-derived from scratch each time.
- **Three emerging skill types**: foundational (core capabilities like document/spreadsheet/presentation handling, in Anthropic's public skills repo), partner-integration (K-Dense, Browserbase, Notion, and others building skills that make their own services agent-accessible), and organizational/proprietary (encoding a company's internal processes, compliance requirements, and institutional knowledge).
- **Skills + MCP composition**: a competitive-analysis skill might coordinate web search, an internal database via MCP, Slack history, and Notion pages in one workflow — skills increasingly orchestrate multiple MCP connections rather than standing alone.
- **Emerging agent architecture layers**: the (reasoning) loop, the runtime that executes, MCP that connects, and skills that guide — each with a clear, independently-evolvable purpose.
- Vertical expansion: skills enhanced Claude's financial-services and healthcare/life-sciences offerings just after the initial Skills launch.
- Reiterates publishing **Agent Skills** as an open standard at agentskills.io, alongside MCP's precedent, so a community-built skill can make any compatible agent more capable regardless of platform.
- Written by Barry Zhang, Mahesh Murag, Keith Lazuka, Ryan Whitehead.

## Related

- [[ClaudeCodeSkills]] — the concept this article substantially expands (progressive-disclosure token estimates, skill types, agent-architecture layering)
- [[ModelContextProtocol]] — the connectivity layer skills compose with
- [[ClaudeAgentSDK]] — the production-ready general agent runtime referenced
