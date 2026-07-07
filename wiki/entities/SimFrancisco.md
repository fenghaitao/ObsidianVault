---
title: "SimFrancisco"
type: entity
tags: [project, hackathon, synthetic-population, forecasting, claude-opus]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Sim Francisco is a winning project from [[Anthropic]]'s [[ClaudeOpus4.8]] Build Day hackathon (June 2026) that models San Francisco's population with 10,000 synthetic residents drawn from US Census data, each with their own demographics, personal history, and worldview, placed on a map of the city and reacting to the news in real time. It was built by [[TanmayiPriyaDasari]] and [[TejasPrabhune]].

## Key Information

- **Core capability**: ask the city a question and it polls the entire synthetic electorate, neighborhood by neighborhood.
- **Forecasting accuracy**: using models with an October 2023 knowledge cutoff, it forecast the 2024 presidential vote at 81.3% Democratic (actual 83.8%) and San Francisco's March 2024 Prop A at 70% (actual 70.38%). It tracks prediction markets like [[Kalshi]] and [[Polymarket]] within a couple of points.
- **Architecture**: [[ClaudeOpus4.8]] wrote the entire front and back end. The team used a verifier and an adversarial agent alongside Claude to build a backend that reproduced the city's real demographic distributions.
- **Cost optimization**: the first version made a separate inference call for each of the 10,000 residents. [[Claude]] then ran an evolutionary clustering algorithm it created itself, batching residents into about 300 representative personas. The grouped version held the same accuracy while cutting inference cost by 10 to 100 times.
- **Team**: [[TanmayiPriyaDasari]] and [[TejasPrabhune]], electrical engineering and computer science majors at [[UCBerkeley]] who met through the Machine Learning club. For Tejas, Sim Francisco also serves as a test for his post-training company, exploring whether simulated personas can stay consistent enough to train models on long-horizon tasks.
- **Note**: the project uses forecasting election outcomes as an example only; this does not represent an [[Anthropic]] endorsement of using AI-simulated election predictions as a use case.

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source summary
- [[ClaudeOpus4.8]] — the model used to build Sim Francisco
- [[SyntheticPopulation]] — the concept underlying the project
- [[TanmayiPriyaDasari]] — co-creator
- [[TejasPrabhune]] — co-creator
- [[UCBerkeley]] — university affiliation of the creators
- [[Kalshi]] — prediction market tracked by the model
- [[Polymarket]] — prediction market tracked by the model
- [[Tekton]] — fellow winning hackathon project
- [[CustomUniverse]] — fellow winning hackathon project
