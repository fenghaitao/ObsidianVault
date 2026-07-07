---
title: "MicrosoftFoundry"
type: entity
tags: [microsoft, cloud, ai-platform, enterprise]
sources: ["raw/01-articles/claude/2026-05-28 - Introducing dynamic workflows in Claude Code.md", "raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

Microsoft Foundry is a cloud platform that hosts Claude models for enterprise customers. It supports Claude Code dynamic workflows via the Claude API, and as of June 2026, the full Claude Desktop experience (chat, Claude Cowork, and Claude Code) with inference running on the customer's own Microsoft Foundry environment.

## Key Information

- Listed alongside [[AmazonBedrock]] and [[VertexAI]] as a cloud platform where [[ClaudeCode]] dynamic workflows are available via the Claude API.
- Part of [[Microsoft]]'s broader AI platform ecosystem, complementing [[Microsoft365Copilot]] where Claude models are also available.
- **Claude Desktop on Microsoft Foundry (June 2026):** Organizations can deploy the full Claude Desktop experience with inference on Microsoft Foundry, including enterprise SSO via Microsoft Entra ID or OIDC providers, MDM policy deployment through Intune, and an [[M365Connector|M365 connector]] for on-device access to mail and documents through the organization's own Entra app.
- The M365 connector supports tenant allowlisting and beta support for GCC High/DoD endpoints, with a local connector mode for strictest data residency requirements.

## Related

- [[ClaudeDesktop]] — the unified desktop application deployable on Microsoft Foundry
- [[ClaudeCode]] — the coding tool available on Microsoft Foundry
- [[DynamicWorkflows]] — the Claude Code feature supported on the platform
- [[Microsoft]] — parent company
- [[Microsoft365Copilot]] — related Microsoft AI offering also hosting Claude models
- [[M365Connector]] — Microsoft 365 integration for Claude Desktop on Microsoft Foundry
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-05-28 - Introducing dynamic workflows in Claude Code]] — source article
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
- [[summary-20 - Build AI agents using Claude in Microsoft Foundry]] — source summary
