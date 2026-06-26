---
title: "summary-20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual"
type: source
tags: [source, transcript, genbi, enterprise-ai, business-intelligence]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual.md"]
last_updated: 2026-06-25
---

## Core Summary
Asaf Bord shares how Northwestern Mutual built a GenBI (Gen AI + Business Intelligence) agent at a 160-year-old, risk-averse Fortune 100 company. The key strategy was an incremental, phased approach with six-week sprints delivering tangible business value at each stage, allowing leadership to pull the plug at any point. By using real messy data, involving end users in the research process, and adopting a crawl-walk-run rollout (BI experts → business managers → executives), the team built trust while delivering immediate impact like automating 80% of report-finding work.

## Key Points
- GenBI fuses Gen AI and BI to create an agent that answers business questions with data, aiming for data democratization
- Northwestern Mutual's risk-averse culture (160-year history, "generational responsibility") required careful trust-building with both users and leadership
- Using real messy data instead of synthesized data ensured lab results would translate to production and brought subject matter experts into the research process
- The crawl-walk-run approach rolled out first to BI experts, then business managers, with executives as a distant vision
- Phase 1 started with report-finding (not SQL generation) to build inherent trust by surfacing already-certified assets
- A multi-agent architecture (metadata agent, RAG agent, SQL agent, BI agent) allowed each component to be productized independently
- The RAG agent alone automated ~80% of the work of two full-time BI team members who only found and shared reports
- Metadata enrichment learnings fed into a parallel semantic layer initiative, proving LLM performance improves with good metadata
- Incremental delivery eliminated sunk cost bias and allowed comparison against third-party solutions like Databricks Genie
- Future considerations include SaaS pricing shifting from per-seat to usage-based models in the Gen AI era

## Related
- [[AsafBord]] — speaker, Northwestern Mutual
- [[NorthwesternMutual]] — Fortune 100 financial services company
- [[DatabricksGenie]] — third-party GenBI competitor
- [[GenBI]] — fusion of Gen AI and Business Intelligence
- [[CrawlWalkRun]] — phased rollout methodology
- [[IncrementalDelivery]] — six-week sprint strategy with tangible deliverables
- [[MetadataEnrichment]] — improving data context for LLM performance
- [[MultiAgentArchitecture]] — pipeline of specialized AI agents
- [[DataDemocratization]] — making data accessible without BI team dependency
- [[SunkCostBias]] — risk addressed by allowing pull-the-plug at any phase
