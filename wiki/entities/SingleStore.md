---
title: "SingleStore"
type: entity
tags: [company, database, technology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

SingleStore is a database company where Braintrust's founder Ankur Goyal was one of the first employees. This background in database engineering contributed to the decision to build a custom database (Brainstorm) for agent traces at Braintrust rather than using existing OLAP solutions.

## Key Information

- Database technology company
- Braintrust founder Ankur Goyal was an early employee, giving him deep database engineering expertise
- Phil Hetzel joked that "only an insane person would build their own database" but noted the founder is "cut from that cloth" due to his SingleStore background
- This database expertise enabled Braintrust to design Brainstorm — a custom database built from the ground up for agent trace workloads with write-ahead log, text indexing (Tantivy), and SQL unification

## Related

- [[summary-20260528 - How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust]] — source
- [[Braintrust]] — company founded by former SingleStore employee
- [[ClickHouse]] — OLAP database Braintrust moved away from
- [[Tantivy]] — text indexing framework used in Brainstorm
