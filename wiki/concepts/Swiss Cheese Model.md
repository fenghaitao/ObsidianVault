---
title: "Swiss Cheese Model"
type: concept
tags: [eval, safety, defense-in-depth, layered-security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
The Swiss Cheese Model is a safety engineering concept (borrowed from Anthropic's blog) applied to AI agent evaluation. Each layer of defense — code evals, LLM judges, human review — has holes (imperfections), but when layered together, the holes don't align, and failures are caught before reaching users.

## Key Information
- Originated in safety engineering; adapted by Anthropic for AI evaluation
- Core insight: no single eval method is perfect — all have flaws and gaps
- The layers: code evals catch basic stuff first (format, forbidden phrases, required fields), LLM judges catch reasoning gaps and semantic issues but miss subtle hallucinations, human review catches what got through the first two layers but can't scale
- When layered, the holes in each "slice" don't line up — failures that slip through one layer get caught by the next
- No single eval method captures everything — using all three types simultaneously is the defense
- The model reinforces that evals are complementary, not competing approaches
- Practical implication: start with code evals (fast, cheap), add LLM judges (semantic), keep humans in the loop (edge cases)

## Related
- [[Code Evals]] — first layer of defense
- [[LLMAsJudge]] — second layer of defense
- [[MetaEvaluation]] — human review layer
- [[Cascading Failures]] — the problem the model prevents
- [[Anthropic]] — originator of the adaptation for AI
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
