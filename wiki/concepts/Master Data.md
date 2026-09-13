---
title: "Master Data"
type: concept
tags: [data-engineering, impact, leverage]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023).md"]
last_updated: 2026-07-21
---

## Definition

Master Data is a data engineering concept referring to foundational data sets that many other pipelines, teams, and systems depend on. Creating Master Data is a key path to staff-level impact for data engineers because it creates leveraged, multiplicative impact across the organization.

## Key Information

- Zach described this as a heuristic for staff-level data engineering: "If you're not creating Master Data, you're not a staff data engineer"
- A data set that services only one visualization is not staff-level — it needs to be the data set that "everyone else makes other data sets with"
- The data set should be used by 30+ other pipelines to qualify as staff-level impact
- Zach's pricing and availability data sets at Airbnb were Master Data — they powered Smart Pricing (an ML algorithm), were used by many teams, and he cut their size by 90%
- The three ways Master Data creates impact: it helps executives make better strategic decisions, helps data scientists/analysts make better product decisions, or helps ML algorithms make better automated decisions
- Data engineers can also use optimization metrics to sell impact: "this pipeline is now 30% faster" or "this data set is 90% smaller"
- Data engineering has a visibility challenge compared to frontend or product work — it "falls into the shadows" without shiny frontend appeal
- There's an alternative path for data engineers: going end-to-end (logging to data set to visualization to ML model) creates more horizontal, visible impact

## Related

- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023)]] — source summary
- [[Zach Wilson]] — described this concept in detail
- [[Multiplicative Impact]] — the mechanism Master Data creates
- [[Leverage]] — the broader concept
- [[Staff Engineer]] — the level this concept helps achieve
- [[Airbnb]] — where Zach applied this concept
- [[Smart Pricing]] — the ML algorithm that used Zach's Master Data
