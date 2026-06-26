---
title: "EARS"
type: concept
tags: [requirements, specification, structured-natural-language, verification]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
EARS (Easy Approach to Requirement Syntax) is a structured natural language format for writing software requirements. It uses a "when X then Y shall Z" syntax that enables deterministic parsing by non-LLM systems, forming the foundation for property-based testing and automated reasoning in spec-driven development.

## Key Information
- Format uses "when... then... shall..." syntax to create structured, machine-parseable requirements
- Enables translation of requirements directly into system properties (invariants) for property-based testing
- Critical to Amazon Kiro's neurosymbolic reasoning strategy: structured natural language allows non-LLM systems to parse and reason about requirements
- Part of Kiro's strategy to use LLMs less over time for quality-critical operations
- Initially seemed like just an interesting design choice, but became foundational when property-based testing was rolled out
- User story format in Kiro: "As a dev I want to X so that Y" combined with EARS acceptance criteria

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[PropertyBasedTesting]] — testing approach enabled by EARS
- [[NeurosymbolicReasoning]] — broader strategy EARS supports
- [[SpecificationDrivenDevelopment]] — the paradigm EARS serves
- [[AmazonKiro]] — IDE that implements EARS
