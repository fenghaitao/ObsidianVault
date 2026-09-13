---
title: "Content Moderation"
type: concept
tags: [engineering, ML, Meta, safety]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Content Moderation is the process of detecting, reviewing, and taking action on violating content on online platforms. At Meta, this involves ML models, human review, and infrastructure to handle everything from hate speech to graphic violence to live-streamed atrocities.

## Key Information

- Content moderation at Meta covers: pornography, hate speech, graphic violence, suicide, terrorism, and child exploitation imagery
- The process involves multi-staged detection: crude quick checks, expensive ML models, photo matching, scoring, human review routing, and final action
- Live video moderation is fundamentally different from static content moderation — it requires real-time detection with far less data
- The psychological impact on engineers is significant: Evan described seeing pornography as "shocking and jarring" at first, but noted that engineers "become desensitized"
- The Seattle office content integrity team was "hidden on the second floor in the corner" so nobody would walk past desks and see disturbing content
- Content moderation engineers deal with the stress of "the next atrocity happens and we get the phone call that we blew it again"
- The field suffers from measurement challenges: atrocities happen infrequently, making it hard to evaluate model performance
- Evan's work was "deeply fulfilling" because he felt he was having a real-world impact preventing harmful content

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Content Integrity]] — Meta org responsible for content moderation
- [[Realtime Integrity]] — team focused on live video moderation
- [[Machine Learning]] — the core technology used
- [[Golden Set Recall]] — evaluation system for content moderation models
