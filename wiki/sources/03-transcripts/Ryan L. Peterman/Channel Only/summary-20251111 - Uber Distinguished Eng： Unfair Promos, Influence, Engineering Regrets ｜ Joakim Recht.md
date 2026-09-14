---
title: "summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md"]
last_updated: 2026-09-14
---

## Core Summary

Joakim Recht, one of Uber's few Distinguished Engineers, describes how Odin — a platform to containerize and automate Uber's stateful workloads — grew from a team-local tool to running ~120,000 physical servers and ~half a million databases, and how that natural scope expansion drove his promotions. He argues that a software engineer must keep writing code, that promotions are only approximately fair because they hinge on how well a manager presents a case, and that real influence comes from leading by example and enabling others rather than top-down authority. He left Uber after management changes eroded the engineering culture he valued.

## Key Points

- Odin started by running sharded MySQL (Schemaless) in Docker to improve utilization and management, then expanded into a single platform operating all of Uber's stateful workloads (previously ~52 database technologies, each with its own team and toolchain)
- The driver was an aversion to doing things repeatedly: automating waste — first your own, then other people's — powers scope expansion and influence
- Promotions followed the work's scope expansion: first version → promotion, expansion to standard MySQL/Cassandra → principal, and hand-off of the mature self-running platform → distinguished engineer
- Promos are "pretty fair" but not always: early Uber promo committees put all managers/VPs/senior engineers and senior ICs in a room going through hundreds of engineers with no prep, so "it all depends on how good is your manager at presenting your case"
- "A software engineer needs to write code. If you're not writing code, you're not a software engineer" — applying at every level; he wrote daily through Distinguished
- "Running code beats perfect code" — ship something to get feedback rather than polishing until it handles every case
- Influence: lead by example, take the shovel/boring work yourself and delegate the hard-but-growth work down; the best outcome is "when the other person thinks the idea is theirs"; never aim for 100% adoption
- Mentorship: prefer mentees outside your own org to plant seeds and get two-way benefit; keep it informal and unscheduled
- He left Uber after a management change and a top-down on-prem→cloud decision (based on a price claim "no engineer believed") triggered a drain of senior engineers

## Related

- [[Joakim Recht]] — the guest
- [[Uber]] — the company
- [[Odin]] — the platform he built
- [[Schemaless]] — the datastore Odin started with
- [[Docker]] — containerization used
- [[Kubernetes]] — orchestration emerging at the time
- [[MySQL]] — database technology automated
- [[Cassandra]] — database technology automated
- [[Kafka]] — data-stack technology Odin had to accommodate
- [[Running Code Beats Perfect Code]] — his engineering philosophy
- [[Force Multiplier]] — how he framed influence
- [[Promotion Process]] — his promo-committee experience
- [[Influence Without Authority]] — how he led
- [[Mentorship]] — his mentoring approach
- [[Ryan L. Peterman]] — host
