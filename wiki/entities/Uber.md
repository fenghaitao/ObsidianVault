---
title: "Uber"
type: entity
tags: [company, tech, ride-hailing, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20251121 - Atoms CTO： Intelligence, Regrets, Travis Kalanick Stories ｜ Brian Attwell.md"]
last_updated: 2026-09-14
---

## Definition

Uber is a ride-hailing and technology company. In these episodes it is discussed as an engineering organization that grew extremely fast, as the birthplace of the Odin infrastructure platform (Joakim Recht), and as the company where Brian Attwell reached Senior Staff in under four years.

## Key Information

- Early Uber gave engineers a lot of freedom: at one point ~52 database technologies were in use, each team building its own toolchain
- The stateful side of Uber was split into online databases (MySQL, Postgres, Cassandra) and the data stack (HDFS, Kafka, Pinot), managed through separate orgs with the management chain going "through the CEO and back down"
- Uber did not have a full software-defined network at the time, so hosts/ports couldn't be moved logically — a pain point for storage technologies
- Joakim Recht's Odin platform eventually operated all of Uber's stateful workloads: ~120,000 physical servers and ~half a million databases run by ~20 people
- Recht's Denmark office (small, ~70 people) had outsized influence, growing two Distinguished Engineers internally
- Early Uber promo committees for platform engineering put all managers/VPs/senior engineers and senior ICs in a room for a day to discuss hundreds of engineers with no prep or materials
- Early Uber culture was very individual/negotiation-centric ("it's all about you, not the team"); the company went through a 2017-era wave of scandals and turnover (board members and Travis Kalanick departing)
- A tracing mandate ("all teams must implement tracing" for thousands of microservices) was emailed repeatedly from ~2015 into 2017-2018 but never completed — an inability to affect global change
- A software-defined networking stack was implemented in Node around 2016 and caused "many years of untangling" — a decision Recht now sees as a mistake
- Early Uber was a JavaScript/Python shop that then became a Go shop when "nobody knew Go"

### Brian Attwell's Uber Tenure
- Attwell described early Uber as "a fantastic engineering firm": good people to learn from, very meritocratic, and growing fast (so there were lots of good problems to solve)
- His mobile-maintainability team fixed maintainability issues as the company hyper-scaled; over a few quarters he and Yi Wang became top-three committers across the ~400-person mobile organization
- Attwell reached Senior Staff at Uber in under 4 years, working ~90–100 hours/week

## Related

- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[summary-20251121 - Atoms CTO： Intelligence, Regrets, Travis Kalanick Stories ｜ Brian Attwell]] — source summary
- [[Joakim Recht]] — Distinguished Engineer at Uber
- [[Odin]] — stateful-workload platform
- [[Schemaless]] — datastore built at Uber
- [[Docker]] — containerization used by Odin
- [[Kubernetes]] — container orchestration emerging at the time
- [[Cassandra]] — database technology used at Uber
- [[Brian Attwell]] — reached Senior Staff at Uber
- [[Travis Kalanick]] — Uber's co-founder and former CEO
- [[Promotion Process]] — Uber's promo committees
