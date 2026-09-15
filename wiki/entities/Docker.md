---
title: "Docker"
type: entity
tags: [tool, containerization, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md"]
last_updated: 2026-09-14
---

## Definition

Docker is a containerization platform. Joakim Recht used it at Uber to run databases in containers and thereby improve utilization and management, an approach that was "very uncommon back then."

## Key Information

- Around the time of Odin's origin, containerization was still fairly new and Docker was "not super new" but not yet ubiquitous
- Running databases in Docker allowed running multiple databases on one host (instead of dedicating whole hosts), a big utilization win for sharded MySQL
- Allowed running different MySQL versions more easily on the same infrastructure

### Docker in Kubernetes' Origin
- At the time Kubernetes was conceived, "you had to explain Docker to people" — the original demo showed a container image built with Docker, deployed across machines and load-balanced.
- Burns describes Docker as "a startup" that could be "way more agile than a big company," which is partly why the Kubernetes team wanted the agility of a separate brand/entity.

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Brendan Burns]] — used Docker for the Kubernetes demo
- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Uber]] — company where Docker was adopted for databases
- [[Odin]] — platform built on containerization
- [[Kubernetes]] — orchestration that appeared around the same time
- [[Schemaless]] — workload containerized first
