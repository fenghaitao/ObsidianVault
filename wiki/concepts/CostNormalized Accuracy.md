---
title: "Cost-Normalized Accuracy"
type: concept
tags: [eval, cost, optimization, trade-off, accuracy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Cost-normalized accuracy is a metric that divides accuracy by cost to evaluate whether a more expensive AI model or configuration is worth the price. It formalizes the trade-off: an agent that is 92% accurate at 2 cents per query may provide better value than one that is 95% accurate at 15 cents per query.

## Key Information
- Formula: accuracy ÷ cost — higher is better value
- Enables data-driven decisions about model selection and tiered routing
- Example application: simple queries ("what are your hours?") routed to cheap models; complex queries ("analyze comparative PE ratios of five semiconductor companies") routed to expensive models
- Evals provide the accuracy data; model pricing provides the cost data
- Part of the impact hierarchy: model selection (level 3) decisions should be informed by cost-normalized accuracy
- Google phrase: "cost-normalized accuracy" — a concrete framework for making accuracy/cost trade-offs
- Mentioned as an advanced technique by Laurie Voss: "what to Google to go even further"

## Related
- [[Impact Hierarchy]] — model selection level informed by this metric
- [[Reliability Scoring]] — complementary metric for consistency
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
