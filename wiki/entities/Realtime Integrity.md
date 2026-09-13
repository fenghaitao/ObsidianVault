---
title: "Realtime Integrity"
type: entity
tags: [team, Meta, content-moderation, live-video]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md"]
last_updated: 2026-07-21
---

## Definition

Realtime Integrity was a Meta team created in response to the Christchurch mosque shooting in March 2019. Its goal was to detect in real time things like murders and suicides on live video. Evan King was the tech lead and effectively the founding engineer.

## Key Information

- Created after the March 2019 Christchurch shooting where a livestream of a mosque shooting killed 51 people and was live on Facebook for 1.5 minutes before detection
- At inception, the team was just Evan King and a PM — they were told "this is your guys's problem, figure out the scope, figure out how many engineers you need, figure out the road map"
- Initially had slow progress due to the infrequency of events and measurement challenges — training on known examples led to overfitting
- The breakthrough came from incorporating comment signals (e.g., "don't do it, your family loves you") into models, improving suicide detection recall from 9% to 55% almost overnight
- By the time Evan left Meta, recall was in the mid-90s
- The team grew to 12-14 engineers at its peak and eventually split into two teams of 8 each (16 total)
- It was a "pet project" of the VP and director of the org because Mark Zuckerberg was "breathing down their neck" about preventing another atrocity
- The Golden Set Recall evaluation system was developed to holistically test the detection infrastructure by restreaming past atrocity content through Bots on real Facebook
- The team had to deal with the psychological weight of working with disturbing content and the stress of "the next atrocity happens and we get the phone call that we blew it again"

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Meta]] — parent company
- [[Evan King]] — tech lead and founding engineer
- [[Content Integrity]] — parent org
- [[Golden Set Recall]] — evaluation system built by the team
- [[Christchurch]] — the incident that triggered the team's creation
