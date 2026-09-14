---
title: "Code Review Culture"
type: concept
tags: [engineering, process, culture, code-quality]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250531 - Instagram Principal Engineer (IC8)： Promotions, Breaking Prod, Tech Leading ｜ Jake Bolam.md"]
last_updated: 2026-09-14
---

## Definition

Code Review Culture refers to the norms and processes around how code changes are reviewed before being merged. Rahul Pandey observed stark differences between Pinterest's rigorous two-reviewer system with blocking herald rules and Meta's lighter single-accept culture.

## Key Information

### Pinterest's Code Review Culture
- Every code change was reviewed by at least two people
- "Herald rules" automatically added reviewers for specific parts of the codebase
- These were blocking reviewers — you couldn't land code until they took a look
- This created a more thorough but slower development process

### Meta's Code Review Culture
- Usually only one accept (LGTM, green check mark) was needed to land code
- Rahul was "kind of shocked" at how quickly people could land code without all the checks and balances
- This was part of Meta's broader culture of speed and impact

### Cultural Implications
- The code review culture reflects broader organizational values: Pinterest was "too nice" while Meta was more direct
- Meta's culture was more willing to say "this doesn't make sense, why are you doing this, let's cut it or kill it"
- Meta had a more aggressive PIP culture compared to Pinterest
- The lighter review process at Meta enabled faster iteration but potentially less oversight

### Jake Bolam's Risk-Based Review Philosophy
- Review depth should scale with risk: thorough on core/prod surfaces, light and trust-based on gated leaf components
- He prefers "how do I accept this diff" over "how do I reject it" — look for what absolutely blocks production, not rewrite-to-your-style
- He'll even comment "this will blow up production" and still accept, trusting a teammate to fix it first
- Leaf components are cheap to fix if they fail, so lower quality there is acceptable; bad architecture in the trunk is expensive to fix
- He invites authors to flag "need real review" so he doesn't under-review something they consider critical

## Related

- [[summary-20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey]] — source summary
- [[Meta]] — the lighter review culture
- [[Pinterest]] — the more rigorous review culture
- [[Rahul]] — experienced both cultures
- [[Impact-Driven Culture]] — Meta's culture that influenced the review process
- [[Jake Bolam]] — his risk-based review philosophy
- [[summary-20250531 - Instagram Principal Engineer (IC8)： Promotions, Breaking Prod, Tech Leading ｜ Jake Bolam]] — source summary
