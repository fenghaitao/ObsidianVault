---
title: "EnterpriseManagedAuthorization"
type: concept
tags: [mcp, authorization, identity-provider, enterprise, security, okta, zero-touch]
sources: ["raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md"]
last_updated: 2026-07-07
---

## Definition

Enterprise-Managed Authorization (EMA) is an extension to the [[ModelContextProtocol|Model Context Protocol (MCP)]] that allows organization admins to provision [[MCPConnector|MCP connectors]] centrally through their identity provider (IdP). Users inherit connector access through IdP groups and roles, eliminating the need for individual per-user authorization.

## Key Information

### How It Works

1. Admins connect the organization's identity provider (e.g., [[Okta]]) to Claude.
2. Admins choose which MCP connectors to enable and scope access by IdP groups/roles.
3. When an employee logs in, their authorized connectors are already available across Claude chat, [[ClaudeCode|Claude Code]], and [[ClaudeCowork|Cowork]].
4. Access stays consistent across all Claude product surfaces.

### Zero-Touch Setup

Before EMA, connector setup required two steps: (1) admin enables a connector for the organization, and (2) every individual user authorizes it themselves. EMA collapses this into a single admin provisioning step, achieving zero-touch connector setup for the end user.

### Security Benefits

- **Centralized access management:** Folds MCP access into the same IdP workflow governing the rest of the enterprise stack.
- **Frictionless revocation:** Because checking access with the IdP is frictionless, admins can shorten access token lifetimes. When a user is deprovisioned, connector access expires quickly instead of lingering on an old token.
- **IdP-only enforcement:** Admins can require that a connector only ever connects through the IdP, keeping work and personal use cleanly separated and preventing accidental linking of personal accounts to work tools.
- **Unified security surface:** Access runs through the already-trusted identity provider, so connectors fall under the same security and access controls as everything else, rather than being a separate surface to monitor.

### Ecosystem Support

EMA requires coordination across three groups:

| Role | Participants at Launch |
|---|---|
| **Identity Providers** | [[Okta]] (additional providers coming soon) |
| **MCP Providers** | [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Granola]], [[Linear]], [[Supabase]] ([[Slack]] coming soon) |
| **Claude Customers** | [[Hubspot]], [[Ramp]], [[Webflow]], among others |

### Open Standard

EMA is the first implementation of the [Enterprise-Managed Authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) to the Model Context Protocol. Any identity provider or MCP provider can add support by implementing the open extension to the MCP authorization spec. This means custom connectors built by an organization's own teams can also support EMA, and they all work the same way for every Claude customer.

### Availability

Available in beta for customers on the Claude Team and Enterprise plans as of June 2026.

## Related

- [[MCPConnector]] — the connectors governed by EMA
- [[ModelContextProtocol]] — the protocol EMA extends
- [[Okta]] — first supported identity provider
- [[Anthropic]] — company launching EMA
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — source announcement
