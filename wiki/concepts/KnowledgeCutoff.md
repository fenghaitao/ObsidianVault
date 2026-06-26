---
title: "KnowledgeCutoff"
type: concept
tags: [llm, training, limitations]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Knowledge cutoff is the date boundary after which an LLM has no training data, making it unaware of events, facts, or developments that occurred after that date. It is a fundamental limitation of pre-trained models that motivates alternative knowledge injection approaches.

## Key Information
- All training data is segmented by date; things after the cutoff are "not known by ChatGPT unilaterally"
- Jack Morris uses the example: ChatGPT doesn't know the Blue Jays didn't win the World Series unless web search is enabled
- Knowledge cutoff is one of several reasons why models fail on niche, proprietary, or recent information
- Combined with fixed model capacity (~3.6 bits per parameter), models must choose what to remember
- Morris argues models waste capacity on irrelevant facts (e.g., capitals of obscure provinces) that could be replaced with domain-specific knowledge
- Motivates the need for weight-based knowledge injection to overcome the cutoff limitation

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[NeuralFileSystem]] — proposed solution
- [[SyntheticContinuedPreTraining]] — technique to inject post-cutoff knowledge
- [[RAG]] — alternative approach to bypass cutoff
