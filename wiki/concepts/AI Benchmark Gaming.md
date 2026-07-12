---
title: "AI Benchmark Gaming"
type: concept
tags: [AI, evaluation, benchmarks, incentives]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md"]
last_updated: 2026-07-10
---

## Definition

AI benchmark gaming is the practice of optimizing AI models to score well on standardized benchmarks — often at the expense of real-world performance. Edwin Chen is highly critical of this practice, arguing it steers AI development in the wrong direction.

## Key Information

- Edwin doesn't trust benchmarks at all, for two reasons: (1) benchmarks themselves often have wrong answers and are full of messiness, and (2) benchmarks have well-defined objective answers that make them easy for models to hill-climb on, unlike the messiness and ambiguity of the real world
- "It's kind of crazy that these models can win IMO gold medals but they still have trouble parsing PDFs"
- Frontier labs game benchmarks by: tweaking system prompts, adjusting the number of times they run the model, and intentionally optimizing training data for benchmark performance
- LM Arena is a prime example: the easiest way to climb it is to add crazy bolding, double emojis, and triple response length — even if the model hallucinates
- Researchers at AI labs are trapped: they must climb leaderboards for promotion even when they know it degrades model quality
- Enterprise customers use leaderboard rankings to decide which model to buy, forcing labs to prioritize benchmarks
- "The models with the best scores are often the worst or just have all these fundamental failures"
- Benchmark optimization is essentially a marketing exercise — "cool, number one at all these benchmarks" — rather than genuine progress

## Related

- [[LM Arena]] — the most criticized benchmark
- [[Objective Functions in AI]] — the root cause of benchmark gaming
- [[Human Evaluation of AI]] — the better alternative to benchmarks
- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
