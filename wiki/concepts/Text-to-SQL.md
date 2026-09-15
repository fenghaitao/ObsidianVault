---
title: "Text-to-SQL"
type: concept
tags: [AI, databases, LLM, benchmarks, SQL]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

Text-to-SQL is the task of converting natural-language questions into SQL. Mike Stonebraker demonstrates that large language models score ~0% on real data-warehouse queries despite ~80–85% accuracy on public benchmarks.

## Key Information

- On four production data-warehouse workloads (published in anonymized form as the "Beaver" benchmark), LLMs get 0%; with RAG and similar tricks, ~10%; with the FROM and JOIN clauses supplied in the prompt, ~35%.
- Why public benchmarks flatter LLMs: warehouse data isn't in the training corpus; real queries are ~100 lines (vs. 10–20 for Spider/BIRD); schemas are messy (redundant materialized views, non-mnemonic column names); data is idiosyncratic (e.g., MIT's January "J-term").
- A knowledgeable SQL user with the schema scores very high (~90%).
- Conclusion: give the retrieval system simpler pieces (including FROM/JOIN), and for heterogeneous sources (SQL, CAD, regulations-as-text) turn everything into tables and join in SQL with a query optimizer.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — published the benchmark
- [[Databases]] — the target systems
- [[Query Optimizer]] — how he joins the tables
- [[Machine Learning]] — the field of the models under test
