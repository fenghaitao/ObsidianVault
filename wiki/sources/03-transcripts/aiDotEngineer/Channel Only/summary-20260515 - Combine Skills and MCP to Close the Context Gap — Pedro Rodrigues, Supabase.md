---
title: "summary-20260515 - Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase"
type: source
tags: [source, transcript, skills, mcp, supabase]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase.md"]
last_updated: 2026-06-29
---

## Core Summary

Pedro Rodrigues presents lessons from building Supabase's agent skill, combining skills and MCP to close the context gap. Key principles: don't duplicate information (point agents to live docs), critical info must go in skill.md not reference files (agents skip references), and be opinionated about workflows. He announces the Supabase Agent Skill and a novel SSH-based documentation interface for agents.

## Key Points

- Skills + MCP together: MCP provides actions/integration, skills provide context/guidance. Not a debate anymore.
- Three principles for product skills: (1) Don't duplicate information — point agents to live docs and be stubborn about fetching. (2) If something can be skipped it will be — critical security info must go in skill.md, not reference files. (3) Be opinionated — guide agents to optimal workflows for your product.
- Supabase Agent Skill announced at the talk; addresses RLS security pitfalls, stale training data, and workflow optimization.
- Experimental SSH-based documentation: exposing docs as a filesystem for agent navigation using Linux tools.
- Demo: Claude Sonnet 4.6 with skill + MCP correctly handled RLS security on SQL views, while MCP-only agent missed the security flag.

## Related

- [[PedroRodrigues]] — speaker, AI tooling engineer at Supabase
- [[Supabase]] — company
- [[Skills]] — agent skills concept
- [[MCP]] — Model Context Protocol
- [[ProgressiveDisclosure]] — skill design pattern
- [[ContextGap]] — the gap skills and MCP address
