---
title: "Declarative UI"
type: concept
tags: [engineering, UI, frameworks, iOS, design]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Definition

Declarative UI is a user-interface paradigm — exemplified by React, SwiftUI, and ComponentKit — in which developers state what the interface should be ("a button with this caption") and the framework derives and manages the actual views, rather than imperatively mutating views directly.

## Key Information

- Adam Ernst contrasts it with Visual Basic's drag-and-drop/imperative style, where there's no separation between describing UI and the code that builds it.
- Core mechanics of the declarative approach: components, immutability, "re-render everything" when anything changes, and view reconciliation — the developer no longer directly manages UI views.
- ComponentKit let Facebook's newsfeed render view hierarchies on a background thread and do minimal work on the main thread.
- Adam Ernst is clear-eyed about trade-offs: declarative UI is ideal for mostly-static, deeply nested scrolling lists (like a newsfeed), but less natural for super-dynamic surfaces like drag-and-drop.
- Peter pointed out that even though it's "an alien way to write code on iOS," once convinced, engineers loved it.

## Related

- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[React]] — the canonical declarative framework
- [[ComponentKit]] — the iOS declarative framework
- [[Adam Ernst]] — built ComponentKit around this paradigm
- SwiftUI (which did not exist yet in 2014) is Apple's later native declarative framework — alongside React and ComponentKit, one of the examples Adam Ernst cites
