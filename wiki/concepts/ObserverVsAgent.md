---
title: "ObserverVsAgent"
type: concept
tags: [ai, design-philosophy, product-categories]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md"]
last_updated: 2026-06-26
---

## Definition
Observer vs. agent is the distinction between AI systems that observe and reflect (read-only, providing insights for human decision) and AI systems that act on behalf of the user (agentic, executing tasks autonomously). Šimon Podhajský argues these are fundamentally different product categories, not a maturity spectrum.

## Key Information
- Core argument: observers and agents are different tools, not stages on a progression
- "The industry frames read-only as a limitation you graduate from. I think that's wrong."
- "A mirror isn't a broken butler" — observers serve a different need than agents
- Value comparison: "The agent saves me 30 seconds on a weather check. The observer shows me I've been avoiding my most important project for 2 weeks."
- The observer produces more value per interaction by a wide margin
- Observers have less risk of exfiltration and cognitive pollution
- The feedback loop in observer systems is mediated by the human: you read the reflection, you decide what to do
- In agent systems, the feedback loop is automated: the AI writes your draft, sends your email, schedules your meetings

## Related
- [[summary-20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint]] — source
- [[ReadOnlyAI]] — the observer category
- [[CognitivePollution]] — risk that agents introduce but observers avoid
- [[Fulan]] — reference implementation of an observer system
