---
title: "LeadQualificationAgents"
type: concept
tags: [agents, sales, lead-qualification, automation, crewai, crm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"]
last_updated: 2026-06-26
---

## Definition
Lead Qualification Agents are a specialized AI agent crew that automates the sales lead qualification process. The crew analyzes lead responses, researches industries, cross-references CRM data, and produces scores, use cases, and talking points to prepare salespeople for high-quality conversations.

## Key Information
- Demonstrated by Joao Moura at CrewAI with a three-agent crew:
  - **Lead Analyst Expert**: Analyzes lead responses and form data
  - **Industry Researcher Specialist**: Researches the prospect's industry, market position, and relevant context
  - **Strategic Planner**: Synthesizes findings into lead scores, use cases, and talking points for sales calls
- The crew takes raw lead responses as input and produces actionable sales preparation material
- Cross-references CRM data during analysis for enriched context
- Result: Enabled 15+ customer calls in 2 weeks — the system worked so well it created more qualified leads than the founder could initially handle
- Represents a "low risk, high impact" use case: automating preparation work without replacing the human relationship-building in sales calls
- Human still conducts the actual sales conversation, but arrives fully briefed with relevant talking points

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source
- [[AgentCompanyPattern]] — broader pattern this is part of
- [[AgentCrewOrchestration]] — technical orchestration underneath
- [[CrewAI]] — framework used
