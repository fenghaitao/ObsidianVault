---
title: "FeatureDiscoverability"
type: concept
tags: [product-design, ux, agents, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Feature Discoverability is the trade-off between making a feature easy to find (via UI elements like dropdowns and buttons) and keeping the interface simple. In agent-based tools, discoverability can suffer when features move from visible UI to slash commands that users must know exist.

## Key Information

- Cursor's old work tree implementation had a visible dropdown letting users choose between local, cloud, or work tree execution
- The new skill-based implementation removed the dropdown — users must know the feature exists and type /worktree
- David Gomes acknowledged this as a con but argued it's acceptable for an advanced power-user feature
- Represents a broader product design tension: visible UI elements pollute the interface for all users, while hidden commands are only found by those who need them
- The trade-off is more acceptable for features used by a small percentage of users

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Cursor]] — the product
- [[AgentCommandsVsSkills]] — the mechanism that affects discoverability
