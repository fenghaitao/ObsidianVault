---
title: "CartaHealthcare"
type: entity
tags: [enterprise, healthcare, clinical-data, ai-adopter, registry, ai-agents]
sources: [raw/01-articles/claude/2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor.md]
last_updated: 2026-07-04
---

## Definition

Carta Healthcare is a clinical data management company that builds software to automate clinical data abstraction — the process of turning patient charts and physician notes into standardized, registry-ready data for outcomes benchmarking and quality improvement. Its flagship platform, Lighthouse, uses Claude to reason across clinical documentation the way a trained human abstractor would, rather than relying on rules-based extraction or pattern-matching NLP.

## Key Information

- **Product**: Lighthouse, a clinical data abstraction platform that reads physician notes, imaging studies, and structured/free-text documentation to answer registry questions requiring temporal logic (e.g., pre- vs. post-procedure lab values) and judgment calls where documentation conflicts.
- **Evolution**: started years ago with NLP-based pattern recognition for extraction; migrated to LLMs (evaluating several before selecting [[Claude]]) because pattern recognition couldn't replicate clinical judgment.
- **Why Claude**: per Hannah Glaser, Applied AI Applications Manager, "No other model we evaluated showed the same capability for understanding and interpreting clinical documentation."
- **Engineering approach**: prioritized [[ContextEngineering]] over prompt tuning — injecting patient-specific runtime context (exact procedure start times, source-document scoping) so Claude reasons from complete, correctly time-bounded information rather than guessing.
- **Feedback loop**: clinical abstractors' explanations of edge cases and documentation patterns are converted directly into revised prompts and shipped the same day, compressing what used to take months of engineering/QA per registry into about a week.
- **Scale/results**: at one large health system, Lighthouse processes 22,000+ surgical cases annually across 14 hospitals, reaching 98-99% inter-rater reliability (the industry-standard accuracy measure for abstraction).
- **Trust design**: Lighthouse is not a black box — for every extracted data point, abstractors see supporting evidence and Claude's rationale, letting them validate rather than blindly accept outputs. Key people quoted: Hannah Glaser (Applied AI Applications Manager) and Matthew Mazzanti (Software Engineering Manager).

## Related

- [[summary-2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor]] — source summary
- [[Claude]] — model powering Lighthouse's clinical reasoning
- [[Anthropic]] — publisher of this case study
- [[ContextEngineering]] — the core engineering practice this case study demonstrates
- [[HealthcareAI]] — broader concept category Carta Healthcare exemplifies
