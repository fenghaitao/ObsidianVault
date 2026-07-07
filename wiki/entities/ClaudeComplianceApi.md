---
title: "ClaudeComplianceApi"
type: entity
tags: [claude, api, security, compliance, enterprise, governance]
sources: ["raw/01-articles/claude/2026-05-21 - Claude now works with more security and compliance tools.md"]
last_updated: 2026-07-07
---

## Definition

The Claude Compliance API (also referred to as the Compliance API) is [[Anthropic]]'s programmatic interface that gives enterprise security and compliance teams access to Claude usage data. It enables organizations to integrate Claude governance into their existing security tooling stack via over 60 partner integrations spanning DLP, SIEM, SASE, eDiscovery, AI-SPM, and AI observability categories.

## Key Information

### Data Streams

The API exposes two types of data:

- **Conversation content from Claude Enterprise** — including chats, uploaded files, and projects — so admin teams can apply the same security, monitoring, and DLP policies to Claude that they already use for other workplace applications.
- **Activity events across Claude Enterprise and the Claude Platform** — user logins, admin actions, and configuration changes — so security teams get a unified view of how Claude is used across the organization.

### Platform Availability

- First launched for [[ClaudeEnterprise|Claude Enterprise]] in August 2025.
- Expanded to the full Claude Platform in March 2026 (see [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]]).
- Organizations using it for Claude Enterprise can merge their Claude API organization under the same parent org for one combined activity feed.

### Partner Integrations (May 2026)

Over 60 security and compliance providers offer integrations across categories including:

- **DLP & Data Security**: Cyera, Forcepoint, Mimecast, Netskope, Nightfall AI, Proofpoint, Sentra, Varonis, Zscaler
- **SIEM & Security Operations**: Cribl, CrowdStrike, Datadog, Elastic, ReliaQuest, SentinelOne, Sumo Logic, Trellix
- **Identity**: Island, Linx Security, Okta, SailPoint, Saviynt
- **eDiscovery**: Relativity, Smarsh
- **AI Security Posture Management (AI-SPM)**: Air, Akto, Bay, Beacon Security, Bloom Security, Brava Security, Dash Security, Daylight, Exaforce, ForceAI Security, Geordie AI, Grip Security, Harmonic Security, Mint Security, Opsin, Pluto Security, Reco, Safeguard, Tenable, Token Security, Torch Security, TrendAI, Zenity
- **AI Observability & Telemetry**: C1.ai, Sysdig
- **Multi-category**: Check Point, Cloudflare, Fortinet, IBM Guardium, Microsoft Purview, Palo Alto Networks, Rubrik, Snyk, Wiz

### Getting Started

For Claude customers: connect and configure the Claude instance to a supported partner platform via the Help Center and Compliance API documentation. Data then flows into existing dashboards and alerting workflows.

For security partners: Anthropic accepts applications to join the integration partner network.

## Related

- [[summary-2026-05-21 - Claude now works with more security and compliance tools]] — source announcement
- [[ClaudeEnterprise]] — the primary plan served by the Compliance API
- [[AISecurityGovernance]] — the broader concept of governing AI usage in organizations
- [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]] — earlier Compliance API platform expansion announcement
- [[ClaudeSecurity]] — related enterprise security product
