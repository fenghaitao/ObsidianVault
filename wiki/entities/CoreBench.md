---
title: "CoreBench"
type: entity
tags: [benchmark, eval, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
CoreBench is a benchmark used to evaluate AI models. It became a notable example of flawed evals when Anthropic discovered that Claude Opus's low score (42%) was due to overly strict answer matching rather than actual incorrect answers — after fixing the eval, Opus scored 95%.

## Key Information
- Claude Opus initially scored 42% on CoreBench
- Anthropic investigated and found the eval was too strict: checking for "96.12" and rejecting "96.124991"
- After fixing the eval's answer matching, Opus's score jumped to 95%
- Demonstrates that evals can be wrong — they can judge things as incorrect when they're just being too strict
- Used as a cautionary tale: always look into eval explanations, check against golden datasets, don't take evals at face value

## Related
- [[Anthropic]] — company that discovered the eval issues
- [[Claude Opus]] — model evaluated
- [[Meta-Evaluation]] — the practice of validating evals
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
