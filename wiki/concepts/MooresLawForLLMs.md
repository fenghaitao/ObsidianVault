---
title: "MooresLawForLLMs"
type: concept
tags: [economics, cost, trends, llm, strategy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Moore's Law for LLMs describes the observed trend that LLM inference costs drop roughly an order of magnitude every 12-18 months at each capability tier. This trend, which is faster than traditional Moore's Law for semiconductors, enables strategic planning: applications that are uneconomical today become viable within approximately 30 months.

## Key Information
- Presented by Bryan Bischof in the 2024 AI Engineer Summit keynote's strategic section
- Three observed capability tiers: DaVinci (original GPT-3 API), text-davinci-002 (underlying ChatGPT), and GPT-4/Sonnet
- In each case, approximately 15 months was enough time for costs to drop by an entire order of magnitude
- This is faster than Moore's Law for semiconductors (which predicted ~2x every 18-24 months)
- Concrete example: in 2023, it cost ~$625/hour to run a video game where all NPCs were powered by chatbots; after two orders of magnitude reduction (~30 months from mid-2023), it would cost ~$6/hour — a consumer-viable price point comparable to 1980 Pac-Man (inflation-adjusted)
- Strategy: design and prototype for capabilities that will be economical at the time of your next funding round
- Inspired by Alan Kay and Xerox PARC's technique of projecting Moore's Law forward to build expensive prototypes for the future

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[BryanBischof]] — presented this analysis
- [[AlanKay]] — pioneered the technique of projecting capability trends forward
- [[XeroxPARC]] — where the forward-projection technique was developed
- [[ModelIsNotTheMoat]] — companion strategic insight
- [[OpenAI]] — models used as data points for the trend
