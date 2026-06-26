---
title: "DocumentBoundaryDetection"
type: concept
tags: [document-processing, llm, classification, dspy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners.md"]
last_updated: 2026-06-26
---

## Definition
Document Boundary Detection is a technique for identifying logical section boundaries within documents (e.g., main body vs. schedules/exhibits) using LLM-based page classification and structural analysis, implemented with DSPy.

## Key Information
- Kevin Madura demonstrated boundary detection on a 13-page contract with schedules and exhibits.
- The process: convert PDF pages to images, classify each page asynchronously, then pass classifications to a DSPy signature that outputs section boundaries as string-to-integer-tuple mappings.
- The technique uses ReAct with tool calling to let the model self-reflect: it can request page images to verify boundary correctness.
- Results showed accurate detection: main document (pages 0-6), Schedule 1 (pages 7-8), Schedule 2 (page 9), Schedule 3 (pages 10-13).
- The approach requires minimal specification — just a signature and brief instructions — yet produces reliable results.
- Combined with recursive summarization for comprehensive document processing pipelines.

## Related
- [[DSPy]] — framework used for implementation
- [[RecursiveSummarization]] — complementary technique
- [[ReAct]] — pattern used for self-reflection during detection
- [[summary-20260108 - DSPy： The End of Prompt Engineering - Kevin Madura, AlixPartners]] — source
