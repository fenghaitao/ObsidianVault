---
title: "summary-2026-06-18 - Centrally manage authorization for MCP connectors"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic launched Enterprise-Managed Authorization (EMA) for MCP connectors, allowing admins to provision connectors for their entire organization through their identity provider, starting with Okta. Instead of requiring every user to individually authorize each connector, admins configure access once via IdP groups and roles, and users inherit connector access automatically on first login across Claude chat, Claude Code, and Cowork. EMA is built on an open MCP authorization extension standard, with Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase supporting it at launch.

## Key Points

- EMA eliminates the two-step connector setup (admin enable + user authorize), collapsing it into a single admin provisioning step.
- Access is scoped by IdP groups and roles, making revocation immediate when a user is deprovisioned.
- Admins can require connectors to only connect through the IdP, preventing personal account linking to work tools.
- Okta is the first supported identity provider, with additional providers coming soon.
- Hubspot, Ramp, and Webflow are among the organizations rolling out EMA across their teams.
- Available in beta for Claude Team and Enterprise plan customers.
- Any identity or MCP provider can implement EMA via the open Enterprise-Managed Authorization extension to the MCP authorization spec.

## Related

- [[EnterpriseManagedAuthorization]] — the concept
- [[MCPConnector]] — MCP connectors this auth mechanism governs
- [[Okta]] — first supported identity provider
- [[Anthropic]] — the company launching EMA
- [[Asana]] — MCP provider supporting EMA at launch
- [[Atlassian]] — MCP provider supporting EMA at launch
- [[Canva]] — MCP provider supporting EMA at launch
- [[Figma]] — MCP provider supporting EMA at launch
- [[Granola]] — MCP provider supporting EMA at launch
- [[Linear]] — MCP provider supporting EMA at launch
- [[Supabase]] — MCP provider supporting EMA at launch
- [[Slack]] — MCP provider with EMA support coming soon
- [[Hubspot]] — Claude customer rolling out EMA
- [[Ramp]] — Claude customer rolling out EMA
- [[Webflow]] — Claude customer rolling out EMA
