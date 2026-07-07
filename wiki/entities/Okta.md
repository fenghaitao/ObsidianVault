---
title: "Okta"
type: entity
tags: [identity-provider, enterprise, authentication, authorization, security, mcp]
sources: ["raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md"]
last_updated: 2026-07-07
---

## Definition

Okta is an enterprise identity and access management platform. It is the first identity provider supported by [[Anthropic]]'s [[EnterpriseManagedAuthorization|Enterprise-Managed Authorization (EMA)]] for [[MCPConnector|MCP connectors]].

## Key Information

- **First IdP for EMA:** Okta is the launch partner for Enterprise-Managed Authorization, enabling admins to provision MCP connectors through Okta groups and roles.
- **Centralized provisioning:** Admins connect Okta to Claude, choose which MCP connectors to enable, and scope access by Okta groups/roles. Users inherit connector access automatically on first login.
- **Unified access control:** MCP connector access runs through the same Okta-based identity and access controls as the rest of the enterprise stack, rather than being a separate surface to monitor.

## Related

- [[EnterpriseManagedAuthorization]] — the authorization mechanism Okta supports
- [[MCPConnector]] — the connectors provisioned through Okta
- [[Anthropic]] — the company integrating Okta for EMA
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — source announcement
