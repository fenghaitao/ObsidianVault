---
title: "One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS"
type: source-summary
source: raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS.md
author: Garrett Galow
company: WorkOS
date: 2026-04-28
---

# One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS

## Core Thesis

MCP's OAuth-based authentication creates a fragmented experience of repeated consent screens that breaks the single sign-on model. Cross-App Access (XAA), built on the ID JAG (Identity JWT Authorization Grant) spec, enables identity providers like Okta to act as trust brokers between MCP clients and servers, eliminating consent screen fatigue while improving IT visibility, security posture, and onboarding efficiency.

## Key Points

1. **The Consent Screen Problem**: MCP servers using OAuth require users to click through consent screens for every tool, repeatedly, with no clear reason why re-authentication is needed. This is an annoyance for individual developers and a scaling nightmare for teams.

2. **IT Blind Spots**: IT teams cannot see which MCP servers developers are connecting to, cannot control which AI agents access sensitive systems (Figma, Notion), and cannot revoke MCP access tokens when an employee leaves or a machine is compromised — access tokens and refresh tokens persist independently of SSO session revocation.

3. **XAA Solution**: Cross-App Access lets the identity provider (Okta) act as a trust broker. Since both the MCP client (Cursor, Claude Code) and MCP server (Figma) already trust Okta for SSO, Okta can issue ID JAG tokens that bridge the gap without manual consent.

4. **ID JAG Flow**: (1) User logs into IDP via SSO → gets ID token + refresh token. (2) Client requests ID JAG token from IDP for a specific audience (e.g., Figma MCP server). (3) Client exchanges ID JAG with the resource authorization server → gets short-lived OAuth access token. (4) Standard MCP communication proceeds. Steps 2-3 are invisible to the user.

5. **Security Improvement**: Access tokens are short-lived (~5 minutes). When an SSO session is revoked, the user cannot get new access tokens once the current one expires — unlike today's long-lived refresh tokens that grant standing access for days or weeks.

6. **IT Setup**: IT admins configure a managed connections policy in Okta specifying which MCP clients can request access to which MCP servers (e.g., "Cursor can request access to Figma").

7. **MCP Client Requirements**: SSO connection with XAA support, ability to request ID JAG tokens, and ability to exchange them with MCP servers.

8. **MCP Server Requirements**: Support for JWT bearer grant type, token validation against the IDP, and standard access token issuance.

9. **Current Limitations**: Only Okta supports XAA (OIDC-based connections). Microsoft Entra does not yet support it. Authorization scoping (e.g., limiting what an agent can do within Figma) is not part of the spec today.

10. **DCR and CIMD**: Dynamic Client Registration is widely supported but not universal. Client ID Metadata (CIMD) is a newer spec (~3 months old) that pre-defines clients upfront, avoiding per-session registration, but has limited ecosystem support.

## Entities

- [[GarrettGalow]] — runs product at WorkOS, previously at Microsoft Azure and Cloudflare
- [[WorkOS]] — makes apps and agents enterprise-ready, powers auth for Anthropic, Cursor, OpenAI
- [[Okta]] — identity provider supporting XAA/ID JAG
- [[MicrosoftEntra]] — Microsoft's identity platform, does not yet support XAA
- [[MicrosoftAzure]] — Garrett's previous employer
- [[DeepSeek]] — mentioned as an MCP client IT might not want employees using
- [[SCIM]] — system for cross-domain identity management, used for access revocation
- [[Cursor]] — MCP client using WorkOS for SSO
- [[Anthropic]] — WorkOS customer, uses WorkOS for Claude Code SSO
- [[ClaudeCode]] — MCP client demonstrated with XAA
- [[Figma]] — example MCP server in the XAA demo
- [[Notion]] — example MCP server with sensitive data
- [[OpenAI]] — WorkOS customer
- [[Cloudflare]] — Garrett's previous employer

## Concepts

- [[CrossAppAccess]] — XAA: identity provider as trust broker between MCP client and server
- [[IDJAG]] — Identity JWT Authorization Grant spec for cross-service token issuance
- [[SingleSignOn]] — SSO: one login for all applications, broken by MCP's OAuth model
- [[OAuth]] — underlying authentication layer used by MCP, source of consent screen friction
- [[SAML]] — SAML-based SSO connections, ID JAG spec supports SAML assertions
- [[JWT]] — JSON Web Token format used for ID JAG tokens
- [[ConsentScreens]] — the UX friction problem that XAA solves
- [[ClientIDMetadata]] — CIMD: newer spec superseding DCR for client registration
- [[DynamicClientRegistration]] — DCR: runtime client registration mechanism

## Related

- [[MCP]] — the protocol whose authentication model creates the problem
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]] — related talk on agent identity
