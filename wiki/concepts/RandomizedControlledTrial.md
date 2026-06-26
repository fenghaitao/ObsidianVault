---
title: "RandomizedControlledTrial"
type: concept
tags: [methodology, research, developer-productivity, experiment-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
A Randomized Controlled Trial (RCT) is an experimental methodology where subjects are randomly assigned to treatment and control groups to measure causal effects. METR used this approach to measure AI's effect on developer productivity.

## Key Information
- METR's RCT involved 16 experienced developers completing ~16 real work tasks each from large open-source repositories
- Tasks were randomly assigned to "AI disallowed" (no AI tools at all, like "software development in 2019") or "AI allowed" (any AI tools permitted, with Cursor Pro provided)
- Developers were paid per hour for external validity reasons
- Time to complete each task was recorded to measure the causal effect of AI access on productivity
- The study found a 19% slowdown when AI was allowed, contrary to all predictions
- Caveats: small study size, concentrated in March 2025, unusual developer population (top contributors on mature repos)
- Economists note the per-hour payment may not incentivize speed, though Becker is skeptical this affected results
- METR also ran an unpublished greenfield hackathon RCT randomizing AI access; found only ~4 percentile point improvement with AI allowed, with enormous overlap between groups
- Becker addressed the J-curve hypothesis in follow-up: plots showed no clear relationship between Cursor familiarity and productivity, though sample sizes were too small for strong conclusions
- The median PR in the study required zero minutes of post-review code work — developers' professional incentives drove extremely high quality

## Related
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[METR]] — organization that conducted the RCT
- [[JoelBecker]] — co-author of the RCT
- [[AIReliability]] — key finding from the RCT
- [[OveroptimismAboutAI]] — key finding from the RCT
- [[ContextBaselines]] — methodological consideration
- [[JCurveFamiliarityEffect]] — debated in relation to RCT findings
- [[BrownfieldVsGreenfield]] — project type distinction relevant to the RCT
