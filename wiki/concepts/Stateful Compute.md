---
title: "Stateful Compute"
type: concept
tags: [infrastructure, agents, paradigm-shift, durable-execution, compute]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev.md"]
last_updated: 2026-06-29
---

## Definition

Stateful Compute is the paradigm shift in backend infrastructure where the compute layer maintains meaningful state — as opposed to the 30-year dominant Shared Nothing Architecture where compute is stateless and all state lives in a database. Eric Allam argues that AI agents force this transition, with snapshot and restore capabilities at its heart.

## Key Information

- **The old paradigm**: For 30 years (CGI → LAMP → Rails → Node → serverless), backend infrastructure followed the Shared Nothing Architecture: compute is stateless, state lives in the database. The equation was "request + DB = response."
- **Why agents demand stateful compute**: Agents accumulate meaningful state in the compute layer — cloned repos, installed packages, in-memory datasets, running dev servers, sandboxed subprocesses. This state cannot be externalized to a database and recreated from scratch on each turn.
- **The shift**: Agents are forcing backend infrastructure to move from stateless to stateful compute. The compute layer must preserve its state across turns, not just across requests.
- **Enabling technology**: Snapshot and Restore (VM-level checkpoint/restore) makes stateful compute practical by capturing the entire machine state and restoring it on demand, without keeping the machine continuously running.
- **Historical precedent**: IBM mainframes (1966) had checkpoint/restore for expensive long-running jobs. The concept isn't new but is being revived for the agent era.
- **Implications**: This represents a fundamental rethinking of backend infrastructure — not an incremental improvement but a paradigm-level change in how we think about compute state.

## Related

- [[Shared Nothing Architecture]] — the old paradigm being displaced
- [[Snapshot and Restore]] — the enabling technology
- [[Execution Snapshot]] — capturing compute state
- [[Context Log]] — the context half of durability
- [[DurableAgents]] — the broader concept
- [[MicroVMArchitecture]] — related infrastructure pattern
- [[FCRun]] — open-source implementation
- [[summary-20260510 - Two Roads to Durable Agents： Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev]] — source
