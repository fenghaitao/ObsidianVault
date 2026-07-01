---
title: "Knowledge Curation"
type: concept
tags: [knowledge-management, agents, documentation, enterprise-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Knowledge Curation is the process by which agents discover, document, and organize institutional knowledge during problem-solving. In the Demand-Driven Context cycle, after a domain expert fills knowledge gaps surfaced by agent failure, the agent curates that knowledge into structured context blocks for future reuse.

## Key Information
- **Part of the Cycle**: Step 6 of the Demand-Driven Context cycle — after the problem is solved, the agent takes the newly provided knowledge and curates it into the knowledge base.
- **Entity Discovery**: One problem cycle can surface 6 undocumented entities and, through curation, discover 5-6 more related entities that were also never documented.
- **Structured Output**: Curation produces context blocks organized according to the meta model (business processes → systems → APIs → jargon), not flat dumps of information.
- **State Tracking**: Curated knowledge carries metadata including creation date, last updated, and state (clean, stale, incomplete), enabling agents to assess trustworthiness.
- **Storage**: Raj prefers GitHub repositories for curated knowledge because they provide PR processes, review workflows, and conflict resolution for multi-agent contributions.
- **Gradual Build-Up**: Knowledge curation is cumulative — each cycle adds to the knowledge base, gradually improving agent confidence from ~1.5 to ~4.4+.
- **Contrast with Manual Documentation**: Traditional knowledge management requires humans to decide what to document and write it. Curation is demand-driven — only what's needed to solve real problems gets documented.

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[DemandDriven Context]] — methodology that includes curation
- [[Agent as Knowledge Manager]] — the agent role performing curation
- [[Context Blocks]] — the output of curation
- [[Knowledge Base Monolith]] — what curation transforms
- [[Meta Model]] — organizational structure for curated knowledge
- [[Knowledge Base Kanban]] — tracks curation progress
