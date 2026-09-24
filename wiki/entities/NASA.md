---
title: "NASA"
type: entity
tags: [organization, aerospace, real-time-systems]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260914 - Casey Muratori： Surprises In Computer History And Where Bad Code Comes From.md"]
last_updated: 2026-09-24
---

## Definition

NASA is the United States space agency whose Apollo program ran real-time flight software managed by Margaret Hamilton.

## Key Information

- Casey cites NASA's "no recursion" rule as sane for safety-critical code: recursion hides stack-depth bounds, whereas a loop plus an explicit stack and state machine is fully predictable.
- The Apollo guidance computer's 1201/1202 alarm handling is cited as a triumph of fault-tolerant engineering.

## Related

- [[summary-20260914 - Casey Muratori： Surprises In Computer History And Where Bad Code Comes From]] — source summary
- [[Margaret Hamilton]] — managed Apollo flight software
