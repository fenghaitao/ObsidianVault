---
title: "AtlasPlatform"
type: entity
tags: [platform, internal-developer-platform, kubernetes, cloud-native, banking-circle]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Atlas is the internal developer platform (IDP) at Banking Circle, designed to abstract away infrastructure and cloud complexity so that engineering teams can focus on building their systems. It consists of multiple sub-platforms serving compute, infrastructure, messaging, and observability needs.

## Key Information
- Built and maintained by Banking Circle's platform engineering team
- Serves 250+ engineers across API development, core banking, internal tools, data science, and clearing scheme integrations
- **Compute sub-platform**: based on Kubernetes for running applications
- **Infrastructure sub-platform**: provisioning of blob storage, databases, and secret management systems
- **Messaging sub-platform**: enables communication between different applications and systems
- **Observability sub-platform**: monitors applications and payment processing
- Designed with the goal of self-service: engineers (and their AI agents) should be able to provision resources and deploy applications without human intervention
- Platform engineering journey was not always easy — the talk uses a fictionalized story to illustrate common pain points (copying pipelines, waiting for infrastructure teams, fragmented documentation)

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[BankingCircle]] — the company that built Atlas
- [[JuanHerrerosElorza]] — team lead for the cloud native technology team
- [[PlatformEngineering]] — the discipline
- [[InternalDeveloperPlatform]] — the broader concept
- [[Kubernetes]] — compute platform foundation
- [[SelfServicePlatform]] — key design principle
