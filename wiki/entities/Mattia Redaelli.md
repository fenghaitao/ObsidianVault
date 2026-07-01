---
title: "Mattia Redaelli"
type: entity
category: person
tags: [person, ai-engineer, enterprise, mcp, a2a, quantyca]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
Mattia Redaelli is an AI Engineer at Quantyca. He presented the development workflow, blueprint repositories, CICD pipeline, and runtime architecture of Amplifon's enterprise registry platform at the aiDotEngineer conference.

## Key Information
- **Role**: AI Engineer at [[Quantyca]]
- **Presentation**: "One Registry to Rule them All" at [[aiDotEngineer]], co-presented with Sonny Merla and Mauro Luchetti
- **Key Technical Topics**: Blueprint repositories (GitHub template repos for MCP and A2A with FastAPI, Docker, auth, cost tracking, LangFuse integration), CICD pipeline (GitHub Actions for Docker image publishing and metadata publishing to registries), runtime proxy architecture (AI Gateway routing to MCP/A2A proxies that look up backend URLs from the registry catalog), platform walkthrough (dashboard, catalog views, inspector pages, widget forms, lineage view)
- **Blueprint Design**: A2A blueprint is framework-agnostic using interfaces and ports so teams can implement agents in their framework of choice; important thing is consistent interface

## Related
- [[Quantyca]] — employer
- [[Sonny Merla]] — co-presenter from Amplifon
- [[Mauro Luchetti]] — co-presenter from Quantyca
- [[Amplifon]] — client organization
- [[Blueprint Repository]] — template repos presented
- [[CICD Agent Publishing]] — automated metadata publishing presented
- [[Lineage View]] — traceability visualization presented
- [[LangFuse]] — observability tool integrated into blueprints
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
