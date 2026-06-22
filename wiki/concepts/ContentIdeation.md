---
title: "ContentIdeation"
type: concept
tags: [automation, content-creation, brian-casel]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260609 - Hermes vs. Claude Cowork Wrong Question.md, raw/03-transcripts/Brian Casel/Channel Only/20260429 - Multitasking With Agents： My 2026 Workflow.md]
last_updated: 2026-06-22
---

## Definition

Content ideation is the agent-driven process of researching, generating, and pitching new content ideas (videos, articles, social posts) based on captured work, audience data, and external trends. Brian Casel uses it as a recurring Night Shift task to keep his content pipeline fed.

## Key Information

- Multi-phase skill: research sources → generate ideas → pitch to Brian → develop drafts → schedule.
- Sources include: [[IntakeProcessing]] captures (podcasts, tweets, journals), audience surveys, external trend monitoring (YouTube, Reddit, X/Twitter).
- Brian's content ideation skill runs on [[ClaudeCowork]] using Claude Opus (his preferred model for creative work).
- Ideas are submitted to [[SparkDrop]] via API as "sparks" for Brian to review, comment on, and greenlight.
- The agent learns from Brian's feedback: creates "learnings" that fold back into training data.
- Brian still puts significant personal input into ideas before development — the agent sparks possibilities, he curates.

## Related

- [[BrianCasel]] — creator
- [[NightShiftModel]] — the pattern
- [[SparkDrop]] — the app that receives ideas
- [[IntakeProcessing]] — the content source
- [[ClaudeCowork]] — the platform running it
- [[ResonanceRadar]] — the external trend monitoring component
