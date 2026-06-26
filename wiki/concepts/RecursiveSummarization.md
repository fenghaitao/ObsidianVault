---
title: "RecursiveSummarization"
type: concept
tags: [summarization, llm, document-processing, dspy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
Recursive Summarization is a technique for summarizing documents longer than an LLM's context window by iteratively processing chunks and combining summaries, demonstrated using DSPy signatures for contract analysis.

## Key Information
- Kevin Madura demonstrated recursive summarization using three separate DSPy signatures to decompose and summarize contract contents.
- The process works by iterating through document chunks, creating intermediate summaries, and combining them into a final summary.
- DSPy's module system makes it straightforward to chain multiple signatures for this multi-step process.
- Combined with document boundary detection to identify logical sections before summarization.
- The approach is described as "poor man's RAG" — it feeds document content directly rather than using vector stores or embeddings.

## Related
- [[DSPy]] — framework used for implementation
- [[DocumentBoundaryDetection]] — complementary technique
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
