---
title: "Golden Set Recall"
type: entity
tags: [project, Meta, evaluation, ML, content-moderation]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Golden Set Recall was an evaluation system and project built by Evan King and the Realtime Integrity team at Meta. It curated a "golden set" of past atrocity content and used Bots to legitimately restream that content on real Facebook infrastructure to holistically test detection systems end-to-end.

## Key Information

- Created to solve the measurement problem: the team had no way to know if their detection was improving because atrocities happened so infrequently
- The golden set included all past atrocities that had happened since live video went live on Facebook (around 2011-2012)
- Bots would legitimately restream the content on real Facebook, complete with comments coming in at the right time, to test the full infrastructure holistically
- Required full isolation — if any real user saw any of this content, it would be "an absolute nightmare"
- The evaluation revealed that live suicide detection recall was only 9% at the time of measurement
- Grew from a team project to an organization-wide project, then an Integrity-wide project across several thousand people
- This was Evan King's largest project at the time and was a key component of his IC6 promotion packet

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Realtime Integrity]] — the team that built it
- [[Evan King]] — creator of the system
- [[Meta]] — company where it was built
- [[Content Integrity]] — parent org
