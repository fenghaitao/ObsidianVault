---
title: "SpecificationDrivenDevelopment"
type: concept
tags: [concept, development-paradigm, specification, verification, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Specification-driven development is a paradigm shift from traditional coding where developers specify constraints and validation criteria, then let AI agents generate and verify solutions against those specifications.

## Key Information
- Contrasts with traditional development: understand problem → design solution → code → test
- New flow with agents: specify constraints → generate solutions → verify (automated + human intuition) → iterate
- Emerging across multiple tools: Factory Droid has specification mode and plan mode; other IDEs are orienting around specification-driven flows
- The developer's role shifts from writing code to curating the validation environment and setting constraints
- Combines with automated validation to produce reliable, high-quality solutions
- Enables decomposing large-scale projects into parallel subtasks handled by multiple agents
- One opinionated engineer can scale their impact across the entire organization through codified specifications
- **Amazon Kiro implementation**: Compresses the full SDLC into a tight inner loop: requirements (EARS format) → design → property extraction → task list → execution
- Kiro uses structured natural language (EARS) to enable deterministic parsing by non-LLM systems for property-based testing and automated reasoning
- Specs in Kiro are living documentation: they are mutated over time rather than created as one-off plans, producing reviewable diffs
- At Amazon, internal teams have replaced design doc reviews with spec reviews using Kiro-generated specs
- Kiro's approach is not just "an LLM with a workflow on top" — it uses neurosymbolic reasoning (LLMs + classic automated reasoning)

## Related
- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — source transcript
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source transcript
- [[AgentReadyCodebases]] — the codebase state that enables this
- [[AutomatedValidation]] — the verification component
- [[Software2.0]] — precursor concept by Andrej Karpathy
- [[FactoryAI]] — company with Droid agent supporting this flow
- [[AmazonKiro]] — Amazon's agentic IDE implementing this paradigm
- [[EARS]] — structured requirement format used in Kiro
- [[PropertyBasedTesting]] — verification approach integrated into Kiro
- [[NeurosymbolicReasoning]] — backend strategy in Kiro
- [[SpecAsLivingDocumentation]] — Kiro's approach to evolving specs
