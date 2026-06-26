---
title: "Agent Skills"
type: concept
tags: [agents, prompt-engineering, context-management, progressive-disclosure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Agent Skills are compact, concise instructions that tell an agent about capabilities and workflows. They use progressive disclosure: only the name and description (front matter) load initially, the full body loads when a matching query is executed, and then the body is wiped from context after execution. This makes skills more context-efficient and maintainable than inline prompts.

## Key Information
- **Progressive disclosure**: Front matter (name + description) is always loaded. Full body loads only when the skill is activated by a matching query. Body is wiped from context after execution
- **Context efficiency**: Unlike inline prompts that permanently occupy context, skills only consume context when actively used
- **Structure**: YAML front matter with name and description, followed by the skill body (instructions/workflow)
- **Description importance**: The description is what the agent uses to match queries to skills, so it must be well-written
- **Shareability**: Skills can be checked into GitHub and shared across teams, unlike personal prompt configurations
- **Maintainability**: Centralized, version-controlled skill definitions are easier to maintain than scattered inline prompts
- **Replaces MCP prompts**: In the workshop, the research workflow prompt was converted into a skill, keeping the MCP server for tool logic only
- **Agent harness detection**: The agent harness (e.g., Claude Code) automatically detects relevant skills based on the user's query and loads them
- **Trade-off with MCP**: Skills are great for local/personal setups; MCP servers are better for distributing business logic at scale (credentials, dependencies, CLI tools)

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Skills]] — broader concept of agent playbooks
- [[ProgressiveDisclosure]] — the design pattern enabling context efficiency
- [[MCP]] — alternative approach for distributing agent capabilities
- [[ClaudeCode]] — agent harness with native skill support
- [[Context Budget]] — the constraint that skills help manage
- [[Deep Research Agent]] — system using skills for workflow instructions
