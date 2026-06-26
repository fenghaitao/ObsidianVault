---
title: "ZeroBugPolicy"
type: concept
tags: [quality, bug-fixing, engineering-process, linear, ai-agents]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md"
last_updated: 2026-06-26
---

## Definition
Zero Bug Policy is an engineering practice where every reported bug is assigned immediately and becomes the assignee's highest priority, to be fixed within hours rather than backlogged. The policy is based on the insight that the rate of bug creation is constant, so fixing bugs immediately costs no more effort than fixing them months later — but provides dramatically better user experience and prevents quality debt accumulation.

## Key Information
- Instituted at Linear by CTO Tuomas Artman
- Every reported bug is automatically assigned (using AI agents) to the engineer who created it or works in that area
- The bug becomes the assignee's highest priority — it's the first thing they pick up in the morning
- Engineers can decide not to fix a bug if it's extremely hard and affects very few users
- Most bugs are fixed within 2-3 hours of being reported
- Linear spent three weeks of no new feature development to bring their bug count to zero, then enforced immediate fixing going forward
- The core insight: the rate of bug creation is constant at every company. Whether you fix bugs immediately or months later, the total effort is the same — but fixing immediately prevents quality debt
- Users get extremely excited when they report a bug and receive an email two hours later saying it's fixed
- 10% of bugs at Linear are now automatically fixed by single-shot AI — an agent creates a PR and lands it without engineer involvement
- Tuomas Artman believes this will approach 100% in the next few years
- Tuomas argues that with AI's help, "literally every company should have a zero bug policy"

## Related
- [[summary-20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer]] — source transcript
- [[TuomasArtman]] — instituted the policy at Linear
- [[Linear]] — company practicing this policy
- [[QualityWednesdays]] — complementary practice at Linear (separate from bug fixing)
- [[CompetitionThroughQuality]] — the strategic rationale for fixing bugs immediately
