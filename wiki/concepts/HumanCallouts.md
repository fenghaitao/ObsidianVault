---
title: "HumanCallouts"
type: concept
tags: [code-review, agent-engineering, human-in-the-loop, automation]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Human callouts are a code review pattern developed at Earendil that separates automated, mechanical bugs (which the agent can fix automatically) from changes that require human judgment. When a pull request contains database migrations, permission changes, or dependency additions, the review tool explicitly flags these as requiring a human to "kick into gear."

## Key Information
- Implemented as a PyExtension at Earendil for code review
- Separates review feedback into two categories:
  - **Mechanical bugs**: Violations of linting rules, type errors, etc. — the agent can automatically fix these
  - **Human callouts**: Changes requiring human judgment — database migrations (depends on locks, data size in production), permission changes (often under-documented), dependency additions (do you trust the maintainers?)
- The callout is designed to give the engineer "a little bit of a hit" — a moment of recognition that they need to engage their brain
- Based on the principle: "you will miss it, but at least these machines can help you find this"
- The goal is to reactivate human judgment at the moments where the agent's lack of context and emotional awareness makes it unreliable

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[IntentionalFriction]] — the philosophy behind human callouts
- [[MechanicalEnforcement]] — the complementary automated layer
- [[CodeReviewAmplification]] — the problem human callouts help address
- [[Earendil]] — company that developed this pattern
- [[CristinaPoncelaCubeiro]] — built the PyExtension
