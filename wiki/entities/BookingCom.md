---
title: "BookingCom"
type: entity
tags: [company, travel, ai, eval]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-25
---

## Definition
Booking.com is a travel e-commerce company and Arize client, used as an example of how to handle subjective evaluation use cases in prompt learning.

## Key Information
- Arize client that uses LLM evaluation for subjective tasks such as determining what constitutes a good property posting or attractive hotel photo.
- Their use case demonstrates the challenge of defining success criteria for subjective evaluations where quality is not universally agreed upon.
- The recommended approach for such cases is to start with binary classification (good/bad) and iteratively refine into more granular criteria (e.g., dimly lit, room layout, etc.).

## Related
- [[Arize]] — AI observability platform used by Booking.com
- [[EvalEngineering]] — practice relevant to their subjective evaluation challenges
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
