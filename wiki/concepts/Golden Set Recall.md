---
title: "Golden Set Recall"
type: concept
tags: [engineering, evaluation, ML, testing, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Golden Set Recall is the evaluation methodology of curating a fixed set of known positive examples (a "golden set") and measuring how many of them a detection system successfully identifies (recall). It was the core evaluation approach for Meta's Realtime Integrity team.

## Key Information

- The methodology was designed to solve the measurement problem: atrocities happen so infrequently that you can't evaluate models on live data
- The golden set included all past atrocities since live video went live on Facebook
- Bots would legitimately restream the content on real Facebook to test the full infrastructure holistically — not just models, but the entire pipeline
- Required full isolation: if any real user saw the test content, it would be "an absolute nightmare"
- The evaluation revealed that live suicide detection recall was only 9%
- The approach is similar to the concept of a "holdout set" in ML, but applied to an end-to-end production system
- The methodology was so successful it grew from a team project to an organization-wide, then Integrity-wide project
- Having a reliable evaluation metric was what enabled the team to iterate and improve from 9% to mid-90s recall

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Golden Set Recall]] — the project entity that implemented this concept
- [[Realtime Integrity]] — the team that used this methodology
- [[Content Moderation]] — the domain where this evaluation approach was applied
