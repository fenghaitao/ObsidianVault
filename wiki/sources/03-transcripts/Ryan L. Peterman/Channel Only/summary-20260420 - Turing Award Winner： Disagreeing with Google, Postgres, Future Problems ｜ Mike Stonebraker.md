---
title: "summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Core Summary

Mike Stonebraker recounts the arc of relational databases from Ingres through Postgres, arguing that "one size fits none" — specialized engines beat general-purpose ones by an order of magnitude — and that Google's MapReduce and eventual consistency were mistakes it later abandoned via Spanner. He then turns to unsolved problems: large language models score ~0% on his real data-warehouse text-to-SQL benchmark, and read-write agentic AI is becoming a distributed-database problem his startup DBOS is positioned for.

## Key Points

- Started Ingres at Berkeley in 1972 with Eugene Wong after Ted Codd's 1970 relational paper; it won Stonebraker tenure in 1976 and became Ingres Corporation in 1980 after the academic version hit real-world limits (e.g., Arizona State's student records without COBOL).
- Oracle's Larry Ellison competed partly through "shady" salesmanship — selling unshipped features and documented-but-unimplemented referential integrity — while Ingres Corporation had the feature implemented.
- Postgres was born when Ingres's hardcoded data types couldn't support extensible types (GIS shapes, bond-market date math); its key innovation was an extensible type system, plus inheritance and (later removed) time travel.
- Stonebraker identifies extraordinary engineers by asking deep technical questions about their own work (master's thesis, error handling, threads vs. processes); "smart" surfaces quickly in conversation.
- "One Size Fits All" (2004 paper): stream processing, column stores, and row stores differ by an order of magnitude, so specialized engines win; Postgres is the right low-end default but lacks columnar and multi-node support for big data warehouses.
- MapReduce and Hadoop were "ridiculously inefficient" versus distributed databases (the 2011 paper with David DeWitt et al.); Google also wrongly pushed eventual consistency, sacrificing integrity constraints — later abandoned when Jeff Dean's Spanner shipped conventional transactions.
- Amazon supports ~15 database systems, which Stonebraker says is ~12 too many; graph databases are almost never the performant option and should be a layer over a relational system.
- DBOS (started 2023) descends from the idea of replacing the upper half of Linux with a database system; today it sells seamless TypeScript/Java/Go/Python with transactional, durable workflows, where ~2/3 of customers do agentic AI.
- On real data warehouses, LLM text-to-SQL scores ~0%, ~10% with RAG, and ~35% when given the FROM and JOIN clauses — because warehouse data isn't in training sets, queries are ~100 lines, schemas are messy, and data is idiosyncratic; the benchmark is published as "Beaver."
- His approach to text-to-SQL over heterogenous sources (SQL, CAD, text) is to turn everything into tables and join in SQL with a query optimizer.
- To learn databases he recommends the "Red Book" (Readings in Database Systems, with Joe Hellerstein); to his younger self he advises "think outside the box" and to pick a problem that isn't going with the flow, and warns computer science may not be a growth industry going forward.

## Related

- [[Michael Stonebraker]] — the guest
- [[PostgreSQL]] — the database he created
- [[Ingres]] — his first database
- [[Ted Codd]] — whose paper inspired Ingres
- [[Eugene Wong]] — his early mentor and collaborator
- [[Oracle]] — the competitor
- [[Larry Ellison]] — Oracle's founder
- [[Google]] — whose MapReduce/eventual-consistency he disputed
- [[Jeff Dean]] — led Spanner's transactional correction
- [[Google Spanner]] — Google's transactional system
- [[MapReduce]] — the model he disputed
- [[Hadoop]] — the reimplementation he called inefficient
- [[Databases]] — the field of his work
- [[One Size Does Not Fit All]] — his core thesis
- [[Eventual Consistency]] — the model he rejected
- [[Text-to-SQL]] — the benchmark failure he showed
- [[Agentic AI]] — the market DBOS targets
- [[Query Optimizer]] — the hardest part of a database
- [[DBOS]] — his current company
- [[Databricks]] — where the DBOS idea originated
- [[Apache Spark]] — Matei Zaharia's creation
- [[Matei Zaharia]] — Databricks/Spark founder
- [[David DeWitt]] — 2011 paper collaborator
- [[StreamBase]] — his stream-processing company
- [[Vertica]] — his column-store company
