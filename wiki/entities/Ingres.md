---
title: "Ingres"
type: entity
tags: [database, relational, Berkeley, history]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260916 - Creator of Postgres (Turing Award)： ＂One Size Fits None＂, Leveraging GPUs, Difficult Implementations.md"]
last_updated: 2026-09-23
---

## Definition

Ingres (transcribed variously as "Ingress"/"Incorous") is the relational database Michael Stonebraker and Eugene Wong began building at Berkeley in 1972; it became Ingres Corporation in 1980.

## Key Information

- Started in 1972 after Ted Codd's 1970 relational paper, as an alternative to the Codasyl network proposal and IBM's hierarchical IMS.
- Ran on Unix and spread to about 100 universities; Arizona State's student-records project failed because Unix had no COBOL, prompting the 1980 founding of Ingres Corporation (moving the system to DEC VMS with real commercial support).
- Ingres Corporation implemented referential integrity, while Oracle's manual promised it "not yet implemented."
- Its hardcoded data types couldn't support GIS types or custom date math — the gap Postgres was built to fill with an extensible type system.
- The original version of Ingres was written entirely from scratch; there was no existing B-tree library to reuse.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — co-creator
- [[Eugene Wong]] — co-creator
- [[Ted Codd]] — whose paper inspired it
- [[PostgreSQL]] — the successor system
- [[Oracle]] — the competitor
- [[Larry Ellison]] — Oracle's salesman
- [[UC Berkeley]] — where it was built
- [[Databases]] — the broader field
