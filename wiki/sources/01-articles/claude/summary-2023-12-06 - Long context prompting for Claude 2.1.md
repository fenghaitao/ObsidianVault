---
title: "summary-2023-12-06 - Long context prompting for Claude 2.1"
type: source
tags: [source, original-material, long-context, prompting, claude-2.1]
sources: ["raw/01-articles/claude/2023-12-06 - Long context prompting for Claude 2.1.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic describes an evaluation showing [[Claude2.1]]'s 200K-token context window is powerful but requires careful prompting: when a single sentence is embedded "out of place" in a long document (e.g., a fact unrelated to the surrounding essay), Claude 2.1 is often reluctant to answer, incorrectly claiming the document lacks enough information — likely a side effect of training aimed at reducing unsupported claims. Anthropic found that appending the sentence "Here is the most relevant sentence in the context:" to the start of Claude's response overrides this reluctance, raising accuracy on the out-of-place-sentence retrieval task from 27% to 98%, and also improving accuracy (90-95%) on in-context (not out-of-place) single-sentence retrieval.

## Key Points

- [[Claude2.1]] offers a 200K token context window (~500 pages) and was trained on real long-document tasks (e.g., summarizing S-1 filings) to reduce mistakes and unsupported claims.
- Claude 2.1 shows a **30% reduction in incorrect answers** versus Claude 2.0, and a **3-4x lower rate** of falsely claiming a document supports a claim it does not.
- **Reluctance phenomenon**: when an embedded sentence seems "out of place" relative to the rest of a long document, Claude 2.1 often responds that the document doesn't provide a definitive answer, even though the sentence is present and relevant — replicated with Paul Graham essays and a Consolidated Appropriations Act test.
- Claude does **not** show the same reluctance for sentences that are contextually "in place" within the document (tested via a randomized-position Viaweb/Yahoo acquisition example).
- **Fix**: prompting Claude to begin its response with "Here is the most relevant sentence in the context:" improved accuracy on the out-of-place sentence retrieval evaluation from 27% to 98%, and to 90-95% on the in-place retrieval case.
- This establishes an early [[LongContextRetrieval]] prompting technique: directing the model to locate relevant material first overrides its tendency to under-claim on long-context tasks.

## Related

- [[Claude2.1]] — the model subject of this evaluation
- [[LongContextRetrieval]] — the retrieval-prompting pattern this article documents
- [[PromptEngineering]] — the discipline this prompting technique belongs to
