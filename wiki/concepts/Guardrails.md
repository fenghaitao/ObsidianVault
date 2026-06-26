---
title: "Guardrails"
type: concept
tags: [safety, production, monitoring, llm, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Guardrails are automated checks deployed in production to catch and prevent defects in LLM outputs. They function as table-stakes quality controls covering toxicity, personally identifiable information (PII), copyright, expected language, and hallucinations, and are essential because the cost to catch and fix defects is orders of magnitude larger than the cost to produce them.

## Key Information
- Presented in the tactical section of the 2024 AI Engineer Summit keynote by Eugene Yan
- Invokes Brandolini's Law: the energy needed to catch and fix defects is an order of magnitude larger than the energy needed to produce them
- Table-stakes guardrails: toxicity detection, PII detection, copyright violation detection, expected language enforcement
- Hallucination guardrails: check whether generated output contains information not present in the source document (entailment vs. contradiction)
- Reference-free evals can be repurposed as guardrails — if you build a hallucination eval that checks entailment against source documents, it can guard all new outputs
- Context matters: even basic checks like expected language can fail in surprising ways (e.g., ads posted in non-English languages on English-language websites)
- Guardrails run either asynchronously or in the critical path, and need ongoing maintenance to stay aligned with evolving quality definitions

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[EugeneYan]] — presented guardrails in the keynote
- [[BrandoliniLaw]] — the asymmetry principle that motivates guardrails
- [[ReferenceFreeEvals]] — technique that can double as guardrails
- [[LLM-as-Judge]] — can serve as a guardrail mechanism
- [[EvalEngineering]] — broader practice guardrails are part of
