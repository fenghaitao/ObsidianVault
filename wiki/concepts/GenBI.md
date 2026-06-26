---
title: "GenBI"
type: concept
tags: [concept, gen-ai, business-intelligence, agent, data-democratization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual.md"]
last_updated: 2026-06-25
---

## Definition
GenBI is the fusion of Generative AI and Business Intelligence — an AI agent that helps people answer business questions with data, similar to how a human BI analyst would. Its primary goal is data democratization: giving users access to data insights without relying on a BI team.

## Key Information
- Combines Gen AI capabilities with traditional BI to create an interactive data-answering agent
- Core motivation is data democratization — access to data at your fingertips without BI team dependency
- Northwestern Mutual's implementation uses a multi-agent architecture: metadata agent, RAG agent, SQL agent, and BI agent
- Initial phase focused on finding and surfacing existing certified reports rather than generating SQL from scratch
- The RAG agent component alone automated ~80% of report-finding work for a 10-person BI team
- Key challenges: no prior art, messy real-world data, blind trust bias, and enterprise budget justification
- Third-party solutions exist (e.g., Databricks Genie) but may be harder to govern than internally built systems
- Building GenBI requires understanding what good metadata looks like for LLMs, which differs from human-oriented metadata

## Related
- [[summary-20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual]] — source transcript
- [[NorthwesternMutual]] — company building GenBI
- [[AsafBord]] — research lead
- [[DatabricksGenie]] — third-party GenBI solution
- [[MultiAgentArchitecture]] — technical architecture pattern
- [[DataDemocratization]] — core motivation
- [[MetadataEnrichment]] — key enabler for GenBI performance
