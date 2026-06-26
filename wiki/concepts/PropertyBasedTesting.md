---
title: "PropertyBasedTesting"
type: concept
tags: [testing, verification, quality, invariants]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Property-based testing (PBT) is a testing approach that defines system invariants (properties) and attempts to find counterexamples that falsify them. If no counterexample is found, there is high confidence the system meets its requirements. It is integrated into Amazon Kiro's spec-driven development workflow.

## Key Information
- Attempts to produce a single test case that falsifies an invariant (property) of the system
- If any counterexample is found, the requirement is not met
- If no counterexample is found, there is high confidence the system does what it says — though "high" depends on how well tests are written
- In Kiro, EARS requirements are translated directly into system properties for PBT
- Popular PBT libraries: Hypothesis (Python), FastCheck (Node.js), Clojure's spec library
- Kiro's GA launch (November 2025) included PBT as the first step in tying structured requirements through to finished code
- Part of Kiro's strategy to use non-LLM (deterministic) systems for quality assurance
- Kiro formalizes requirements into correctness properties during the design phase

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[EARS]] — requirement format that feeds into PBT
- [[NeurosymbolicReasoning]] — broader strategy PBT is part of
- [[SpecificationDrivenDevelopment]] — the paradigm
- [[AmazonKiro]] — IDE that integrates PBT
- [[Verification in Agentic Loops]] — related verification concept
