---
title: "summary-2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor.md"]
last_updated: 2026-07-04
---

## Core Summary

Carta Healthcare built Lighthouse, a clinical data abstraction platform that uses Claude to answer registry questions the way a trained human abstractor would — reasoning across conflicting clinical documentation, applying temporal logic (e.g., distinguishing a pre- vs. post-procedure lab value), and handling ambiguity that rules-based NLP systems could never resolve. After evaluating several models, Carta Healthcare chose Claude for its superior interpretation of clinical documentation. The team found that model capability alone wasn't the bottleneck: the hard engineering problem was context engineering — assembling the right source documents, time windows, and priority order at runtime so Claude has precise, complete information to reason over. With context construction solid, clinical abstractors' feedback on edge cases could be turned directly into revised prompts and shipped the same day, compressing what used to take months of engineering per registry into about a week. The result: Lighthouse processes over 22,000 surgical cases annually across 14 hospitals with inter-rater reliability of 98-99%, matching the industry standard for abstraction accuracy, while keeping abstractors in the loop via transparent evidence and rationale for every extracted data point.

## Key Points

- Clinical data abstraction (turning patient records into registry-ready data) is labor-intensive — a single registry program can consume 11,000+ hours of skilled labor annually; routine cases take ~60 minutes, complex ones 5-6 hours.
- Rules-based systems and NLP fail because the same clinical finding may appear as a structured field at one hospital and free-text at another; Carta Healthcare's early NLP-based approach couldn't replicate clinical judgment, motivating a move to LLMs.
- Answering registry questions requires temporal reasoning (e.g., "most recent glucose before the procedure") and disambiguation (e.g., medication ordered for discharge vs. administered during stay) — genuine clinical judgment, not database lookups.
- Carta Healthcare evaluated multiple models and selected Claude because, per Applied AI Applications Manager Hannah Glaser, "No other model we evaluated showed the same capability for understanding and interpreting clinical documentation."
- Core lesson: agent performance is determined less by the model and more by what context it's given — an excellent prompt with incomplete/unordered context underperforms, while a straightforward prompt with the right context delivers.
- Carta Healthcare's system injects patient-specific runtime context (e.g., exact procedure start time) so Claude has a precise boundary for time-sensitive questions rather than inferring it.
- Software Engineering Manager Matthew Mazzanti: "The hardest problems we solved weren't about building a perfect prompt, they were about context construction." Granular, variable-isolating evaluation frameworks let the team trace underperformance to a specific prompt, context issue, or retrieval gap rather than an opaque aggregate score.
- Production results: 22,000+ surgical cases/year across 14 hospitals, with inter-rater reliability (the industry standard accuracy measure for abstraction) reaching 98-99%.
- Transparency built trust with human abstractors: Lighthouse shows supporting evidence and Claude's rationale for every extracted data point, letting abstractors validate rather than blindly accept outputs.
- Clinical-expert feedback loop: when an abstractor flags a misextracted field, her explanation of the edge case becomes a same-day prompt revision — collapsing what used to be months of engineering/QA per registry into about a week.
- Anomaly: the raw file contains scraped page-widget boilerplate (a duplicated intro paragraph, a stray "Accelerate your enterprise AI transformation..." CTA line, and a trailing newsletter-signup fragment) — no prompt-injection content was present, just marketing-site clutter; it was excluded from this summary as non-substantive.

## Related

- [[CartaHealthcare]] — company profiled in this case study, maker of the Lighthouse platform
- [[HealthcareAI]] — broader concept this case study is folded into
- [[ContextEngineering]] — the core technical practice this article is about
- [[Claude]] — the model Carta Healthcare evaluated and selected
- [[Anthropic]] — publisher of this case study, author of the article
