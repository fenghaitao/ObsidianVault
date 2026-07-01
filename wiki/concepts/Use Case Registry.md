---
title: "Use Case Registry"
type: concept
tags: [registry, enterprise, governance, lineage, traceability, use-case]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
A Use Case Registry is a centralized catalog that maps business use cases to the AI assets they employ -- agents, tools (MCP servers), and models. It provides the connective tissue between technical registries (MCP and A2A) and business context, enabling governance, lineage tracking, and impact analysis.

## Key Information
- **Connective function**: Links MCP Registry and A2A Registry together from a business perspective, mapping agents and tools to specific use cases adopted across the organization
- **Asset mapping**: For each use case, tracks which agents, MCP servers, and AI models are being used, providing a complete inventory of AI asset usage
- **Lineage view**: Provides an object lineage visualization showing all connections -- use cases connected to agents, agents connected to other agents, all connected to AI models -- enabling full traceability
- **Impact analysis**: When a component in the lineage has an outage or problem, operators can immediately identify all affected use cases and make modifications
- **Governance function**: Serves as the catalog that makes governance happen -- knowing where AI is used, what the main use cases are, for both regulatory compliance and organizational awareness
- **Use case metadata**: Each use case entry includes status, version, description, assets used, and lifecycle history
- **Create workflow**: Platform provides form-based use case creation with name, description, status, ownership, and asset linkage
- **Maintenance support**: By knowing which use cases use which models, the organization can address LLM model disruptions promptly -- knowing exactly which use cases are affected when a model changes

## Related
- [[MCP Registry]] — tool registry connected through use cases
- [[A2A Registry]] — agent registry connected through use cases
- [[Lineage View]] — the visualization of use case-to-asset connections
- [[Enterprise Registry Metadata]] — metadata dimensions enriching registry entries
- [[AI Gateway]] — unified LLM access layer
- [[Amplify Program]] — Amplifon's program that includes the use case registry
- [[Enterprise Agent Governance]] — governance patterns enabled by use case registries
- [[Amplifon]] — organization that built this use case registry
- [[Mauro Luchetti]] — presenter who described the use case registry design
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
