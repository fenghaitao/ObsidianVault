---
title: "AgentProductionDeployment"
type: concept
tags: [agents, deployment, production, api, crewai, autoscaling, enterprise]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"]
last_updated: 2026-06-26
---

## Definition
Agent Production Deployment is the process of taking agent crews from local development (terminal) to a production-ready API with autoscaling, authentication, private networking, and UI integration — enabling agents to serve as backend services in production applications.

## Key Information
- Demonstrated through CrewAI Plus, an enterprise offering:
  - Build crews locally in the terminal
  - Push crews to GitHub in 3 minutes
  - Crews become a real API with autoscaling
  - Protected by bearer token authentication
  - Runs within a private VPC
  - One-click export to a React component for demo/customizable UI
- Agents can be connected to any frontend or service within minutes
- Addresses the gap between prototyping agents and running them reliably in production
- First 50 companies get access within 24 hours (launch offer)
- Meta-feature: A crew that builds crews — given an email and company name, it creates a crew, pushes to GitHub, and deploys — self-referential deployment automation

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[CrewAI]] — platform offering this capability
- [[AgentCrewOrchestration]] — crews being deployed
- [[AgentCompanyPattern]] — business pattern enabled by production deployment
- [[TemporalWorkflows]] — alternative production deployment approach for durable agents
