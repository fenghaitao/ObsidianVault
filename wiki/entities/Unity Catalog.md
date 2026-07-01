---
title: "Unity Catalog"
type: entity
tags: [tool, governance, schema, databricks, data-catalog]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik.md"]
last_updated: 2026-06-30
---

## Definition
Unity Catalog is Databricks' centralized governance layer for data and AI assets. In multi-agent systems, it serves as the registry for agent input-output schemas (data contracts), making agents centrally discoverable, versioned, and governed. It provides access control, lineage tracking, and audit trails for both data and AI agents.

## Key Information
- Centralized governance for data and AI assets on Databricks
- Agents are registered as Unity Catalog functions (SQL or Python) or models
- Agent input-output schemas (data contracts) are versioned and governed in one place
- Makes agents centrally discoverable within an organization
- Provides access control, lineage, and audit trail for both data and agents
- Critical for operating multi-agent workflows in production — every agent's contract is versioned
- Enables schema validation at agent handoff boundaries
- Part of the production architecture: LangGraph → Unity Catalog functions → Model Serving → Delta Lake

## Related
- [[Databricks]] — platform
- [[Data Contracts (Agent)]] — schemas registered in Unity Catalog
- [[Mosaic AI Agent Framework]] — agent framework using Unity Catalog
- [[Delta Lake]] — complementary data layer
- [[MLflow]] — complementary tracing layer
- [[summary-20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik]] — source
