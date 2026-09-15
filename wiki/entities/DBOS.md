---
title: "DBOS"
type: entity
tags: [company, database, operating-system, workflows, agentic-AI]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

DBOS (transcribed "DeBoss"/"Debboss") is the company founded in 2023 from the academic idea of replacing the upper half of Linux with a database system; it now sells a seamless programming model with transactional, durable workflows in TypeScript, Java, Go, and Python.

## Key Information

- Academic origin (Berkeley/Stanford, early 2020s): "most everything you do in an operating system is managing data at scale," so keep the device-driver layer and replace the rest with a database; a filesystem on top of a DBMS was reportedly faster than Linux's, with failover giving high availability.
- VCs rejected "displacing Linux" but funded the programming-language idea: JavaScript extensions giving programs durable, transactional state with failover.
- Today sells "vanilla-looking" versions of TypeScript, Java, Go, and Python where workflow steps are transactional and workflows are durable (and can be atomic — all-or-nothing).
- ~2/3 of customers do agentic AI; most agentic AI today is read-only, and Stonebraker expects read-write agents to make applications "very, very databasey" — a market DBOS is positioned for.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — founder
- [[Matei Zaharia]] — where the scheduling idea originated
- [[Databricks]] — the scheduling problem that seeded it
- [[Agentic AI]] — the market it serves
- [[PostgreSQL]] — the database technology underneath
