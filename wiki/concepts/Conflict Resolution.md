---
title: "Conflict Resolution"
type: concept
tags: [context-engineering, data-governance, truth-resolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked.md"]
last_updated: 2026-06-30
---

## Definition

Conflict resolution in the context of context engines is the ability to detect and resolve conflicting signals across multiple data sources (code, documentation, Slack conversations, etc.) and determine what information represents the authoritative truth to provide to an AI agent.

## Key Information

- Conflicts arise naturally: source code may say one thing, a Slack conversation where the CTO says "that was implemented wrong" says another, and documentation says a third
- A context engine must detect these conflicts and weigh authority: the CTO's statement in Slack likely overrides stale code or docs
- Without conflict resolution, agents may pick whichever source they encounter first (satisfaction of search) and produce incorrect implementations
- Social graphs help with resolution: knowing the authority and role of the person making a statement helps determine truth weight
- Conflict resolution is described as a "tough problem" that is "not fully solved" — it remains an active area of development
- Related to data governance: the engine must respect permissions and never expose private conversations to unauthorized users

## Related

- [[summary-20260526 - Stop babysitting your agents... — Brandon Waselnuk, Unblocked]] — source
- [[ContextEngine]] — the system that performs conflict resolution
- [[Satisfaction of Search]] — failure mode that conflict resolution prevents
- [[Social Graph]] — helps determine authority weighting for conflict resolution
- [[Brandon Waselnuk]] — speaker who identified this as a key context engine challenge
