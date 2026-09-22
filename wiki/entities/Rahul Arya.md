---
title: "Rahul Arya"
type: entity
tags: [person, engineer, AI, Google]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Rahul Arya is a Google engineer who, with a report (transcribed "Gangyan") and Google's Israel team, applied pipeline prefill to mixture-of-experts models for Gemini Flash 2.0.
## Key Information
- He worked on transferring the pipelining technique from the dense case to MoE, where it moved layers (not experts) across machines.
- The result hid token-routing communication behind other computation and made MoE latency attractive enough for the Flash 2.0 architecture decision.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — colleague
- [[Gemini Flash]] — pipeline prefill application
- [[Pipeline Parallelism]] — the technique
