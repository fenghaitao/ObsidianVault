---
title: "Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Cognitive Exhaust Fumes, or： Read-Only AI Is Underrated — Šimon Podhajský, Head of AI, Waypoint.md"
author: "Šimon Podhajský"
date: 2026-04-08
ingested: 2026-06-26
---

## Core Thesis

Šimon Podhajský argues that read-only AI systems — which observe and reflect on your digital activity without ever writing back — are an underrated and distinct product category from agentic AI. He presents Fulan, a personal AI system that ingests six read-only data sources to produce cross-source insights about intention-action gaps, attention drift, and relationship decay, while avoiding the asymmetric risks of write-capable agents.

## Key Points

- **Cognitive exhaust fumes**: Digital activity that is a byproduct of cognition — individually waste, but collectively diagnostic of how you think and operate
- **Cross-source signal**: The value comes from combining data across disconnected sources (email, journal, browser, task manager, CRM) that were never designed to talk to each other
- **Three top use cases**: Intention-action gaps (what you said you'd do vs. what you did), attention drift (where your focus actually goes), and relationship decay (who you've been neglecting)
- **Read-only architecture**: Six sources with read access only, no write permissions — the AI never writes back to source systems
- **Output to separate vault**: Analysis results land in a separate Obsidian vault (or any separate system) for human review
- **Weekly reflection demo**: A Claude skill that launches a Python script, pings the Anthropic API, and produces a markdown reflection on how you spent your week — not a productivity report, but a reflection on how you're thinking
- **Cross-source query demo**: Given recent reading (from Vivaldi browser SQLite), the system identifies people in your network (via Clay CRM) who might be interested in discussing those articles
- **Asymmetric risk**: The downside of a read-only error is zero (just ignore it); the downside of a write error is unbounded — personal AI operates in high-stakes environments (relationships, career, reputation)
- **Cognitive pollution**: When AI writes to your data sources, the exhaust fumes are contaminated — you're observing a human-AI hybrid, not your own cognition
- **Observer vs. agent**: Observers and agents are different tools serving different needs; read-only isn't a stepping stone to "real" agents
- **Security concerns**: The mosaic effect (combining small pieces of information to reveal a larger picture) makes the system a devastating target; Simon Willison's lethal triquetra (private data + untrusted content + external communications) is partially but not fully mitigated
- **Philosophical stance**: Read-only produces better analysis because the feedback loop is mediated by the human, not automated

## Entities Mentioned

- [[ŠimonPodhajský]] — Head of AI at Waypoint, creator of Fulan
- [[Waypoint]] — Company where Šimon Podhajský works
- [[Fulan]] — Read-only personal AI system built by Šimon Podhajský
- [[Anthropic]] — AI company whose Claude models and API power the system
- [[ClaudeCode]] — Anthropic's coding agent used to run the weekly reflection and cross-source queries
- [[Cursor]] — AI-powered code editor used to preview analysis outputs
- [[Clay]] — CRM/friend relationship management tool used for contact data
- [[Vivaldi]] — Browser whose SQLite database stores reading history for cross-source queries
- [[Obsidian]] — Note-taking app used as the separate output vault for AI-generated reflections
- [[DavidAllen]] — Author of Getting Things Done (GTD), whose weekly review methodology inspired the reflection feature
- [[SimonWillison]] — Creator of the lethal triquetra security risk model

## Concepts Introduced

- [[CognitiveExhaustFumes]] — Digital activity as a byproduct of cognition; individually waste, collectively diagnostic
- [[ReadOnlyAI]] — AI systems with read-only access that observe and reflect without writing back
- [[MosaicEffect]] — Security risk where combining many small pieces of information reveals a larger, sensitive picture
- [[LethalTriquetra]] — Simon Willison's security model: private data + untrusted content + external communications
- [[CognitivePollution]] — Contamination of digital exhaust when AI writes to your data sources, obscuring your own patterns
- [[CrossSourceSignal]] — Insights derived from combining data across multiple disconnected sources
- [[IntentionActionGaps]] — Discrepancies between what you intend to do and what you actually do
- [[AttentionDrift]] — How your focus shifts over time, revealed by digital exhaust analysis
- [[RelationshipDecay]] — Deterioration of relationships when not maintained, detectable via cross-source analysis
- [[ObserverVsAgent]] — Distinction between AI that observes/reflects and AI that acts on your behalf

## Related

- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — contrasting agentic AI perspective
- [[summary-20251222 - No More Slop – swyx]] — also discusses Anthropic and Claude capabilities
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — related Claude tooling
