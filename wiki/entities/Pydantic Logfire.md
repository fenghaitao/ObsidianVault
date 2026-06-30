---
title: "Pydantic Logfire"
type: entity
tags: [tool, observability, platform, opentelemetry, evals, managed-variables, pydantic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
Pydantic Logfire is an observability platform built by the Pydantic company. Under the hood it is a general OpenTelemetry-based observability platform (logs, metrics, traces), but it markets as AI observability. It goes beyond standard observability with evals, managed variables, and (in development) autonomous agent optimization.

## Key Information
- Built on OpenTelemetry: supports logs, metrics, and traces
- Markets as AI observability because that's what customers want, but Colvin believes AI observability is a feature, not a category
- **Evals**: Provides eval views for comparing experiment runs, per-metric performance graphs, and case-level drill-down into where prompts differ
- **Managed Variables**: Any Pydantic model can be managed inside Logfire, enabling A/B testing via the OpenFeature standard, and runtime updates to prompts, models, and temperature without redeployment
- **Gateway**: Pydantic AI Gateway provides one API key for multiple model providers with caching, fallback, and observability
- **Self-driving managed variables (in development)**: Vision to wire GEPA optimization directly into managed variables for autonomous agent improvement
- Free tier is "extremely generous"
- Supports archiving old eval runs to keep the view clean
- Can configure to not send raw data (system prompts, inputs) for privacy-sensitive use cases
- Enterprise self-hosting available for VPC deployment
- Has an annotation system for recording human feedback against prompts
- Integrates with the cell AI protocol for building chat interfaces

## Related
- [[Pydantic]] — parent company
- [[Pydantic AI]] — agent framework it integrates with
- [[Samuel Colvin]] — creator
- [[Managed Variables]] — key feature
- [[GEPA]] — optimization algorithm
- [[Agent Optimization]] — core use case
- [[AI Observability]] — the category it operates in
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source
