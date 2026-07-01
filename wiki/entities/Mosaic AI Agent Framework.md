---
title: "Mosaic AI Agent Framework"
type: entity
tags: [tool, agent-framework, databricks, orchestration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik.md"]
last_updated: 2026-06-30
---

## Definition
Mosaic AI Agent Framework is a Databricks component that works with LangGraph to handle multi-agent orchestration on the Databricks Data Intelligence Platform. It manages the workflow graph and determines which agents to call in what order, forming the orchestration layer of production multi-agent systems.

## Key Information
- Part of the Databricks Data Intelligence Platform
- Works alongside LangGraph for multi-agent orchestration
- Manages workflow graphs (directed acyclic graphs) for agent execution
- Agents are implemented as Unity Catalog functions (SQL or Python) or registered models
- Integrates with Model Serving / Function Serving for deployment
- Circuit breaker policies (retries, timeouts, rate limits) enforced at the serving layer via AI Gateway
- Part of a production architecture that runs 24/7 across billions of transactions
- Used in conjunction with Delta Lake (state storage), MLflow (tracing), and Unity Catalog (governance)

## Related
- [[Databricks]] — platform
- [[LangGraph]] — orchestrator framework used with Mosaic AI
- [[Unity Catalog]] — governance and agent registration
- [[MLflow]] — tracing and evaluation
- [[Delta Lake]] — state version storage
- [[Agent Bricks]] — higher-level packaged orchestration patterns
- [[AI Gateway]] — circuit breaker enforcement layer
- [[summary-20260408 - From Chaos to Choreography： Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik]] — source
