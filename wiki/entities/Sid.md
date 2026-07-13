---
title: "Sid"
type: entity
tags: [person, anthropic, engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md"]
last_updated: 2026-07-11
---

## Definition

[[Anthropic]] team member credited by [[Cat Wu]] with adding [[Claude Code]]'s original to-do-list feature, modeled on how a human would track a large multi-step refactor (similar to a "find all references" list in an IDE).

## Key Information

- Built the feature to solve an early-model failure mode: Claude Code would start a large refactor (e.g., 20 call sites to change), do a handful, and stop without finishing. The to-do list gave the model an explicit checklist to track and complete.
- Per Cat Wu, this scaffolding became progressively less necessary as models improved (Opus 4 and later versions began completing checklists without needing reminders), illustrating [[Building Blocks Progression]] and [[AGI Pilled]] in practice.

## Related

- [[summary-13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary
- [[Cat Wu]] — credits him with this feature
- [[Claude Code]] — product this feature was built for
- [[Building Blocks Progression]] — concept this example illustrates
