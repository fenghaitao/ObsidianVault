---
title: "Modularity"
type: concept
tags: [software-design, ai-architecture, system-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md"]
last_updated: 2026-06-25
---

## Definition
Modularity, as preached by Greg Brockman, is a design principle for AI systems where humans define clear boundaries and interfaces for critical components, while AI is free to generate the code that fills in everything between those boundaries.

## Key Information
- Advocated by Greg Brockman (OpenAI co-founder) as a key principle for AI-assisted development
- Core idea: keep clear boundaries on what is human-designed, let AI code everything in between
- Serves as a defense against slop by maintaining human oversight on architectural decisions
- Allows AI to be maximally productive on implementation details while humans retain control of design
- Aligns with the Semi-Sync Value of Depth framework: humans focus on the hardest, most critical design problems
- Was one of the highlights of the year for swyx to discuss with Brockman personally

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[GregBrockman]] — key advocate of modularity
- [[SemiSyncValueOfDepth]] — complementary framework
- [[CodeSlop]] — modularity helps prevent this
- [[swyx]] — discussed modularity with Brockman
