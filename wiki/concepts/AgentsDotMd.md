---
title: "AgentsDotMd"
type: concept
tags: [ai, agents, configuration, standards, project-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-26
---

## Definition
agents.md is a de facto standard file for AI coding agent project configuration. It contains always-on rules and details about the project that agents load into context automatically — conventions, build/test commands, testing requirements, and other project-specific information the agent needs to work effectively.

## Key Information
- Quickly becoming the de facto standard across AI coding agents for project-level configuration
- Contains minimal but critical information: coding conventions, build and test commands, testing requirements, pre-commit checklists
- Loaded into context automatically (always-on), unlike skills which are loaded on demand
- Part of a three-bucket agent configuration system: modes (role-based behavior), agents.md (always-on project rules), and skills (on-demand reusable playbooks)
- Should be kept minimal to avoid unnecessary context consumption
- For internal platform APIs without OpenAPI specs: convert API documentation to markdown and include in agents.md or elsewhere in the repository
- Contrasts with skills.md: agents.md is always loaded; skills are invoked on demand for specific workflows

## Related
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source transcript
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source transcript
- [[AgentModes]] — complementary mode-based configuration
- [[Skills]] — complementary on-demand configuration
- [[ContextEngineering]] — the practice of managing what goes into context
- [[AgenticEngineering]] — the parent paradigm
- [[Clone the Repo Pattern]] — references agents.md for repo configuration
- [[Pattern Files (AI)]] — referenced from agents.md
- [[Model Prompting Styles]] — affects how agents.md is written
