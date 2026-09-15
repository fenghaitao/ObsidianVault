---
title: "Agentic AI"
type: concept
tags: [AI, agents, LLM, databases, workflows]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

Agentic AI refers to LLM-driven agents that take actions. Mike Stonebraker argues most agentic AI is read-only today but will quickly become read-write, turning it into a distributed-database problem.

## Key Information

- About two-thirds of DBOS's customers do agentic AI.
- Most agentic AI today is read-only: it runs computation and produces a prediction handed to a person, without updating source state.
- Read-write agents (e.g., two agents moving $100 across two accounts) need commit-or-roll-back atomicity — a workflow that "all happens or it looks like it never happened."
- Stonebraker expects the shift to read-write to make applications "very, very databasey," which he sees as favorable for DBOS's transactional, durable workflows.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the prediction
- [[DBOS]] — the company positioned for it
- [[Databases]] — what read-write agents require
- [[AI and Software Engineering]] — the broader impact of AI
