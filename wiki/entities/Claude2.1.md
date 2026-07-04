---
title: "Claude 2.1"
type: entity
tags: [claude, model, anthropic, llm, foundation-model, long-context]
sources: ["raw/01-articles/claude/2023-12-06 - Long context prompting for Claude 2.1.md"]
last_updated: 2026-07-04
---

## Definition

Claude 2.1 is Anthropic's enhanced successor to [[Claude2|Claude 2]], offering a 200K-token context window (roughly 500 pages) and trained specifically to improve real-world long-document retrieval and reduce hallucinated claims.

## Key Information

- **Context window**: 200K tokens.
- Trained on large amounts of feedback on long-document tasks users find valuable, such as summarizing S-1-length filings, using real tasks on real documents.
- **30% reduction in incorrect answers** compared with Claude 2.0.
- **3-4x lower rate** of mistakenly stating that a document supports a claim when it does not.
- Excels at real-world retrieval tasks across long contexts, though it can be reluctant to answer when a relevant sentence appears "out of place" relative to surrounding context — see [[LongContextRetrieval]] for the prompting technique that mitigates this.

## Related

- [[Claude2]] — predecessor model
- [[Anthropic]] — creator of Claude 2.1
- [[LongContextRetrieval]] — retrieval behavior and prompting pattern documented for this model
- [[ContextWindow]] — the 200K-token working-memory capacity
- [[PromptEngineering]] — prompting techniques used to improve retrieval accuracy
- [[summary-2023-12-06 - Long context prompting for Claude 2.1]] — source article
