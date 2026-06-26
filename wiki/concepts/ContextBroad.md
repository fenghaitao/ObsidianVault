---
title: "ContextBroad"
type: concept
tags: [context, llm, performance, degradation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is.md"]
last_updated: 2026-06-25
---

## Definition
Context Broad is a phenomenon documented by Chroma's research showing that LLM performance degrades as context windows grow, even when the amount of relevant information remains constant. The larger the context, the worse models perform at finding and reasoning about relevant information.

## Key Information
- Documented in Chroma's "Context Broad" report
- Performance degradation begins noticeably around 10,000 tokens and becomes severe beyond that
- Claude performs best at resisting context broad degradation compared to other models
- At ~10^4 tokens (10,000), models "don't work at all" — they output grammatical text but fail to actually solve problems
- This is distinct from models "breaking" (producing nonsensical output); they appear coherent but are ineffective
- The phenomenon explains why long context windows (1M-2M tokens) don't translate to practical effectiveness
- Even with efficient architectures (Mamba, linear attention, sparse attention), the trade-off between efficiency and reasoning quality persists

## Related
- [[summary-20251229 - Jack Morris： Stuffing Context is not Memory, Updating Weights is]] — source
- [[Chroma]] — published the report
- [[Context Management]] — techniques to mitigate this
- [[RAG]] — alternative approach that avoids large contexts
