---
title: "Render"
type: entity
tags: [deployment, cloud, platform, agents]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260508 - Shifra Williams - What your AI pipeline does when you're not looking - PyAI London at AIE 2026.md]
last_updated: 2026-06-25
---

## Definition

Render is a cloud platform for deploying full-stack apps and AI agents in production. Provides web services, background workers, cron jobs, and Render Workflows (durable, long-running services with checkpoint and recovery). Uses render.yaml for declarative infrastructure configuration.

## Key Information

- Zero-downtime deploys
- Render Workflows: launched in open beta May 2026 — durable, resilient, long-running with retry, checkpoint, and recovery
- render.yaml: simple declarative config with auto-injected database secrets
- PG Vector extension support for RAG workloads
- Free tier with credits available
- Founding DevRel: Shifra Williams

## Related

- [[DurableExecution]] — Render Workflows implements this
- [[Logfire]] — observability integration
- [[PydanticAI]] — agent framework deployable on Render
- [[ShifraWilliams]] — founding Developer Advocate
