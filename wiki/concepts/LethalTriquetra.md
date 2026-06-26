---
title: "LethalTriquetra"
type: concept
tags: [security, ai, risk-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md"]
last_updated: 2026-06-26
---

## Definition
The lethal triquetra is a security risk model created by Simon Willison that combines three factors — private data, untrusted content, and external communications — to assess the vulnerability of AI systems. When all three are present, the system is at maximum risk.

## Key Information
- Created by Simon Willison
- Three factors: private data, untrusted content, and external communications
- Šimon Podhajský initially thought Fulan "only broke the lethal triquetra" but later acknowledged it doesn't fully — it removes natural exfiltration channels but shell access still represents the "external communications" leg
- The model is used as a framework for examining where AI systems are vulnerable, not as a pass/fail test
- "The worst security posture is the one you haven't examined" — the value is in the examination, not in claiming security
- Even in the best case, data is still sent to Anthropic on a mostly open network

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[SimonWillison]] — creator of the model
- [[MosaicEffect]] — related security concept
- [[ReadOnlyAI]] — design philosophy that partially mitigates triquetra risks
- [[LethalTrifecta]] — related but distinct concept (agent-specific: code execution + file system + network)
