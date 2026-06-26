---
title: "DeveloperProductivityMeasurement"
type: concept
tags: [measurement, productivity, engineering-management, metrics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md"]
last_updated: 2026-06-26
---

## Definition
Developer productivity measurement refers to the practice of quantifying engineering output through metrics. Historically plagued by poor proxies (lines of code, PR counts), the AI era has introduced new metrics like token usage and AI spend, which suffer from the same Goodhart's Law problems.

## Key Information
- Historical bad metrics: lines of code, number of PRs — both gamed by engineers
- Early tools like Velocity and Pluralsight Flow measured these metrics
- AI era introduces new metrics: token output, AI tool spend, leaderboards
- Meta uses token count as one data point in performance evaluations
- Salesforce has minimum AI spend targets (~$175/month)
- The pattern: leadership wants to measure → creates targets → engineers game the system → measurement becomes meaningless
- The meter study (30 people): participants felt 20% more productive but were actually 20% less productive — demonstrating the gap between perceived and actual productivity
- Simon Willison: after 2 years of using AI, still figuring out what works — there's no manual for AI productivity

## Related
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source
- [[TokenMaxing]] — current manifestation of metric gaming
- [[GoodhartsLaw]] — underlying principle
- [[Meta]] — company using token metrics
- [[Salesforce]] — company with spend targets
