---
title: "Chatter Driven Development"
type: concept
tags: [ai-agent, software-development, coining]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue.md"]
last_updated: 2026-07-12
---

## Definition

"Chatter driven development" is a half-joking term coined on the spot by [[Alexander Imbiricos]] (Codex product lead, [[OpenAI]]): an alternative to spec-driven or plan-driven development where an AI agent simply monitors a team's communication channels (Slack, customer-support tickets) and writes/ships small fixes reactively, without a human first producing a formal spec.

## Key Information

- Positioned as a lighter-weight counterpart to "spec-driven development"/"plan-driven development" (writing a plan.md before delegating a long task to [[Codex]]) — useful for small, low-stakes fixes where writing a spec would be overkill, not a wholesale replacement for planning on larger tasks.
- [[Lenny Rachitsky]] connects this directly to a real-world precedent from a separate interview with [[Dhanji Prasanna]] (CTO of Block): an engineer there has Block's internal agent, "[[Goose]]," watch his screen and listen to meetings all day, proactively shipping PRs, sending emails, and drafting Slack messages based on what it observes.
- Imbiricos frames the near-term bottleneck to this kind of proactive workflow as not the agent's ability to act, but the human review/validation step required afterward — tying back to his broader "[[Human Typing Speed As Bottleneck|human review speed]]" argument.

## Related

- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue]] — source summary
- [[Alexander Imbiricos]] — coined this term
- [[Codex]] — the agent this concept applies to at OpenAI
- [[Goose]] / [[Dhanji Prasanna]] — real-world precedent cited by Lenny Rachitsky
- [[Human Typing Speed As Bottleneck]] — related constraint on this workflow
