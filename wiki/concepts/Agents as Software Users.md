---
title: "Agents as Software Users"
type: concept
tags: [agents, software-consumption, api, cli, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md"]
last_updated: 2026-06-26
---

## Definition

Agents as Software Users is the observation that AI agents are becoming the primary consumers of software, replacing human users. Malte Ubl revealed that over 60% of page views on vercel.com were AI agents, and that usage is shifting from dashboard UIs to APIs and CLIs.

## Key Information

- Over 60% of page views on vercel.com in a 7-day period were AI agents (previously undisclosed data)
- Humans are now in the minority on Vercel's web properties
- Usage shift: from people clicking around in dashboards to API and CLI usage
- Implication for feature design: when proposing features, Malte now asks "What's the CLI? How do I automate this? How does an agent use this?"
- UI is now "something that's so cheap" — the real interface is programmatic
- Infrastructure implications: agent-written software must "just run" without developer oversight
- Requires different infrastructure: sandboxes, security models, agent-oriented deployment

## Related

- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source
- [[Vercel]] — company sharing the data
- [[Malte Ubl]] — shared the insight
- [[AgentHarnessSeparation]] — related architectural principle
- [[Sandboxing]] — required infrastructure shift
