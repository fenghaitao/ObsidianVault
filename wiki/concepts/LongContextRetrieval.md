---
title: "LongContextRetrieval"
type: concept
tags: [long-context, retrieval, prompting, evaluation]
sources: ["raw/01-articles/claude/2023-12-06 - Long context prompting for Claude 2.1.md"]
last_updated: 2026-07-04
---

## Definition

Long context retrieval is the pattern of effectively locating and using a specific, relevant piece of information embedded within a very large document or context window (100K+ tokens), as distinct from simply having a large context window available.

## Key Information

- A large [[ContextWindow]] does not guarantee accurate retrieval: models can be reluctant to answer when a relevant fact seems "out of place" relative to its surrounding context, instead falsely claiming the document lacks sufficient information.
- Demonstrated on [[Claude2.1]] using a needle-in-haystack style evaluation: a single out-of-place sentence embedded in a long document (Paul Graham essays; a Consolidated Appropriations Act bill) was often missed or denied, while sentences that were contextually "in place" were retrieved reliably regardless of position.
- **Mitigation technique**: prepending the instruction "Here is the most relevant sentence in the context:" to the start of the model's response overrides the reluctance, raising retrieval accuracy from 27% to 98% on the out-of-place case, and to 90-95% on the in-place case.
- This shows that retrieval reluctance is a prompting problem as much as a capability problem — directing the model to search for relevant content first changes the outcome substantially.

## Related

- [[Claude2.1]] — model on which this behavior and fix were evaluated
- [[ContextWindow]] — the underlying capacity that makes long-context retrieval possible
- [[PromptEngineering]] — the broader discipline this technique belongs to
- [[summary-2023-12-06 - Long context prompting for Claude 2.1]] — source article documenting the evaluation and fix
