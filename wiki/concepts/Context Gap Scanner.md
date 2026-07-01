---
title: "Context Gap Scanner"
type: concept
tags: [automation, knowledge-base, agents, testing, enterprise-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
The Context Gap Scanner is an automated tool that implements the Demand-Driven Context methodology at scale. It takes past work items (Jira tickets, incidents, customer support tickets), validates each against the knowledge base, and produces a consolidated report of documentation quality — identifying what's clean, stale, incomplete, or entirely missing.

## Key Information
- **Three-Step Process**: (1) Generate probes — basic tests to validate knowledge. (2) Run probes against the knowledge base. (3) Analyze gaps and produce a consolidated report.
- **Per-Incident Analysis**: For each work item, the scanner checks if documentation exists for referenced systems, APIs, and processes. It flags: missing documentation (never written), stale documentation (old, potentially untrustworthy), and incomplete documentation.
- **Consolidated Output**: Classifies knowledge as clean, stale, incomplete, or entirely missing. Identifies what's tribal knowledge. Creates a Kanban board of documentation gaps organized by critical/high/medium priority.
- **Criticality Ranking**: Items that repeatedly appear across multiple incidents are ranked as critical — these are the highest-priority documentation gaps to fix.
- **Automation Rationale**: Manual Demand-Driven Context cycles are painful (15+ cycles of sitting with an agent). Automation makes the approach practical at scale.
- **Data Sources**: Can connect to Confluence, Jira, Slack, GitHub, and other enterprise knowledge sources. The demo used flat files but the approach works with any data source.
- **Cost**: Inexpensive to run — per-domain knowledge bases average ~96K tokens. Running the scanner daily is unlikely to burn even $1 in API costs.
- **Live Demo**: Raj provided a publicly accessible Context Gap Scanner with presets for workshop attendees to try.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[DemandDriven Context]] — methodology the scanner automates
- [[Knowledge Base Kanban]] — output format of the scanner
- [[Agent Failure as Discovery]] — the principle the scanner operationalizes
- [[Knowledge Base Monolith]] — what the scanner analyzes
- [[Raj]] — creator of the scanner
