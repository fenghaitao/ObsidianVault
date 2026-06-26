---
title: "ToolComposition"
type: concept
tags: [agentic-tools, composition, mcp, advanced]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
Tool composition is the practice of creating new specialized agentic tools by building on top of existing third-party tools, giving them distinct descriptions and behaviors so the agent can choose the right tool for different contexts within the same workflow.

## Key Information
- Composed tools have the same or similar underlying functionality as existing tools but different descriptions, allowing the agent to differentiate when to use each.
- New tools can include additional deterministic actions or guardrails specific to their purpose.
- In Baz's spec reviewer example, an "evidence tool" was composed from the screenshot tool, with instructions to only use it for capturing evidence, include ticket numbers in filenames, and apply evidence-specific naming conventions.
- The agent's prompt describes the flow ending with evidence capture, so the agent naturally chooses the evidence tool over the generic screenshot tool at that stage.
- Composition is considered more advanced/niche than curation, wrapping, and guardrails, but is a powerful tool in the arsenal.
- A composed tool should only be created if its underlying base tool has not been filtered out by curation.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[ThirdPartyToolOptimization]] — parent framework
- [[ToolWrapping]] — simpler alternative (rewrapping vs. composing new)
- [[DeterministicGuardrails]] — can be embedded in composed tools
- [[ToolCuration]] — composed tools depend on base tools not being filtered
