---
title: "Context Assembly"
type: concept
tags: [ai, context, context-engineering, llm, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver.md"]
last_updated: 2026-06-30
---

## Definition
Context assembly is the dynamic process of constructing an agent's context window — selecting what to include and what to exclude. It represents the evolution from static, frequency-based approaches (like TF-IDF for cluster labeling) to dynamic, need-based context construction, where the challenge has shifted from getting enough context in to keeping noise out.

## Key Information
- Introduced by Angus J. McLean in the context of how agent development has evolved with increasing context windows.
- Historical approach (small context windows): TF-IDF for cluster labeling — take the most frequent words within a cluster to label it, use top-K approaches.
- Modern approach (large context windows): dynamic context assembly — selectively include what's needed and exclude what's noise.
- The challenge has inverted: from "how do I fit everything in?" to "what should I leave out?"
- Context constraints act as soft constraints on the model — as powerful as guardrails in shaping behavior.
- Practical example: not giving a model internet access and instead providing high-quality documentation yields much better results — the assembly of context matters more than the raw availability of information.
- Models are bad at spotting promotional content and very susceptible to SEO — what you include in context assembly determines output quality.
- Key insight: context assembly is a form of bounded autonomy — you're choosing the bounds within which the agent operates.
- This connects to broader context engineering: deliberate curation of what goes into the context window.

## Related
- [[Angus J. McLean]] — speaker who introduced the concept
- [[summary-20260525 - Bounded Autonomy： Between Free Will and Determinism — Angus J. McLean, Oliver]] — source
- [[ContextEngineering]] — the broader discipline of context curation
- [[Context Management]] — related techniques for maintaining context coherence
- [[Context Budget]] — the practical constraint on what can be assembled
- [[ProgressiveDisclosure]] — loading context on demand rather than all at once
- [[SmartTruncation]] — Arize's approach to context selection
- [[Bounded Autonomy]] — the parent framework
