---
title: "Comet"
type: entity
tags: [product, ai-browser, security]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Definition

Comet is [[Perplexity]]'s AI-powered web browser, cited by [[Sander Schulhoff]] (and confirmed by [[Lenny Rachitsky]], who uses it) as the subject of a real-world indirect [[Prompt Injection]] data-leak incident.

## Key Information

- A malicious chunk of text was crafted into a web page; when Comet's AI navigated to that page, it was tricked into exfiltrating and leaking the logged-in user's account/personal data.
- Schulhoff notes this vulnerability class is not unique to Comet — he expects it applies to [[Atlas]] (OpenAI's browser) and "probably all the AI browsers."

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Perplexity]] — maker of Comet
- [[Sander Schulhoff]] — cites this incident
- [[Atlas]] — comparable AI browser Schulhoff expects shares the same vulnerability class
- [[Prompt Injection]] — the attack class this incident exemplifies
