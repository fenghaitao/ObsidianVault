---
title: "Consent Screens"
type: concept
tags: [ux, authentication, oauth, mcp]
---

# Consent Screens

## Definition

Consent screens are OAuth authorization prompts that ask users to approve an application's access to their data. In the MCP context, they create significant UX friction by requiring users to click through them for every MCP server, repeatedly.

## Key Information

- **MCP Friction**: Each MCP server requires its own consent screen. Users must click through for every tool, and sometimes must re-authenticate without understanding why
- **Scale Problem**: An individual developer might connect to a half-dozen MCP servers. Across a team of dozens, the cumulative time spent on consent screens is substantial
- **User Behavior**: Users typically don't read consent screens — they just click "OK" — undermining the security purpose of explicit consent
- **XAA Solution**: Cross-App Access eliminates consent screens entirely by having the identity provider broker trust automatically, using the existing SSO relationship

## Related

- [[CrossAppAccess]]
- [[OAuth]]
- [[MCP]]
- [[SingleSignOn]]
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]]
