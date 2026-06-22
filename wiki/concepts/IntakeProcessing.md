---
title: "IntakeProcessing"
type: concept
tags: [automation, content-capture, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md]
last_updated: 2026-06-22
---

## Definition

Intake processing is Brian Casel's automated system for capturing all of his published content and daily work into a structured file system that his AI agents can draw from. It runs daily, ingesting podcasts, tweets, YouTube transcripts, newsletters, journal entries, and Claude Code session logs, then creates nightly summaries.

## Key Information

- **Published content captured**: podcast transcripts (The Panel), tweets, YouTube video transcripts, newsletter editions (Builder Briefing).
- **Internal work captured**: journal entries (business strategy), Claude Code session logs (all coding sessions).
- All stored in Dropbox in organized folders.
- A nightly agent job (3 AM) reads recent entries and creates daily summaries.
- The summaries themselves aren't the main value — the accumulated corpus is what agents draw from for content ideation, research, and context.
- Enables agents to answer questions like "what did I work on 2 weeks ago?" and make connections across work.
- Originally built on [[OpenClaw]], ported to [[HermesAgent]].

## Related

- [[BrianCasel]] — creator
- [[NightShiftModel]] — the pattern it follows
- [[HermesAgent]] — the platform running it
- [[ContentIdeation]] — what the captured content feeds
- [[SecondBrain]] — related concept (Cole Medin's version)
