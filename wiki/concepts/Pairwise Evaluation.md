---
title: "Pairwise Evaluation"
type: concept
tags: [eval, llm-as-judge, comparison, ab-testing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Pairwise evaluation is an LLM-as-judge technique where the judge compares two outputs side-by-side and determines which is better, rather than assigning an absolute score to a single output. It is significantly more reliable than asking an LLM to rate outputs on a numeric scale (1-10).

## Key Information
- LLMs are bad at absolute ratings (what's the difference between a 6 and a 7?) but good at relative comparisons
- Present two outputs and ask the judge: "Which one is better?" — the LLM has two concrete examples to work with
- Much more reliable than asking for a score from 1 to 10, which introduces noise and requires defining what each number means
- Especially useful for A/B testing prompt versions or model upgrades
- Can be used to compare: different prompt versions, different model outputs, different agent configurations
- Part of the advanced techniques Laurie Voss mentioned at the end of his workshop — "what to Google to go even further"

## Related
- [[LLM-as-Judge]] — the underlying evaluation technique
- [[Meta-Evaluation]] — validating the pairwise judge's decisions
- [[Reliability Scoring]] — complementary advanced technique
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
