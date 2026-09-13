---
title: "Technical Debt"
type: concept
tags: [engineering, code-quality, maintenance, trade-offs]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Technical Debt is the implied cost of additional rework caused by choosing an expedient solution now instead of a better approach that would take longer. Evan's "ship it and run" approach at Meta implicitly accumulated technical debt.

## Key Information

- Meta's impact-driven culture encouraged "ship it and run" which implicitly accepts technical debt in favor of speed
- Evan's approach: "experiment, see numbers go up, and if they went up, success" — without understanding why, which can lead to fragile systems
- Evan's regret: "I took shortcuts... once it works, you might move on" rather than understanding the underlying cause
- This is the trade-off: fast iteration and impact vs. sustainable, well-understood systems
- Big tech companies have infrastructure and abstractions that hide technical debt from individual engineers
- Evan noted that he "used [Meta's caching layer] every day as an abstraction" without understanding it, which is a form of knowledge debt
- The shift to deep understanding ("why it actually worked") is a move toward reducing technical and knowledge debt

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Impact-Driven Culture]] — the culture that encourages shipping over understanding
- [[Curiosity]] — the counterbalance to technical debt accumulation
