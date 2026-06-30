---
title: "ContextGap"
type: concept
tags: [context-engineering, skills, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase.md"]
last_updated: 2026-06-29
---

## Definition

The context gap is the delta between what an AI agent knows from its training data and what it needs to know to work correctly with a specific product, API, or codebase. Skills and MCP together close this gap: MCP provides actions/integrations, skills provide context/guidance and workflows.

## Key Information

- Agents default to stale training data and are stubborn about admitting ignorance
- Skills provide progressive disclosure: name/description envelope loaded first, full instructions only when needed
- Critical information must be in skill.md (not reference files) because agents skip loading references
- MCP + skills is complementary, not competitive: MCP for actions, skills for context
- Novel approach: SSH-based documentation for agent filesystem navigation

## Related

- [[summary-20260515 - Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase]] — source
- [[Skills]] — agent skills
- [[MCP]] — Model Context Protocol
- [[ProgressiveDisclosure]] — skill design pattern
- [[Supabase]] — case study
