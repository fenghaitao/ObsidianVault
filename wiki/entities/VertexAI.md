---
title: "Vertex AI"
type: entity
tags: [ai-platform, google-cloud, ml-platform, managed-service]
sources: [raw/01-articles/claude/2025-04-02 - Claude on Google Cloud's Vertex AI FedRAMP High and IL2 Authorized.md, raw/01-articles/claude/2025-06-23 - Introducing Citations on the Anthropic API.md, raw/01-articles/claude/2025-08-14 - Prompt caching with Claude.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md]
last_updated: 2026-06-28
---

## Definition

Vertex AI is Google Cloud's unified AI and machine learning platform for building, deploying, and managing AI/ML models and applications.

## Key Information

- Managed and serverless platform offering AI/ML models as APIs.
- Provides [[VertexAI#Model Garden|Model Garden]] for accessing pre-built and custom models.
- Eliminates the need for infrastructure provisioning and management.
- Supports government and defense workloads through [[VertexAI#Assured Workloads|Assured Workloads]].

## Claude on Vertex AI

Vertex AI provides access to [[Claude]] models with government compliance features and advanced capabilities:
- **FedRAMP High Authorization**: Federal agencies can use Claude through Vertex AI in compliance with FedRAMP High standards for sensitive unclassified data.
- **DoD IL2 Support**: Defense contractors can use Claude with [[DoD_IL2]] compliance for non-controlled unclassified information.
- **Managed Infrastructure**: Fully serverless APIs eliminate the need for agencies to provision infrastructure.
- **Complete Model Family**: Access to all [[Claude]] models including [[Claude3.7Sonnet]].
- **Assured Workloads**: Enhanced security and compliance controls for government workloads.
- **Citations**: Support for [[Citations]] feature enabling grounded responses with precise source citations (available June 23, 2025).
- **Prompt Caching**: [[PromptCaching]] available in preview on Vertex AI, reducing costs by up to 90% and latency by up to 85% for long-context applications.

## Getting Started with Claude on Vertex AI

1. Set up a [[GoogleCloud]] environment with Assured Workloads for FedRAMP High or IL2
2. Access Claude models through the Vertex AI Model Garden
3. Build with Claude using the Vertex AI API endpoints

## Related

- [[GoogleCloud]] — Cloud provider hosting Vertex AI platform
- [[Claude]] — AI models available on Vertex AI
- [[Claude3.7Sonnet]] — Latest Claude model on Vertex AI
- [[FedRAMP]] — Compliance standard for federal cloud services
- [[DoD_IL2]] — Department of Defense Impact Level 2 compliance
- [[GovernmentAI]] — Government and defense AI adoption
- [[Anthropic]] — Provider of Claude models
- [[Citations]] — API feature for citations available on Vertex AI
- [[PromptCaching]] — API feature available in preview on Vertex AI
- [[summary-2025-08-14 - Prompt caching with Claude]] — article noting Vertex AI preview availability
