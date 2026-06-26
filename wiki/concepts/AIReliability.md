---
title: "AIReliability"
type: concept
tags: [ai, reliability, developer-productivity, correctness]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md"]
last_updated: 2026-06-25
---

## Definition
AI Reliability is the consistency with which AI systems produce correct outputs on a given task type. For developer productivity, reliability must be extremely high (95-99%) to save time, because verification and correction costs negate any speed gains from AI generation.

## Key Information
- **LLM non-determinism**: A fundamental barrier to LLM adoption — LLMs are non-deterministic and hard to build on, completely different from what most developers are used to. Reliability is still an issue and prompts take rounds of optimization
- Low AI reliability was identified as a key factor in METR's RCT where developers were slowed down by 19% when using AI
- Even if AI is correct 50-80% of the time, developers must still check and often correct its work, which is costly from a time perspective
- For developers to "tab tab tab through" AI suggestions without spending time verifying, reliability needs to reach 95-99%
- This is one of the hypothesized explanations for the gap between impressive benchmark results and disappointing real-world productivity gains
- Contrasts with benchmark scoring where partial correctness or pass/fail on isolated unit tests may overstate practical usefulness

## Related
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source for LLM non-determinism barrier
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[MergeabilityScoring]] — holistic scoring beyond unit test pass/fail
- [[RandomizedControlledTrial]] — study that revealed the reliability gap
- [[OveroptimismAboutAI]] — developers overestimating AI reliability
