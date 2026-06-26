---
title: "ReferenceFreeEvals"
type: concept
tags: [eval, llm, hallucination, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Reference-free evals are evaluation techniques that compare an LLM's output directly against the source document or input, without requiring a pre-collected set of ideal reference outputs. They are particularly useful as guardrails for detecting hallucinations and can be deployed on all new outputs once built.

## Key Information
- Contrasted with reference-based evals, which compare generated output to an ideal sample (expensive, requires collecting gold-standard examples)
- Example: for summarization, check whether the summary entails or contradicts the source document — this is a reference-free hallucination eval
- Key advantage: once built, a reference-free eval can be applied as a guardrail to all new outputs without needing per-output reference data
- Can be implemented via fine-tuned classifier models or entailment/contradiction checks
- Eugene Yan advocated for investing in reference-free evals specifically because they can double as guardrails
- More broadly, reference-free evals represent a class of techniques that reduce the annotation burden compared to collecting gold-standard reference outputs

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[EugeneYan]] — advocated this technique in the keynote
- [[Guardrails]] — the primary use case for reference-free evals
- [[LLM-as-Judge]] — alternative evaluation approach
- [[EvalEngineering]] — broader practice this technique belongs to
