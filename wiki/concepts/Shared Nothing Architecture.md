---
title: "Shared Nothing Architecture"
type: concept
tags: [infrastructure, backend, history, stateless, compute]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

Shared Nothing Architecture is the dominant backend infrastructure paradigm of the last 30 years, where the compute layer is stateless and all meaningful state resides in a database. The model is "request + DB = response" — each request is handled independently with no state retained in the compute layer between requests.

## Key Information

- **Origins**: CGI (1993) — each HTTP request forks a new process, request data goes in, process does work, writes response to stdout, process goes away. Completely stateless.
- **Evolution**: PHP/LAMP stack reused processes but kept the stateless principle. Ruby on Rails, Node.js, serverless — all followed the same paradigm.
- **Core principle**: The compute layer is stateless. State lives in the database. There is no meaningful state in compute.
- **Dominance**: Has been the dominant backend infrastructure model for 30 years (1993-2023).
- **Extension for async work**: As web apps became more complex, async side effects (emails, credit card charges, image resizing) were added. Multi-step side effects led to workflow/durable execution engines (the Replay Model).
- **Why agents break it**: Agents accumulate state in the compute layer (cloned repos, installed packages, running servers, in-memory data) that can't be externalized to a database. This state must survive between user turns.
- **Successor paradigm**: Stateful Compute — where the compute layer preserves meaningful state across turns, enabled by snapshot and restore.

## Related

- [[Stateful Compute]] — the paradigm shift away from shared nothing
- [[Replay Model]] — durability built on top of shared nothing architecture
- [[Snapshot and Restore]] — the approach that enables stateful compute
- [[DurableAgents]] — the broader concept
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
