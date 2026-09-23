---
title: "Agentic AI"
type: concept
tags: [AI, agents, LLM, databases, workflows]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky.md"]
last_updated: 2026-09-23
---

## Definition

Agentic AI refers to LLM-driven agents that take actions. Mike Stonebraker argues most agentic AI is read-only today but will quickly become read-write, turning it into a distributed-database problem.

## Key Information

- About two-thirds of DBOS's customers do agentic AI.
- Most agentic AI today is read-only: it runs computation and produces a prediction handed to a person, without updating source state.
- Read-write agents (e.g., two agents moving $100 across two accounts) need commit-or-roll-back atomicity — a workflow that "all happens or it looks like it never happened."
- Stonebraker expects the shift to read-write to make applications "very, very databasey," which he sees as favorable for DBOS's transactional, durable workflows.
- Odersky: for agentic AI, give agents very precise, fine-grained capabilities (what they can/cannot do) so we remain confident they "will not be able to leak my API keys or my email."
- Capabilities must prevent both forgetting and forging; Scala ships an experimental capability-tracking feature for this.
- He advocates keeping prompts as first-class program values so an LLM change stays incremental rather than nondeterministically regenerating already-reviewed code.

## Related

- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — the prediction
- [[DBOS]] — the company positioned for it
- [[Databases]] — what read-write agents require
- [[AI and Software Engineering]] — the broader impact of AI
- [[Martin Odersky]] — capabilities for agents
- [[Capability-Based Security]] — the mechanism he proposes
- [[Scala]] — halfway there with capability tracking
- [[Type System]] — the reviewable human/AI contract
- [[summary-20260831 - Creator of Scala： Comparing Languages And How AI Will Impact Them ｜ Martin Odersky]] — source summary
