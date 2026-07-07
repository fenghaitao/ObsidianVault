---
title: "Google Cloud"
type: entity
tags: [cloud-platform, infrastructure, google]
sources: ["raw/01-articles/claude/2025-04-02 - Claude on Google Cloud's Vertex AI FedRAMP High and IL2 Authorized.md", "raw/01-articles/claude/2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry.md"]
last_updated: 2026-06-28
---

## Definition

Google Cloud is Google's suite of cloud computing services providing infrastructure, platform, and software-as-a-service offerings for enterprises and developers.

## Key Information

- Provides [[VertexAI]], a managed AI/ML platform for building, deploying, and managing machine learning models.
- Offers [[VertexAI#Assured Workloads|Assured Workloads]] with enhanced security and compliance controls designed for government workloads.
- Partner with [[Anthropic]] for distributing [[Claude]] models through Vertex AI.
- Supports [[FedRAMP]] High authorization for [[Claude]] models, enabling federal agency adoption.
- Supports [[DoD-IL2|DoD Impact Level 2]] compliance for defense contractors and agencies.

## Claude on Google Cloud

Google Cloud Vertex AI provides Claude models as fully managed and serverless APIs, enabling:
- Federal agencies to build AI applications while maintaining FedRAMP High compliance
- Defense organizations to use Claude with DoD IL2 compliance for non-controlled unclassified information
- Access to the complete Claude model family through Vertex AI Model Garden and API endpoints

## Claude Desktop on Google Cloud

As of June 2026, organizations can deploy the full Claude Desktop experience (chat, Claude Cowork, and Claude Code) with inference running on Google Cloud. This enables:
- Inference in customer-controlled regions with local conversation history storage
- Enterprise SSO via Workforce Identity Federation or OIDC providers like Okta
- MDM policy deployment through Intune, GPO, or Jamf
- Pre-rollout validation of connectors and model availability before organization-wide rollout

## Related

- [[ClaudeDesktop]] — the unified desktop application deployable on Google Cloud
- [[VertexAI]] — Google Cloud's managed AI platform hosting Claude models
- [[Anthropic]] — Provider of Claude models distributed through Google Cloud
- [[Claude]] — AI models available on Google Cloud
- [[FedRAMP]] — Compliance standard for federal cloud services
- [[DoD-IL2]] — Department of Defense Impact Level 2 compliance
- [[GovernmentAI]] — AI adoption in federal and defense agencies
- [[CloudInference]] — the pattern of running AI inference within the customer's own cloud
- [[summary-2026-06-22 - The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry]] — source article
- [[summary-15 - Building with Claude on Google Cloud]] — source summary
