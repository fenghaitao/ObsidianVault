---
title: "CloudInference"
type: concept
tags: [cloud, inference, enterprise, deployment, ai-infrastructure]
sources: ["raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

Cloud inference is the pattern of running AI model inference within an organization's own cloud environment rather than on the AI provider's infrastructure. In the context of [[ClaudeDesktop]], it means Claude's reasoning and generation run on the customer's AWS, Google Cloud, or Microsoft Foundry instances, with conversation history stored locally on end-user devices.

## Key Information

- **Data control:** Organizations control which regions inference runs in, what endpoints data connectors can reach, and what aggregated telemetry the AI provider receives.
- **No cloud credentials on end-user machines:** Users authenticate via the organization's existing SSO (IAM Identity Center, Entra ID, Okta, etc.) rather than API keys or shared credentials.
- **Local conversation history:** Chat history is stored on the user's device rather than in the AI provider's cloud, addressing data residency and compliance requirements.
- **Model guard:** A routing safeguard keeps inference on the correct Claude models (including GovCloud) even if deployment settings are misconfigured.
- **Air-gapped support:** Offline installer and local-only connectors (e.g., M365 local connector mode) support environments with strict network isolation requirements.

## Related

- [[ClaudeDesktop]] — the desktop application using cloud inference
- [[AWS]] — cloud platform for Claude inference
- [[GoogleCloud]] — cloud platform for Claude inference
- [[MicrosoftFoundry]] — cloud platform for Claude inference
- [[M365Connector]] — local connector mode for strict residency requirements
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
