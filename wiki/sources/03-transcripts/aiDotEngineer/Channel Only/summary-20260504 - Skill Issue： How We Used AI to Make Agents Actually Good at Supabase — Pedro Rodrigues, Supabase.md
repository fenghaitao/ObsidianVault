---
title: "summary-20260504 - Skill Issue： How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase"
type: source
tags: [source, transcript, skills, agents, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Skill Issue： How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase.md"]
last_updated: 2026-06-29
---

## Core Summary

Pedro Rodrigues, AI tooling engineer at Supabase, presents a workshop on writing, testing, and evaluating agent skills. He explains the skill structure (skill.md frontmatter with progressive disclosure, reference files, scripts), contrasts skills vs MCP tools (skills provide context, MCP provides actions — use both), and demonstrates how to test skills with evaluations. The talk covers Supabase's "agent experience" (AX) focus and their approach to making agents effective through well-crafted skills.

## Key Points

- Skills are folders with instructions and files: skill.md (main), reference files, and scripts.
- Progressive disclosure: frontmatter description loads first; full content loads only when the agent decides it needs it.
- Skills vs MCP: skills provide context/instructions; MCP tools provide actions/integrations. Use both.
- Scripts in skills run locally (environment-dependent); MCP tools run server-side.
- Testing skills involves the same patterns as testing code: unit, integration, and end-to-end (via evaluations).
- Supabase focuses on AX (agent experience) alongside DX (developer experience).

## Related

- [[PedroRodrigues]] — speaker, AI tooling engineer at Supabase
- [[Supabase]] — company, open-source Firebase alternative
- [[Skills]] — agent skills concept
- [[ProgressiveDisclosure]] — key pattern in skill design
- [[MCP]] — Model Context Protocol, complementary to skills
- [[EvalEngineering]] — evaluation approach for testing skills
