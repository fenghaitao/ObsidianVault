---
title: "Outrunning Your Headlights"
type: concept
tags: [software-engineering, ai-coding, feedback-loops, tdd]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Definition
"Outrunning your headlights" is a metaphor from The Pragmatic Programmer describing the practice of producing too much code without feedback. The rate of feedback is your speed limit — producing code faster than you can verify it leads to accumulating bugs and design problems.

## Key Information
- From The Pragmatic Programmer by Andrew Hunt and David Thomas
- The metaphor: driving too fast for your headlights to illuminate the road ahead
- In software: producing large amounts of code before checking if it works, type-checks, or passes tests
- AI by default is very bad at this — it produces huge amounts of code and only then thinks about type-checking or testing
- AI doesn't use feedback loops well in the way a veteran developer would
- The solution is TDD: write a test first, make it pass, then refactor — forcing small deliberate steps
- Static types, browser access for front-end apps, and automated tests are essential feedback loops
- Even with feedback loops available, AI tends to not use them effectively without being forced to

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[Software Entropy]] — the result of outrunning your headlights
- [[MattPocock]] — speaker who identified this AI behavior
- [[KentBeck]] — creator of TDD, the solution
- [[DevXFeedbackLoop]] — related concept
