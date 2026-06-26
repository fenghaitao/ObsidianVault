---
title: "ReadOnlyAI"
type: concept
tags: [ai, design-philosophy, personal-ai, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md"]
last_updated: 2026-06-26
---

## Definition
Read-only AI is a design philosophy and product category where AI systems have read access to data sources but no write permissions — they observe, analyze, and reflect, but never act on behalf of the user or modify source data. Šimon Podhajský argues this is not a stepping stone to agentic AI but a distinct and underrated category.

## Key Information
- Core principle: read access only, no write permissions — the AI never writes back to source systems
- Outputs go to a separate system (e.g., separate Obsidian vault, Notion, text files) for human review
- The limitation is fully intentional, not a temporary constraint
- Asymmetric risk profile: downside of a read-only error is zero (just ignore it); downside of a write error is unbounded
- Produces better analysis because the exhaust fumes remain uncontaminated — you observe your own cognition, not a human-AI hybrid
- The feedback loop is mediated by the human: you read the reflection, you decide what to do
- Contrasts with the industry obsession with agents that act on your behalf
- The observer produces more value per interaction than the agent: "The agent saves me 30 seconds on a weather check. The observer shows me I've been avoiding my most important project for 2 weeks"
- Observers and agents are different tools serving different needs — "a mirror isn't a broken butler"

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[ŠimonPodhajský]] — advocate
- [[Fulan]] — reference implementation
- [[CognitiveExhaustFumes]] — what read-only AI analyzes
- [[CognitivePollution]] — what read-only AI avoids
- [[ObserverVsAgent]] — the core distinction
- [[LethalTriquetra]] — security model that read-only partially mitigates
- [[MosaicEffect]] — security risk that read-only systems must still contend with
