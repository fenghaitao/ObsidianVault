---
title: "Context Blocks"
type: concept
tags: [context-management, knowledge-base, agents, enterprise-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Context Blocks are curated, agent-usable chunks of institutional knowledge, analogous to microservices decomposed from a monolithic legacy system. They are the output of the Demand-Driven Context methodology — organized, validated pieces of domain knowledge that agents can reliably consume to complete enterprise tasks.

## Key Information
- **Analogy**: Context blocks are to knowledge bases what microservices are to monolithic applications — decomposed, independently useful, and well-defined.
- **80/20 Rule**: 20% of documentation provides 80% of value. Context blocks should capture this critical 20% as a "cache database" for agents, with the remaining 80% accessible via links when agents need more detail.
- **Storage**: Raj prefers GitHub repositories for context block storage because they provide built-in PR processes, review workflows, and conflict resolution for multi-agent, multi-team contributions.
- **Meta Model Integration**: Context blocks are organized according to a meta model (business processes → systems → APIs → jargon), giving agents a navigation map.
- **Creation Process**: Context blocks are created through the Demand-Driven Context cycle: agent fails on a task → surfaces missing knowledge → domain expert provides it → agent curates it into a context block.
- **Entity Discovery**: One problem cycle can surface 6 undocumented entities and discover 5-6 more through curation — the knowledge base grows organically through use.
- **Confidence Tracking**: Context blocks carry confidence scores that improve as they are validated across multiple work items (from 1.5 to 4.4+ after ~14 cycles).

## Related
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Demand-Driven Context]] — methodology that produces context blocks
- [[Knowledge Base Monolith]] — what context blocks decompose
- [[Meta Model]] — organizational structure for context blocks
- [[Knowledge Curation]] — the process of creating context blocks
- [[Agent as Knowledge Manager]] — agent role in maintaining context blocks
- [[Context Management]] — broader field
