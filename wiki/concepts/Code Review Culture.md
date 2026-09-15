---
title: "Code Review Culture"
type: concept
tags: [engineering, process, culture, code-quality]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250531 - Instagram Principal Engineer (IC8)： Promotions, Breaking Prod, Tech Leading ｜ Jake Bolam.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
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

### Adam Ernst's Diff-Review Philosophy

- Reviewed ~1,600 diffs in six months (~14/workday); he still does a lot of code review because it lets you influence engineers "in an organic way."
- Be flexible: "here's my concern and why," then either let the author decide or redo together — not blanket reject.
- Comment on why you care, not just what to change: explain the problem with X and suggest Y, rather than dictating "change X to Y."
- Assume you may be missing context and ask the author to fill it in (and put it in the diff summary) — so if you're wrong, you don't look like "a total idiot."

### Michael Bolin on AI-Assisted Code Review
- At OpenAI, Bolin's preferred approach is to have the agent do multiple rounds of review until it is confident the change is worth a human's time, but a human still looks at it before it merges.
- Humans still catch things the agent misses — often a "gap in knowledge" that needs context added back into the repo or a detail not yet memorialized that the human happens to know.
- AI-generated pull-request summaries ("the why and the what, the reason behind the PR") make review faster and are getting better across the team, which matters because there is "a lot more review to do" as agents write more code ([[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]]).

## Related
- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[Adam Ernst]] — his code-review philosophy

- [[summary-20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey]] — source summary
- [[Meta]] — the lighter review culture
- [[Pinterest]] — the more rigorous review culture
- [[Rahul]] — experienced both cultures
- [[Impact-Driven Culture]] — Meta's culture that influenced the review process
- [[Jake Bolam]] — his risk-based review philosophy
- [[summary-20250531 - Instagram Principal Engineer (IC8)： Promotions, Breaking Prod, Tech Leading ｜ Jake Bolam]] — source summary
- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — AI-assisted review at OpenAI
- [[Codex]] — the agent doing multiple review rounds
