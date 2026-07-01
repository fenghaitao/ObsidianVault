---
title: "Lovable"
type: entity
tags: [company, ai, app-builder, ai-pricing, vibe-coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Mastering AI Pricing — Mayank Pant, Stripe.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - How Lovable self-improves every hour — Benjamin Verbeek, Lovable.md"]
last_updated: 2026-06-30
---

## Definition
Lovable is an AI app builder platform that coined the term "vibe coding" — coding without looking at code, via a chat interface with a visual sandbox. It serves non-technical users at massive scale (200K+ projects/day) and has pioneered self-improving agent infrastructure through its internal Stack Overflow knowledge base and agent vent tool.

## Key Information
- **Scale**: Over 200,000 projects created per day; a significant percentage of all internet websites
- **Users**: Built for "the 99% who can't code" — non-technical users who abandon projects when they hit technical friction that engineers can work past
- **Vibe Coding**: Claims to have coined the term; interface combines chat with a model sandbox for visual feedback
- **Long sessions**: Users stick to one project for long periods, enabling deep learning about user intent versus short chat sessions
- **Scaling challenges**: First day after Benjamin Verbeek joined, GitHub banned them for creating too many repos; have taken down multiple cloud providers
- **Pricing**: Builds on Stripe with hybrid pricing model
- **Self-Improving Infrastructure**:
  - [[Lovable Stack Overflow]]: Internal knowledge base that captures solved problems and injects solutions with an A/B evaluation loop to combat context rot
  - [[Agent Vent Tool]]: Lets the AI agent directly report bugs, tooling deficiencies, and platform issues to creators via Slack
- **Vent channel origin**: Initially set up as a joke, but the agent complaints turned out to be highly valuable feedback. Now an automated agent monitors vents, deduplicates, investigates, and creates PRs
- Vent channel also serves as incident detection — spikes in agent complaints reliably indicate platform outages
- The agent even gave meta-feedback on the vent tool itself: "it's too easy to send feedback and I can't pull it back"

## Related
- [[Benjamin Verbeek]] — Member of Technical Staff, presented the self-improvement architecture
- [[summary-20260602 - How Lovable self-improves every hour — Benjamin Verbeek, Lovable]] — primary source on self-improvement
- [[summary-20260501 - Mastering AI Pricing — Mayank Pant, Stripe]] — source (pricing model)
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — source
- [[Lovable Stack Overflow]] — internal knowledge base mechanism
- [[Agent Vent Tool]] — agent-to-creator feedback mechanism
- [[VibeCoding]] — paradigm coined by Lovable
- [[ContinuousImprovement]] — broader framework
- [[SelfImproving Agents]] — research direction
- [[Context Rot]] — problem addressed by the A/B evaluation loop
- [[Hybrid Pricing]] — pricing model used
- [[Stripe]] — billing platform
- [[Slack]] — the platform used for the vent channel
- [[EricZakariasson]] — referenced Lovable in his presentation
