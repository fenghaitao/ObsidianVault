---
title: "Odin"
type: entity
tags: [project, platform, infrastructure, Uber]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md"]
last_updated: 2026-09-14
---

## Definition

Odin was the platform project at Uber that automated and unified the operation of all stateful workloads (databases and storage), replacing per-team bare-metal toolchains with a single orchestration and monitoring platform.

## Key Information

- Started by running sharded MySQL (Schemaless) in Docker to improve utilization and management, using "goal state/intent" declarations instead of procedural puppet mangling
- Expanded to run any stateful workload for the whole company, growing from a team-local tool to ~120,000 physical servers and ~half a million databases operated by ~20 people
- Built an orchestration layer and monitoring on top of a traditional git-ops strategy, replacing a one-way push "hope for the best" workflow
- Had to work around technologies that were not container/cloud-ready (e.g., HDFS and Kafka were "notoriously bad at moving stuff around dynamically")
- Adoption was incremental ("build it, make it work, let people see it work") rather than forcing everyone at once; eventually leadership mandated "Odin is the future" for stateful workloads
- The project's natural scope expansion drove Joakim Recht's promotions through principal to distinguished engineer

## Related

- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Joakim Recht]] — built Odin
- [[Uber]] — company where Odin ran
- [[Schemaless]] — the first workload Odin managed
- [[Docker]] — containerization technology used
- [[Kubernetes]] — orchestration emerging at the time
- [[Force Multiplier]] — Odin as a technology force multiplier
