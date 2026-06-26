---
title: "Specs-to-Code"
type: concept
tags: [ai-coding, development-methodology, anti-pattern, software-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Definition
Specs-to-code is a movement in AI-assisted development that proposes writing a specification for how an application should work, using AI to turn it into code, and then — when there's a problem — going back to the spec rather than the code. The idea is that code becomes a disposable artifact regenerated from the spec.

## Key Information
- Core premise: write a spec, run the AI "compiler," get code. If there's a problem, change the spec and recompile — never look at the code
- Matt Pocock critiques this as "vibe coding by another name"
- In practice, repeatedly running the compiler produces progressively worse code due to software entropy
- Each iteration makes the code worse because changes are made without considering overall system design
- The movement is driven by the belief that "code is cheap" — Pocock argues the opposite: bad code is the most expensive it's ever been
- Specs-to-code divests from system design rather than investing in it daily (contra Kent Beck)
- Contrasts with approaches that treat code as important and invest in its design (deep modules, TDD, ubiquitous language)

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[Software Entropy]] — the mechanism by which specs-to-code fails
- [[VibeCoding]] — related anti-pattern
- [[SpecificationDrivenDevelopment]] — related but more structured approach
- [[Code is Not Cheap]] — the counter-argument
- [[Code is Free]] — the premise specs-to-code is built on
- [[Code as Disposable Build Artifact]] — related paradigm
- [[MattPocock]] — critic of this approach
