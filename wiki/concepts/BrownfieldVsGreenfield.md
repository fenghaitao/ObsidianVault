---
title: "BrownfieldVsGreenfield"
type: concept
tags: [software-engineering, ai, project-type, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
Brownfield vs. Greenfield is the distinction between modifying existing, mature codebases (brownfield) and building new projects from scratch (greenfield). This distinction is critical for evaluating AI coding tools because the two contexts present fundamentally different challenges.

## Key Information
- Brownfield projects involve mature open-source repositories where developers have years of accumulated context and the codebase has established patterns
- Greenfield projects involve building something new, where AI may have more room to contribute without conflicting with existing architecture
- METR's RCT used brownfield projects (mature open-source repos like the Haskell compiler, HuggingFace Transformers, scikit-learn)
- A natural hypothesis is that AI would show more productivity gains on greenfield projects
- METR ran an unpublished greenfield hackathon randomizing AI access; found only ~4 percentile point improvement with AI allowed, with enormous overlap between groups
- Open-source projects have different incentive structures than enterprise codebases: maintainers prioritize maintainability over feature velocity, leading to higher rejection rates for AI-generated PRs
- Enterprise codebases survive because they make money even if they're difficult to develop on, creating different dynamics for AI tool adoption

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[RandomizedControlledTrial]] — brownfield study by METR
- [[MergeabilityScoring]] — relevant to brownfield PR acceptance
- [[METR]] — organization studying this distinction
