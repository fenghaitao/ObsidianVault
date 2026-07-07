---
title: "ClaudeDesktop"
type: entity
tags: [product, claude, anthropic, desktop, enterprise]
sources: ["raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-07-07
---

## Definition

Claude Desktop is Anthropic's unified desktop application that brings chat, Claude Cowork, and Claude Code together in a single app. It can be deployed organization-wide with enterprise-grade controls, running inference within the customer's own cloud environment (AWS, Google Cloud, or Microsoft Foundry).

## Key Information

- **Three surfaces in one app:** Chat for quick answers and problem-solving, Claude Cowork for research and deliverable creation, and Claude Code for agentic software development.
- **Cloud inference:** Inference runs on the customer's own cloud (AWS, Google Cloud, or Microsoft Foundry) in regions they configure. Conversation history is stored locally.
- **Each surface has its own policy key**, allowing administrators to phase rollout by role — e.g., give non-technical teams chat and Cowork first, then engineering Claude Code, broadening access as adoption grows. Hard-deny rules apply across every tab.
- **Enterprise SSO:** Sign-in via IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID, or any OIDC provider like Okta. No shared keys to rotate, no cloud credentials on end-user machines.
- **MDM deployment:** Export policy templates from the setup UI and push through Intune, GPO, or Jamf. An offline installer supports air-gapped environments.
- **M365 connector:** Gives Claude access to mail and documents through the organization's own Entra app, with tenant allowlisting and beta support for GCC High/DoD endpoints. A local connector option keeps the connection between the device and Microsoft for strictest residency requirements.
- **Pre-rollout validation:** Test every connector, confirm which Claude models the provider serves, and verify connections before rollout. A model guard keeps routing on Claude (including GovCloud) even if settings are misconfigured.
- **Customer adoption:** [[HanwhaSolutions|Hanwha Solutions]] deployed Claude Desktop to hundreds of users worldwide through their existing cloud environment and LLM Gateway, with no separate vendor contract or heavy infrastructure build-out.

## Related

- [[ClaudeCode]] — the coding agent surface within Claude Desktop
- [[ClaudeCowork]] — the knowledge work surface within Claude Desktop
- [[AWS]] — cloud platform for Claude Desktop inference
- [[GoogleCloud]] — cloud platform for Claude Desktop inference
- [[MicrosoftFoundry]] — cloud platform for Claude Desktop inference
- [[M365Connector]] — Microsoft 365 integration for on-device data access
- [[Anthropic]] — the company behind Claude Desktop
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
