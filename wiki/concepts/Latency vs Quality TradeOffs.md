---
title: "Latency vs Quality Trade-offs"
type: concept
tags: [consumer-ai, latency, quality, llm, production]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
The engineering challenge in consumer-facing AI applications of balancing response speed against output quality, where different user experiences justify different trade-off points.

## Key Information
- Play Magnus targets sub-3 second end-to-end latency for game review commentary because users want to cycle through moves quickly after finishing a game
- "You really couldn't show you like a coach is thinking screen you know indefinitely while reasoning tokens are kind of running in the background"
- Gemini 3 Flash achieves ~1 second time-to-first-token and ~3 seconds total, meeting the latency target at ~75% accuracy
- Reasoning models produce higher quality but have unpredictable completion times — the latency is not just longer but variable
- Future "chat with your coach" features can tolerate longer latency because users expect a more conversational, patient interaction
- The trade-off is not just model selection but feature design: instant game review vs. chat-with-coach are different products with different latency budgets
- Anant Dole emphasized this as a key learning for consumer AI: "you had to really kind of consider this trade-off between latency versus quality"

## Related
- [[Gemini 3 Flash]] — chosen for latency over quality
- [[Play Magnus]] — consumer app facing this trade-off
- [[Separating Data Pipeline from Language Generation]] — architectural pattern that reduces latency by offloading computation from LLM
- [[LLM Hallucination In Chess]] — quality concern that the pipeline must address
- [[Anant Dole]] — presented this section
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
