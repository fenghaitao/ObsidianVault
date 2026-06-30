---
title: "VibesBasedSafety"
type: concept
tags: [agents, safety, prompt-engineering, trust]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Vibes-based safety is a semi-ironic term for relying on prompt instructions rather than mechanical enforcement to constrain agent behavior. Instead of physically preventing an agent from doing something dangerous, you trust the model to follow instructions — "knock on wood, please don't forget about this."

## Key Information

- Coined or popularized by David Gomes in the context of Cursor's work tree isolation
- Contrasts with the old approach where "it was physically impossible" for the agent to touch files outside its work tree
- The new approach says "operate on this directory" and hopes the model complies
- Particularly unreliable over long sessions and with weaker models
- Cursor is working to improve reliability through evals, prompt improvements, and RL training
- Represents a broader trade-off in agent design: less infrastructure code vs. less guaranteed safety

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[AgentIsolation]] — the safety property being enforced
- [[MarkdownAsCode]] — the paradigm that enables this approach
- [[Cursor]] — the product
