---
title: "High-Bandwidth Artifacts"
type: concept
tags: [agents, ui, ux, collaboration, interface-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
High-bandwidth artifacts are persistent, domain-specific interfaces for agent-human collaboration that replace one-dimensional chat. They allow humans to quickly review agent work, inject judgment at precise points, and maintain context across interactions — unlike chat which collapses a tree of work into a linear conversation.

## Key Information
- Chat is one-dimensional and low-bandwidth: it tries to collapse a work tree/DAG into a single linear thread, making it impossible to effectively review complex agent work
- High-bandwidth artifacts are typically persistent and look different across industries and verticals depending on the task
- Examples from Legora (legal AI):
  - **Document collaboration**: highlight clause three and only clause three changes; add comments; tag agents and collaborators; hand off parts of the document to specialized agents
  - **Tabular review**: a known primitive where the agent spins up a review table, flags items needing human input, the human reviews quickly, then kicks off the rest of the agent
- Key properties: persistent (survives sessions), domain-specific (matches the artifact type of the industry), high control (precise injection of human judgment), reviewable (quick assessment of what the agent did)
- Chat boxes remain useful as input (language is the universal interface), but should not be the main mode of collaboration for complex agents
- Agents are not humans and should not be constrained to human language interfaces — they can interact through richer artifacts that humans cannot

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[Agent-Human Collaboration]] — the broader framework
- [[JacobLauritzen]] — presented this concept
- [[Legora]] — company implementing these artifacts
- [[Vertical AI]] — domain where artifacts vary by industry
- [[Decision Log]] — a specific artifact type for non-blocking elicitation
