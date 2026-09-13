---
title: "Real-Time Detection"
type: concept
tags: [engineering, ML, live-video, safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Real-Time Detection is the ability to identify violating content in live video streams as they are happening, rather than after the fact. It is fundamentally more challenging than static content moderation due to the need for immediate detection, limited training data, and severe consequences of failure.

## Key Information

- Real-time detection of atrocities on live video is a "different fundamental challenge" from detecting static content
- The Christchurch shooting (livestreamed for 1.5 minutes before detection) was the catalyst for Meta to invest in real-time detection
- Key challenges: limited training data (atrocities happen infrequently), overfitting risk (training on known examples), and measurement difficulty (need the next atrocity to know if you're improving)
- The measurement problem was solved by Golden Set Recall — restreaming past atrocity content through Bots on real Facebook infrastructure
- The breakthrough came from incorporating comment signals into models ("don't do it, your family loves you") rather than just pixel and audio analysis
- Comment-based detection improved suicide recall from 9% to 55% almost overnight, and eventually to mid-90s
- The insight: "the people who are posting the comments know of the atrocity long before our sophisticated models were able to figure it out"
- Evan's holistic approach — focusing on the overall problem rather than just model sophistication — was key to finding the simple solution

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Realtime Integrity]] — team responsible for real-time detection
- [[Golden Set Recall]] — evaluation system for real-time detection
- [[Content Moderation]] — the broader domain
- [[Christchurch]] — the incident that triggered the focus on real-time detection
