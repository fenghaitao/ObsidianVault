---
title: "ChatGPT Image"
type: entity
tags: [model, image-generation, openai, chatgpt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

## Definition
ChatGPT Image is OpenAI's image generation model, accessible through ChatGPT. It ranks #1 on some aggregate leaderboards (e.g., Design Arena) but never ranks #1 on task-specific leaderboards for individual image editing tasks.

## Key Information
- **Leaderboard rankings**: #1 on Design Arena aggregate leaderboard, but not #1 on any specific task leaderboard (removing objects, changing backgrounds, editing text)
- **Compute cost**: Each image takes 62 seconds to generate; a 26K-battle evaluation takes 20 days of compute
- **Evaluation cost**: $5,000 for 26K evaluations; 556 kWh of energy (equivalent to ~400 marathons)
- **Win rate caveat**: Even as a top model, loses at least 40% of head-to-head battles
- **Efficiency comparison**: An optimized model (like Pruna's) can achieve the same evaluation in 7 hours at $265
- Demonstrates the core thesis that the "top model" on a leaderboard isn't necessarily the best choice when efficiency and task specificity are considered

## Related
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source
- [[OpenAI]] — parent company
- [[ChatGPT]] — product through which ChatGPT Image is accessed
- [[Public Leaderboards]] — context for rankings
- [[Model Efficiency]] — key consideration when comparing
- [[Pareto Frontier]] — methodology showing multiple SOTA models exist
