---
title: "Jeremy Fronae"
type: entity
tags: [person, ai-engineer, mcp, oauth, lenses]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses.md"]
last_updated: 2026-06-30
---

## Definition
Jeremy Fronae is an AI Engineer at Lenses specializing in MCP authorization flows and enterprise-grade security for agentic AI systems.

## Key Information
- Works on AI engineering at Lenses
- Presented the OAuth flows section of "Your Insecure MCP Server Won't Survive Production"
- Detailed the progression from local API key MCP → remote API key MCP → OAuth 2.1 with DCR → CIMD
- Explained how traditional OAuth pre-registration breaks with MCP's architecture of unbounded clients connecting to unbounded servers
- Highlighted DCR's problems: non-portable registrations, phishing vulnerability (anyone can POST to /register), no client identity verification
- Advocated for CIMD (Client ID Metadata Document) as the preferred approach since November 2025: proving URL control is meaningful, redirect URIs are explicitly bound, authorization server can selectively allow/deny
- Outlined enterprise-grade requirements beyond OAuth: RBAC at tool/resource level, data masking for PII, audit logging (EU AI Act compliance), end-to-end observability

## Related
- [[summary-20260408 - Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses]] — source
- [[Lenses]] — company
- [[TunShwe]] — co-presenter
- [[CIMD]] — Client ID Metadata, preferred over DCR
- [[DynamicClientRegistration]] — DCR, with its limitations
- [[ConfusedDeputyVulnerability]] — vulnerability in API key pass-through MCP
- [[MCPRBAC]] — tool/resource-level permissions
- [[DataMaskingForAgents]] — PII masking for agents
- [[MCPAuditLogging]] — compliance logging
- [[MCPObservability]] — end-to-end tracing
- [[OAuth]] — authorization framework for MCP
- [[TokenExchange]] — RFC 8693 for delegation tokens
- [[PKCE]] — proof key for code exchange
