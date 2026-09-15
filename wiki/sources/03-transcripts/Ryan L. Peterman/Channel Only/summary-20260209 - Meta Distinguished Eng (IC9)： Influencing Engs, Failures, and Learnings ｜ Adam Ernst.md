---
title: "summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Core Summary

Adam Ernst, a Distinguished Engineer (IC9) at Meta, traces his path from a middle-school software company to building iOS infrastructure that shaped how Facebook and Instagram wrote native apps. He details replacing Apple's Core Data, inventing ComponentKit (a React-like declarative UI framework for iOS) with Lee Byron's prompting, and the "total and complete failure" of ComponentScript — drawing out his lessons on influencing engineers without authority, reviewing code, and killing failed projects responsibly.

## Key Points

- He founded "CosmicSoft" in middle school, selling online testing software written in REALbasic/Visual Basic and accepting payment via mailed checks and an early e-commerce service ("Eccelerate") that issued unlock codes.
- Joined Facebook as an E5 in 2012, weeks before the IPO, during the native-code rewrite away from the HTML5 "Faceweb" app, when all iOS engineers could fit in one conference room.
- His E6 project replaced Apple's Core Data (which "falls over completely" once an iOS team grows past ~100-200 engineers) with an immutable "mem models" system that made thread-safety and mutations easier to reason about.
- To win adoption he disassembled Core Data's closed source to understand what it was doing, then used his playbook for influencing without authority: talk in person, sympathize with the other side, show data, and "do the work for them" rather than asking them to do the migration.
- He reviewed ~1,600 diffs in six months (~14/workday); he values code review as a way to influence engineers organically, prefers flexible review ("here's my concern, but here's what I'd do next time"), and explains why he cares rather than dictating "change X to Y."
- ComponentKit (2014) was his answer to Lee Byron's ask to bring React's concepts — components, immutability, re-render, view reconciliation — to iOS, years before Swift/SwiftUI/React Native; it powered Facebook newsfeed but required convincing skeptics, mediators, allies, and a compromise adopting Panels' data-source technology.
- He acknowledges declarative UI trade-offs: ideal for mostly-static scrolling lists like newsfeed, less natural for dynamic drag-and-drop interfaces.
- ComponentScript, his ~2-year cross-platform framework (a React-like API running on ComponentKit and Litho), was a "total and complete failure" despite being type-safe and technically excellent: it targeted no specific engineer audience, bet on slow GraphQL tooling, and scattered adoption among individual engineers rather than a committed team.
- A "meets most" rating was the signal to kill it; he deleted the framework and helped teams migrate, and published a candid postmortem — cathartic, and intended to stop others repeating the same mistakes; killing responsibly earned more goodwill than dragging it out.
- On staying on the IC track: he stayed on iOS by "rolling with it," built deep-plus-broad knowledge by diving "eight levels deep" into any blocking system (GraphQL codegen, Buck), and "flips the switch off" on worrying whether his code is "IC9-level" in favor of checking in with his manager.
- He always knew management wasn't for him — he loves writing code and is best at communicating with engineers on technical, not directional, problems.
- He admires engineers with distinct strengths: Dustin Shahitapor (prolific coder), Wei Han (fixer), Michael Bolan (project starter), Bob Baldwin and Oliver Ricard (communication), Nolan O'Brien (alignment and the Apple relationship).

## Related

- [[Adam Ernst]] — guest
- [[Meta]] — company where he is IC9
- [[Facebook]] — joined weeks before the IPO
- [[Instagram]] — a Meta property his iOS infrastructure served
- [[Lee Byron]] — manager who nudged him toward ComponentKit, GraphQL co-inventor
- [[GraphQL]] — relied on by ComponentScript when tooling was slow
- [[React]] — the concepts transplanted to iOS
- [[React Native]] — the cross-platform alternative he considered
- [[ComponentKit]] — his successful iOS UI framework
- [[ComponentScript]] — his failed cross-platform framework
- [[Core Data]] — the Apple ORM he replaced
- [[Buck]] — Meta's build system he knows in depth
- [[Influence Without Authority]] — how he drove adoption
- [[Code Review Culture]] — his diff-review philosophy
- [[Declarative UI]] — the paradigm behind ComponentKit
- [[Code Machine Archetype]] — his self-described working style
- [[Technical Breadth vs Depth]] — his dive-deep, breadth-building approach
- [[Good Failure]] — the ComponentScript postmortem lesson
