---
title: "IntentionalFriction"
type: concept
tags: [agent-engineering, software-process, code-review, friction]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Intentional friction is the deliberate introduction of checkpoints, reviews, and judgment calls into the software development process — especially when using AI coding agents. It is the counterpoint to the "ship without friction" mindset, recognizing that friction is where human judgment, experience, and steering live.

## Key Information
- Armin Ronacher and Cristina Poncela Cubeiro argue that friction is necessary for steering: "Without friction there's no steering"
- SLOs (Service Level Objectives) are cited as an example of intentionally designed friction in large engineering organizations — they force teams to think about reliability, criticality, and staffing
- The drive to eliminate friction from shipping is dangerous when AI agents can produce months of technical debt in days
- Friction should be positively associated with judgment and experience, not seen as an obstacle
- Key areas where intentional friction is essential: database migrations, permission changes, dependency additions, system architecture decisions
- The goal is not to eliminate friction but to place it strategically where human judgment is irreplaceable

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[HumanCallouts]] — implementation pattern for intentional friction in code review
- [[MechanicalEnforcement]] — automated friction via linting rules
- [[CodeReviewAmplification]] — the problem intentional friction addresses
- [[AgentLegibleCodebase]] — complementary design philosophy
- [[ArminRonacher]] — key proponent
- [[CristinaPoncelaCubeiro]] — key proponent
