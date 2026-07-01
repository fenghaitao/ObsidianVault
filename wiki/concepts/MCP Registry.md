---
title: "MCP Registry"
type: concept
tags: [mcp, registry, enterprise, governance, catalog]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
An MCP Registry is a centralized catalog of all available MCP servers within an organization. In an enterprise context, it extends the public community MCP registry with private internal servers, curated approved public servers, and enterprise metadata that enables governance, impact analysis, and auditability.

## Key Information
- **Enterprise extension**: Built on top of the community MCP registry as an extension in functionality and enterprise context
- **Two categories of servers**: Custom internal servers built by teams for specific systems and integrations, plus a curated set of approved public servers certified for organizational use
- **Enterprise metadata enrichment**: Each registered server is enriched with ownership (which team/use case/project is responsible), environment (dev/test/prod), authentication model (how developers access the server), cost attribution (linked to AI Gateway budgeting), and use case linkage (which use cases are using the server)
- **Impact analysis**: Enterprise metadata enables understanding what would break if a server changes or goes down -- which use cases depend on it
- **Governance and auditability**: Provides a complete trail of what AI tooling exists and how it's being used by developers across the organization
- **Inspector integration**: Platform includes inspector pages that can launch MCP inspector in another tab to check what an MCP server provides
- **Widget forms**: Platform provides form-based creation of server.json to simplify MCP server registration without hand-writing JSON
- **CICD publishing**: MCP servers auto-publish their server.json metadata to the registry via GitHub Actions when a branch is tagged
- **Runtime lookup**: MCP proxy looks up actual backend URLs from the registry catalog when agents route calls through the AI Gateway

## Related
- [[MCP]] — the Model Context Protocol that MCP servers implement
- [[A2A Registry]] — companion registry for agent-to-agent protocol
- [[Use Case Registry]] — connects MCP servers to business use cases
- [[AI Gateway]] — unified LLM access layer that routes to MCP proxies
- [[Enterprise Registry Metadata]] — the metadata dimensions enriching MCP servers
- [[Amplifon]] — organization that built this enterprise MCP registry
- [[Quantyca]] — consultancy that designed the registry
- [[Mauro Luchetti]] — presenter who described the MCP registry design
- [[MCPEnterpriseChallenges]] — related concept on enterprise MCP adoption challenges
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
