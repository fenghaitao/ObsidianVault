---
title: "Enterprise Registry Metadata"
type: concept
tags: [registry, enterprise, metadata, governance, mcp, a2a]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
Enterprise Registry Metadata refers to the additional dimensions of information that enrich registry entries (MCP servers, A2A agents, use cases) beyond their technical descriptions, enabling governance, impact analysis, cost tracking, and auditability in enterprise AI deployments.

## Key Information
- **Five metadata dimensions** (as defined by Amplifon/Quantyca):
  1. **Ownership**: Which team, use case, or project is responsible for the registered asset
  2. **Environment**: Which environment the asset runs in (dev, test, prod)
  3. **Authentication Model**: What mechanisms developers need to use to access the asset
  4. **Cost Attribution**: Linked to AI Gateway budgeting, tracking which asset is spending what
  5. **Use Case Linkage**: Which business use cases are actually using the asset
- **Purpose**: These metadata fields are not "nice to have" -- they enable impact analysis (what breaks if a server changes), complete audit trails (what AI tooling exists and how it's being used), and governance (knowing the full scope of AI adoption)
- **Application**: Applied to MCP Registry entries (custom internal servers and curated approved public servers) and to use case entries in the Use Case Registry
- **Gateway integration**: Cost attribution links directly to the AI Gateway's budgeting functionality, enabling per-asset cost tracking
- **Lineage foundation**: The use case linkage field is the key connector that enables the object lineage view across use cases, agents, tools, and models

## Related
- [[MCP Registry]] — registry where this metadata is applied to MCP servers
- [[A2A Registry]] — companion registry with similar metadata needs
- [[Use Case Registry]] — registry that connects metadata across all assets
- [[AI Gateway]] — provides the cost tracking that feeds cost attribution metadata
- [[Lineage View]] — visualization enabled by use case linkage metadata
- [[Enterprise Agent Governance]] — governance patterns enabled by metadata
- [[Amplifon]] — organization that defined these metadata dimensions
- [[Mauro Luchetti]] — presenter who defined the enterprise metadata framework
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
