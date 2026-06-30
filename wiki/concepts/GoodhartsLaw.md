---
title: "GoodhartsLaw"
type: concept
tags: [measurement, metrics, management, productivity]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Definition
Goodhart's Law states: "When a measure becomes a target, it ceases to be a good measure." In the context of AI and software engineering, it describes how token usage metrics and AI adoption targets get gamed by engineers, rendering the measurements useless.

## Key Information
- Referenced by swyx during discussion of token maxing: "whatever gets measured gets sort of abused"
- Classic examples in software: lines of code, number of PRs — both known to be stupid metrics that people optimize for
- New manifestation: token counts and AI spend as productivity proxies
- Companies that measure token output see engineers artificially inflating usage
- The dynamic: leadership wants to measure AI adoption → creates leaderboards/targets → engineers game the system → measurement becomes meaningless
- Historical parallel: early developer productivity tools like Velocity and Pluralsight Flow measured lines of code and PR counts, with the same gaming behavior
- Brian Scanlan acknowledged Goodhart's Law when choosing "code changes per R&D person" as Intercom's primary metric for the 2x project: "Every measure is bad. Once you start measuring it, it's not a measure"

## Related
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source (acknowledged by Intercom)
- [[TokenMaxing]] — current manifestation
- [[DeveloperProductivityMeasurement]] — broader context
- [[Doubling Engineering Throughput]] — Intercom's project aware of this limitation
- [[Intercom]] — company that acknowledged Goodhart's Law in their metric choice
