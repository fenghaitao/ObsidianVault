---
title: "Kafka"
type: entity
tags: [tool, infrastructure, messaging, Uber]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht.md"]
last_updated: 2026-09-14
---

## Definition

Kafka is a distributed streaming/messaging platform. At Uber it was part of the data stack, and was one of the technologies that was "notoriously bad" to run dynamically, posing a challenge for Odin.

## Key Information

- Kafka belonged to Uber's data stack (alongside HDFS and Pinot), managed in a separate org from the online databases
- Kafka was historically "notoriously bad at moving stuff around dynamically" — hostnames and partition numbers are encoded everywhere and data must be shuffled
- Making technologies like Kafka and HDFS work under Odin (which were "inherently not cloud/container ready") was a major, lengthy challenge

## Related

- [[summary-20251111 - Uber Distinguished Eng： Unfair Promos, Influence, Engineering Regrets ｜ Joakim Recht]] — source summary
- [[Uber]] — company context
- [[Odin]] — platform that had to accommodate Kafka
