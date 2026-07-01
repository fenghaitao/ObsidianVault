---
title: "PlatformEngineering"
type: concept
tags: [platform-engineering, devops, internal-developer-platform, cloud-native, self-service]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza.md"]
last_updated: 2026-06-30
---

## Definition
Platform engineering is the discipline of designing and building internal developer platforms (IDPs) that abstract away infrastructure and cloud complexity, enabling development teams to self-serve their compute, storage, networking, messaging, and observability needs. The goal is to reduce cognitive load on developers so they can focus on building business systems.

## Key Information
- Centralizes and productizes common infrastructure concerns (compute, databases, secrets, messaging, observability) behind a unified platform
- Reduces reliance on tribal knowledge, manual handoffs, and waiting for infrastructure teams
- Banking Circle's Atlas is an example: sub-platforms for compute (Kubernetes), infrastructure (blob storage, databases, secrets), messaging, and observability
- Juan Herreros Elorza argues that platform engineering must now serve two user classes: human developers and AI coding agents
- AI agents expose platform friction more acutely — a developer can walk to the second floor to ask for help, but an agent cannot
- Key principles for AI-ready platform engineering: self-service, API-first, local-first validation, agent-friendly observability, structured documentation, and contribution guardrails
- Measuring success: DORA metrics (change frequency, MTTR, lead time, change failure rate), reliability metrics, support request volume, SPACE framework for developer experience

## Related
- [[summary-20260408 - Platforms for Humans and Machines： Engineering for the Age of Agents — Juan Herreros Elorza]] — source transcript
- [[JuanHerrerosElorza]] — speaker, platform engineering team lead
- [[BankingCircle]] — example organization
- [[AtlasPlatform]] — example internal developer platform
- [[InternalDeveloperPlatform]] — the product of platform engineering
- [[SelfServicePlatform]] — key design principle
- [[APIFirstDesign]] — key design principle
- [[AgentReadyPlatform]] — platforms designed for AI agent consumption
- [[ShiftLeftValidation]] — validation strategy
- [[DORA]] — measurement framework
