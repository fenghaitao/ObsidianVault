---
title: "React Native"
type: entity
tags: [technology, framework, cross-platform, mobile]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Definition

React Native is Facebook's framework for building native mobile apps using React and JavaScript.

## Key Information

- Around 2014 it either didn't exist or was only a prototype; it also did not exist yet when ComponentKit was invented.
- Was designed (in Adam Ernst's view) to be "in charge of the entire app" — it works well when the whole app is React Native with small native/bridged pieces at the bottom.
- Did not fit Facebook's mid-2010s architecture, where they wanted to slot small cross-platform pieces into different areas of a large existing native app.
- ComponentScript was explicitly an attempt to build a "different React Native" on top of their existing native frameworks (ComponentKit and Litho), which was abandoned.

## Related

- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[React]] — the underlying library
- [[ComponentKit]] — the iOS framework it would have run on
- [[ComponentScript]] — Adam Ernst's attempt at a cross-platform alternative
- [[Meta]] — the company behind it
