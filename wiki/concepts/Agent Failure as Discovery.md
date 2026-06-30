---
title: "Agent Failure as Discovery"
type: concept
tags: [agents, knowledge-management, testing, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Agent Failure as Discovery is the principle that agent failures on real work items are the most effective mechanism for surfacing undocumented institutional knowledge. Rather than trying to predict what documentation is missing, you give agents problems they will fail on and let the failures reveal exactly what knowledge gaps exist.

## Key Information
- **Core Insight**: "Unless you don't do this way, you will never know what is not documented." Agent failures surface exactly what tribal knowledge is missing — something traditional documentation audits cannot do.
- **Checklist Generation**: When an agent fails, it produces a checklist of specific missing information: "I don't understand these terminologies," "This business logic is not documented," "I need information about this system."
- **Confidence Scoring**: Each failure includes a confidence score (1-5) indicating how well the knowledge base supports the task. Starting from 1.5 (everything critical/missing), confidence improves as gaps are filled.
- **Discovery vs Manual Audits**: Traditional approach: "There is documentation missing. We need to write." But what to write? Agent failures provide specific, actionable items rather than vague gaps.
- **Surfacing Tribal Knowledge**: The 40% of enterprise knowledge that is tribal (never documented) can only be surfaced by probing with real work items. Agent failures are the probe.
- **Scale**: One incident can surface 6 undocumented entities. 14 incidents can improve confidence from 1.5 to 4.4 while discovering and documenting dozens of entities.
- **Automation**: The Context Gap Scanner automates this principle at scale, running past work items against the knowledge base to produce a consolidated gap report.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Demand-Driven Context]] — methodology built on this principle
- [[Context Gap Scanner]] — automation of this principle
- [[TribalKnowledge]] — what failures surface
- [[Agent as Knowledge Manager]] — the agent role after discovery
- [[Knowledge Curation]] — what happens after discovery
- [[Pull vs Push Context]] — the paradigm enabling discovery
