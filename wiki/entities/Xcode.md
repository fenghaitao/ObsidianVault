---
title: "Xcode"
type: entity
tags: [tool, IDE, Apple, iOS]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Xcode is Apple's IDE for iOS/macOS development, which Michael Bolin found did not scale to Facebook's giant mobile app and which motivated him to build Nuclide as a replacement.

## Key Information

- Bolin disliked Objective-C's header/implementation file split and ARC-era reference-counting patterns, and felt Xcode "just didn't feel right."
- Facebook always had "the biggest app" and hit the scaling limits of mobile developer tools before everyone else; Facebook told Apple Xcode wasn't scaling, and Apple's response was "your project's too big, you should make it smaller."
- That feedback made building a Facebook-specific IDE (Nuclide) justifiable — no off-the-shelf tool would support Facebook's own build system (Buck), Mercurial, and other bespoke infrastructure.
- Bolin found IntelliJ (for Android) was "actually quite good" at scale, but Xcode was more difficult, so the IDE effort targeted iOS.

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — who found Xcode insufficient at Facebook's scale
- [[Nuclide]] — the IDE built to replace Xcode
- [[Buck]] — the build system Xcode never integrated
- [[Facebook]] — the company that hit Xcode's limits
