---
title: "summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic announced that organizations using Claude Desktop through AWS, Google Cloud, and Microsoft Foundry now get the full Desktop experience — chat, Claude Cowork, and Claude Code — all in one app. This unified deployment lets IT teams keep inference inside their own cloud environment across all products, with enterprise-grade deployment controls including per-user SSO, MDM policy templates, an offline installer, and an M365 connector that can run entirely on-device. Each product surface (chat, Cowork, Code) has its own policy key, so administrators can phase rollout by role and control which teams get access to which capabilities.

## Key Points

- Full Claude Desktop experience (chat, Claude Cowork, Claude Code) now available through AWS, Google Cloud, and Microsoft Foundry, covering every role in an organization from a single deployment.
- Inference runs in the customer's own cloud environment in regions they configure; conversation history is stored locally, and organizations control endpoint access and telemetry sharing.
- SSO integration via IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID, or any OIDC provider like Okta — no shared keys or cloud credentials on end-user machines.
- MDM policy template export for Intune, GPO, or Jamf; offline installer available for air-gapped environments.
- Each surface (Chat, Claude Cowork, Claude Code) has its own policy key, enabling phased rollout — start with chat for non-technical teams and expand access as adoption grows.
- M365 connector gives Claude access to mail and documents through the organization's own Entra app, with tenant allowlisting and beta support for GCC High/DoD endpoints. A local connector option keeps the connection between the device and Microsoft for strictest residency requirements.
- Pre-rollout validation: test every connector, confirm model availability, and verify connections before rollout. A model guard keeps routing on Claude (including GovCloud) even if settings are misconfigured.

## Related

- [[ClaudeDesktop]] — the unified desktop application
- [[ClaudeCode]] — the coding agent surface within Claude Desktop
- [[ClaudeCowork]] — the knowledge work surface within Claude Desktop
- [[AWS]] — cloud platform for Claude Desktop inference
- [[GoogleCloud]] — cloud platform for Claude Desktop inference
- [[MicrosoftFoundry]] — cloud platform for Claude Desktop inference
- [[M365Connector]] — Microsoft 365 integration for on-device data access
- [[Anthropic]] — the company behind Claude Desktop
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud environment
