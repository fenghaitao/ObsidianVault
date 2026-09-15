---
title: "ComponentKit"
type: entity
tags: [technology, framework, iOS, UI, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Definition

ComponentKit is Adam Ernst's iOS UI framework, built around 2014, that brings React's declarative concepts — components, immutability, re-rendering, and view reconciliation — to iOS/Objective-C++.

## Key Information

- Created in response to Lee Byron's prompt to think through how React's concepts could work "in an iOS-first way."
- Uses components, immutability, "re-render everything when anything changes," and view reconciliation, so developers state the UI instead of directly managing views.
- Let Facebook newsfeed render view hierarchies on a background thread and do only minimal work on the main thread.
- Showed the same UI as roughly one-third the code of the imperative version.
- Was written as a C++/Objective-C++ framework (now "creaky" per Adam Ernst) with a Swift API added later.
- Adoption required overcoming pushback ("an alien way to write code on iOS"), mediators, allies, and a compromise that adopted Panels' data-source technology.
- Predated SwiftUI, Swift, and React Native, making it very early on the scene of declarative mobile UI.

## Related

- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[Adam Ernst]] — creator
- [[Lee Byron]] — prompted its creation
- [[React]] — the concepts it transplanted
- [[Declarative UI]] — the paradigm it exemplifies
- [[React Native]] — the cross-platform alternative that came later
- [[Meta]] — the company that used it
- [[ComponentScript]] — the cross-platform framework built on top of it
