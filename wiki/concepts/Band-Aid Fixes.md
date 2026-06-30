---
title: "Band-Aid Fixes"
type: concept
tags: [ai, llm, model-limitations, agent-design, technical-debt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver.md"]
last_updated: 2026-06-30
---

## Definition
Band-aid fixes are temporary, superficial workarounds that mask the symptoms of LLM constraints rather than addressing the underlying problems. In the context of AI engineering, most tools and techniques built around models are band-aids — quick fixes that are inadequate in the long run and will be superseded as models improve.

## Key Information
- Introduced by Angus J. McLean as a framework for evaluating AI tools and techniques.
- Characteristics of band-aid fixes:
  - **Temporary**: quick fixes, not long-term solutions
  - **Superficial**: mask symptoms rather than fixing the root problem
  - **Inadequate**: don't fully address the underlying issues
- Examples include many common AI engineering patterns: RAG pipelines, complex prompt engineering, classifier chains — all exist because models have limitations today.
- Even the way models themselves are trained can be seen as a form of band-aid — techniques like RLHF exist to compensate for fundamental model limitations.
- The key insight: as models improve, many band-aids become obsolete. The question is whether to invest in band-aids or wait for model improvements.
- This parallels the "AGI pill" philosophy from Anthropic: don't over-engineer around model flaws today because models will get better.
- Spotting band-aids helps teams avoid over-investing in infrastructure that will be short-lived.

## Related
- [[Angus J. McLean]] — speaker who introduced the concept
- [[summary-20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver]] — source
- [[SimpleDesignPhilosophy]] — the counter-approach: less scaffolding, more model
- [[LLM as Fuzzy Compiler]] — related framing of LLM limitations
- [[TechnicalDebtInML]] — the broader problem of accumulating workarounds
- [[Bounded Autonomy]] — the parent framework
