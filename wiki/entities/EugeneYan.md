---
title: "EugeneYan"
type: entity
tags: [person, ai, evals, llm, engineer]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240719 - Lessons From A Year Building With LLMs.md"]
last_updated: 2026-06-26
---
## Definition
Eugene Yan is an AI practitioner and co-author of the O'Reilly white paper "What We Learned from a Year of Building with LLMs." He presented the tactical considerations section of the keynote at the AI Engineer Summit, focusing on LLM-as-judge, fine-tuned evaluators, and guardrails.

## Key Information
- Co-authored the O'Reilly white paper on LLM application building lessons alongside five other practitioners
- Presented the tactical track of the keynote alongside Shreya Shankar
- Strongly bullish on LLM-as-judge for quick prototyping of evals with minimal development effort
- Acknowledged LLM-as-judge limitations: difficult to align to specific business criteria, requires chain-of-thought (5-8 seconds latency), and needs ongoing maintenance of few-shot examples
- Advocated for fine-tuned evaluator models (classifiers, reward models) for production use due to 100x lower latency (milliseconds vs seconds) and higher precision
- Recommended reference-free evals (comparing output to source document for entailment/contradiction) that can double as hallucination guardrails
- Emphasized guardrails as table stakes: toxicity, PII, copyright, expected language detection

## Related
- [[summary-20240719 - Lessons From A Year Building With LLMs]] — source
- [[ShreyaShankar]] — co-author and co-presenter
- [[LLM-as-Judge]] — evaluation technique he analyzed in depth
- [[Guardrails]] — topic he presented on
- [[ReferenceFreeEvals]] — technique he advocated for hallucination detection
