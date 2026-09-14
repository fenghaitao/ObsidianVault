---
title: "Schemaless"
type: entity
tags: [tool, database, Uber, MySQL]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md"]
last_updated: 2026-09-14
---

## Definition

Schemaless is Uber's object store ("schema-less"), based on sharded MySQL. It was the first workload Joakim Recht containerized and automated, seeding the Odin platform.

## Key Information

- Based on sharded MySQL; Recht's early job was managing, operating, monitoring, and scaling those MySQL shards
- Early setup was "bare metal, puppet, and MySQL" — every master promotion or maintenance required manual "puppet mangling"
- Running sharded MySQL is expensive (at least ~9 physical servers per database); containerizing improved utilization
- Containerizing Schemaless to run different MySQL versions and multiple databases per host was the prototype that led to Odin

## Related

- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Odin]] — the platform Schemaless spawned
- [[MySQL]] — underlying database technology
- [[Uber]] — company where Schemaless ran
- [[Docker]] — containerization applied to Schemaless
