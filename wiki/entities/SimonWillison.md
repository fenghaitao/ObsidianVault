---
title: "SimonWillison"
type: entity
tags: [person, security, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Simon Willison is a security researcher and creator of the lethal triquetra security risk model, which combines three factors — private data, untrusted content, and external communications — to assess AI system vulnerability.

## Key Information
- Creator of the lethal triquetra / Lethal Trifecta security risk model
- The Lethal Trifecta combines three factors: private data, untrusted content, and external communications — when all three collide in the same context, data loss is essentially guaranteed
- Chris Parsons uses the Lethal Trifecta as a guiding principle for agent sandboxing: minimize collisions between untrusted tokens, internet access, and secret data
- Šimon Podhajský references the lethal triquetra when assessing Fulan's security posture, noting that while Fulan removes natural exfiltration channels, shell access still represents the "external communications" leg
- The model is used as a framework for examining where AI systems are vulnerable
- Peter Steinberger noted Simon Willison has been "working a lot" on prompt injection; the dual LLM approach "seems smart"
- Peter acknowledged he hasn't worked on prompt injection "probably enough yet" but that front-end models are getting quite good at detecting random injection from websites/email
- Creator of Django; top blogger and most-submitted contributor on Hacker News
- Told Gergely Orosz in 2024 that after 2 years of using AI, he's still figuring out what works — "there's no manual" for AI productivity

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (prompt injection work)
- [[summary-20260421 - How AI is changing Software Engineering： A Conversation with Gergely Orosz, @pragmaticengineer]] — source (2 years still figuring out AI)
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source (Lethal Trifecta)
- [[LethalTrifecta]] — security model he created
- [[Lethal Triquetra]] — alternate name for the model
- [[MosaicEffect]] — related security concept discussed alongside the triquetra
- [[ReadOnlyAI]] — design philosophy that partially mitigates triquetra risks
- [[PromptInjection]] — security problem he works on
- [[LeavingPriorsBehind]] — his experience exemplifies the concept
- [[ChrisParsons]] — applies Lethal Trifecta to agent sandboxing
- [[Agent Sandboxing]] — mitigation approach based on his model
