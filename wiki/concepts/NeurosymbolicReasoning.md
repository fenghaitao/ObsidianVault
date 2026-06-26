---
title: "NeurosymbolicReasoning"
type: concept
tags: [ai, reasoning, llm, symbolic, verification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Neurosymbolic reasoning combines neural approaches (LLMs) with symbolic approaches (classic automated reasoning techniques) to achieve more reliable and deterministic results than LLMs alone. Amazon Kiro uses this strategy for quality-critical operations like requirements verification and property-based testing.

## Key Information
- Kiro's backend may use non-LLM systems alongside LLMs depending on the task type
- Goal: use LLMs less over time for quality-critical operations, relying more on classic automated reasoning
- EARS structured natural language is key: it enables deterministic parsing by non-LLM systems
- Examples in Kiro: requirements verification (scanning for ambiguity, conflicting constraints), property-based testing, formalizing requirements into correctness properties
- Distinction: when chatting with Kiro, you talk to an LLM; when executing structured operations, you may be talking to an amalgam of systems
- Represents a shift from "just an LLM with a workflow on top" to a hybrid architecture

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[EARS]] — structured format enabling symbolic reasoning
- [[PropertyBasedTesting]] — testing approach using symbolic methods
- [[SpecificationDrivenDevelopment]] — the paradigm
- [[AmazonKiro]] — IDE implementing this strategy
