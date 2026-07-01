---
title: "BullshitBench"
type: concept
tags: [benchmark, model-evaluation, nonsense-detection, bullshit, pushback]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-29
---

## Definition
BullshitBench is a benchmark created by Peter Gostev (Arena.ai) that tests whether AI models push back against nonsense questions or compliantly attempt to answer them. It consists of 155 deliberately nonsensical questions, with responses graded by LLM-as-judge (validated by human review).

## Key Information
- **Creator**: Peter Gostev, Arena.ai
- **Size**: 155 nonsense questions
- **Grading**: LLM-as-judge, validated by human review of responses
- **Scoring**: Green (clear pushback), Amber (partial acceptance), Red (full compliance with nonsense)
- **Top performers**: Claude/Sonnet models (especially Claude 4.5, Sonnet 4.5), Qwen models, latest Grok
- **Middle performers**: GPT models, Gemini models (~50/50 pushback vs compliance)
- **Worst performers**: Smaller models — "you can ask anything, they just respond"
- **Open source**: Publicly available
- **Key finding about reasoning**: Thinking/reasoning often makes bullshit detection worse — models question the premise then spend paragraphs trying to solve anyway
- **Key finding about model size**: No clear correlation between parameter count and bullshit detection ability
- **Key finding about trends**: Only Anthropic shows clear improvement over time; OpenAI and Google are up-and-down with no clear trend

## Why It Matters
- Exposes a capability gap not captured by standard benchmarks: the ability to recognize and reject ill-posed questions
- Reveals that models are overtrained to "solve at any cost" rather than exercise judgment
- Has practical implications for agent reliability — agents that can't push back will execute nonsense tasks
- Resonated widely because it "spoke to a slight unease people had with different models"

## Related
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source
- [[Peter Gostev]] — creator
- [[ArenaAi]] — platform where creator works
- [[Nonsense Detection]] — the capability being measured
- [[Reasoning Limits]] — finding that reasoning worsens performance
- [[LLMAsJudge]] — grading methodology
- [[Model Dissatisfaction Rate]] — complementary Arena metric
- [[ModelBehavior]] — solve-at-any-cost training critique
- [[Anthropic]] — best performer
- [[OpenAI]] — middle performer
- [[GoogleDeepMind]] — middle performer
- [[Qwen]] — decent performer
