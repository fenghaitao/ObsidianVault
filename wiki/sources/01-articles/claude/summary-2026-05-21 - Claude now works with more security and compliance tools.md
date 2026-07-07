---
title: "summary-2026-05-21 - Claude now works with more security and compliance tools"
type: source
tags: [source, claude-blog, security, compliance, enterprise]
sources: ["raw/01-articles/claude/2026-05-21 - Claude now works with more security and compliance tools.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic announced 28 integrations (later expanded to over 60) with security and compliance tools, all powered by the Claude Compliance API. This API gives enterprise security teams programmatic access to Claude Enterprise conversation content and Claude Platform activity events, enabling organizations to apply existing DLP, SIEM, SASE, eDiscovery, and AI security posture management tools to govern Claude usage the same way they govern other workplace applications. Integrations span major providers including CrowdStrike, Datadog, Microsoft Purview, Okta, Palo Alto Networks, Snyk, Wiz, and Zscaler.

## Key Points

- The Claude Compliance API exposes two data streams: conversation content from Claude Enterprise (chats, files, projects) and activity events across both Claude Enterprise and the Claude Platform (logins, admin actions, config changes).
- Over 60 security and compliance partners now offer integrations across categories: DLP, SASE, data security, SIEM, security operations, identity, eDiscovery, AI security posture management (AI-SPM), and AI observability/telemetry infrastructure.
- Connecting a Claude instance to a supported partner platform is straightforward — configure the connection and data flows into the same dashboards and alerting workflows already in use.
- This launch represents a significant step in making Claude enterprise-governable, addressing a key blocker for large-organization adoption.

## Related

- [[ClaudeComplianceApi]] — the API powering all integrations
- [[ClaudeEnterprise]] — the plan these integrations primarily serve
- [[AISecurityGovernance]] — the broader concept of governing AI usage in organizations
