---
title: "MySQL"
type: entity
tags: [tool, database]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

MySQL is an open-source relational database. At Uber it was the engine behind sharded datastores (Schemaless), where Joakim Recht began the Odin project.

## Key Information

- Schemaless was based on sharded MySQL
- Early MySQL operations at Uber used bare metal and Puppet, requiring manual "puppet mangling" for promotions and maintenance
- Running sharded MySQL was expensive (each database required at least ~9 physical servers), motivating containerization
- Odin's scope later expanded from Schemaless MySQL to standard MySQL, Cassandra, and beyond

- Mike Stonebraker: when Oracle acquired MySQL, people got afraid and moved to Postgres — the genesis of Postgres replacing MySQL as the preferred open-source relational database.

## Related

- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Schemaless]] — sharded-MySQL object store
- [[Odin]] — platform that automated MySQL operations
- [[Uber]] — company context
- [[Docker]] — used to containerize MySQL
- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — on the Postgres migration
- [[Oracle]] — the acquirer
- [[PostgreSQL]] — the beneficiary
