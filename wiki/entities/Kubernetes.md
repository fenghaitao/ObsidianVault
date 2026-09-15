---
title: "Kubernetes"
type: entity
tags: [tool, orchestration, infrastructure, containers]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md"]
last_updated: 2026-09-14
---

## Definition

Kubernetes is a container orchestration system. At the time Joakim Recht began containerizing Uber's databases, Kubernetes had "just got released" in its first alpha version.

## Key Information

- Kubernetes was released in its first alpha "just around" the time Uber began running databases in containers
- Odin's framing (declarative "goal state/intent," letting a system reconcile) aligns with the pattern Kubernetes popularized, which was "very uncommon back then"

### Brendan Burns's Origin Story
- Kubernetes began at Google as a week-long demo by Burns, [[Joe Beda]], and [[Craig McLuckie]], assembled from existing open-source pieces; Burns wrote a high-80s% share of the original code.
- The pitch to leadership drew on MapReduce (Google got no credit for Hadoop), the need for orchestration "autopilots" as software becomes business-critical, and the fact that open ecosystems win (the Linux analogy): "there's going to be an open source one — do you want it to be ours or someone else's?"
- Independence was central: Kubernetes was donated to the [[Cloud Native Computing Foundation]] under the [[Linux Foundation]] about a year in, and democratic governance rules were written in 2016 to stop any single company controlling it.
- Architecture: declarative configuration, loosely coupled control loops driving desired↔current state (inspired by control theory), and all persistence forced through the [[etcd]]-backed API server for statelessness — stable but hard to debug.
- Scale: everything is horizontally scalable except the storage layer (etcd); "every time you change an order of magnitude, the problem moves."

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Brendan Burns]] — co-creator
- [[Google]] — where Kubernetes was created
- [[Borg]] — Google's internal predecessor
- [[etcd]] — consensus storage layer
- [[Declarative Configuration]] — the configuration model
- [[Thought Leadership]] — the strategy behind open-sourcing it
- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Docker]] — the container technology Kubernetes orchestrates
- [[Odin]] — Uber platform with a similar declarative-ops pattern
- [[Uber]] — company context
