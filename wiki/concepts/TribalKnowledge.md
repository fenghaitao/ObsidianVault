---
title: "TribalKnowledge"
type: concept
tags: [knowledge-management, documentation, software-engineering, developer-experience]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Tribal Knowledge is information about a software system — its requirements, design rationale, external interfaces, and operational context — that exists only in the minds of team members and is not written down anywhere accessible.

## Key Information
- AI coding agents cannot access tribal knowledge: they did not attend verbal meetings, hear hallway conversations, or absorb unwritten cultural understanding
- Many organizations depend on tribal knowledge to understand system requirements, why code was written, and specifications
- Anything that cannot be inferred from the code itself must be written down somewhere the agent can access
- Examples of tribal knowledge gaps: the shape of data from an external API parameter, the business reason for a design decision, unwritten specifications
- Documentation of code structure may become less necessary (agents can analyze and explain code), but documentation of intent and external context becomes more critical
- This is a particular challenge for large enterprises with long-lived legacy systems and high team turnover
- Writing down tribal knowledge is a "no regrets" investment that helps both human onboarding and agent effectiveness
- **Demand-Driven Context**: Raj identifies tribal knowledge as 40% of enterprise knowledge — the largest single category. Agent failures are the most effective mechanism for surfacing tribal knowledge: "Unless you don't do this way, you will never know what is not documented." The Demand-Driven Context cycle surfaces specific tribal knowledge gaps through agent failure checklists.

## Related
- [[summary-20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One]] — source transcript
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[AICodingAgents]] — systems that cannot access tribal knowledge
- [[DeveloperExperience]] — field concerned with knowledge management
- [[NoRegretsInvestments]] — documenting tribal knowledge as a no-regrets investment
- [[DemandDriven Context]] — methodology for surfacing tribal knowledge
- [[Agent Failure as Discovery]] — using failures to surface tribal knowledge
- [[Knowledge Base Monolith]] — tribal knowledge is 40% of the monolith
- [[Institutional Knowledge]] — broader category containing tribal knowledge
