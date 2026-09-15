---
title: "ComponentScript"
type: entity
tags: [technology, framework, cross-platform, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md"]
last_updated: 2026-09-14
---

## Definition

ComponentScript was Adam Ernst's cross-platform UI framework at Meta — a simplified, React-like API running on top of the existing native frameworks ComponentKit (iOS) and Litho (Android) — which failed after about two years and was fully deleted.

## Key Information

- Prompted by manager Ari Grant, who wanted to escape the per-platform silo (iOS ComponentKit vs Android Litho) without using React Native.
- Adams first attempted to make "a different React Native" on top of ComponentKit and Litho, but React's surface area was too large; he pivoted to a pared-down React-like API.
- Technically it "checked all the boxes": type-safe, integrated with GraphQL, ComponentKit and Litho, and bidirectional (native could always embed in it and vice versa).
- Failed despite technical excellence because it: (1) targeted no specific engineer audience — iOS engineers didn't want JavaScript and JS engineers wanted React Native; (2) bet on slow, janky GraphQL tooling; and (3) scattered adoption among individual engineers rather than a committed team.
- Was killed after a "meets most" rating; Adam Ernst deleted the code and helped teams migrate off rather than leaving a long tail to clean up later.
- He published a candid public postmortem as catharsis and to stop others repeating the mistakes — and gained goodwill from killing it responsibly.

## Related

- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[Adam Ernst]] — creator
- [[ComponentKit]] — iOS framework it ran on
- [[React Native]] — the alternative it tried to improve on
- [[GraphQL]] — the data layer that slowed it down
- [[Meta]] — the company context
- [[Good Failure]] — the postmortem lesson
