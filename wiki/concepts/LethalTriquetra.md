---
title: "LethalTriquetra"
type: concept
tags: [security, ai, risk-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
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
- Peter Steinberger described the same concept independently: "Any agentic system that has access to your data, has access to untrusted content, and the ability to communicate is something that's potentially at risk. That's not anything special to OpenClaw. It's like any agent, any powerful agent system has a problem."
- "The more powerful you make it, the more it can do for you, but the more you also have to understand what it does"
- OpenClaw's security recommendations directly address the triquetra: personal agent should not be in group chat (limits untrusted content), team agent should use sandboxing (limits communication/exfiltration), personal agent should only be accessible by owner (limits untrusted content)

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source (independent description)
- [[SimonWillison]] — creator of the model
- [[MosaicEffect]] — related security concept
- [[ReadOnlyAI]] — design philosophy that partially mitigates triquetra risks
- [[LethalTrifecta]] — related but distinct concept (agent-specific: code execution + file system + network)
- [[OpenClaw]] — project whose security model addresses the triquetra
- [[PeterSteinberger]] — independently articulated the same risk model
- [[Sandboxing]] — key mitigation for the communication leg
