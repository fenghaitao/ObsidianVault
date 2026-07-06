---
title: "summary-2026-04-29 - Product development in the agentic era"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-29 - Product development in the agentic era.md"]
last_updated: 2026-07-04
---

## Core Summary

Jess Yan, product manager for [[ClaudeManagedAgents|Claude Managed Agents]], describes how building with Claude has reshaped her PM workflow. Previously, API design lived in docs and comment threads; now she prototypes directly against pre-production API specs in [[ClaudeCode|Claude Code]], going from a "hello world" test to a working agent within a single sitting, and even litigating shapes with raw curl requests. This dogfooding surfaced abstraction and Claude Console UX problems that a multi-week doc review would have missed and user feedback would have caught too late. Her workflow now splits cleanly by product: [[Claude.ai|Claude]] and [[ClaudeCowork|Claude Cowork]] for open-ended, early-stage research and discovery (an ongoing conversation for murky problems), and Claude Code plus Managed Agents once she has clarity on the job to be done, to write and ship a custom agent. The payoff is two-sided — prototyping against her own product raises the ceiling on what she can imagine shipping, while the same muscle lets her automate the long-tail operational work that used to stall in her backlog. She frames this as a return to the "craft" of product management (partnering with users and engineers) rather than the "alignment" busywork (status reports, ticket backlogs, cross-functional advocacy) that used to dominate her week.

## Key Points

- Author: Jess Yan, Claude Managed Agents product manager. Published 2026-04-29 (Anthropic/Claude blog), last modified 2026-06-21.
- Central claim: building agents against her own team's pre-production API specs in Claude Code lets her validate designs "within an afternoon," catching problems a multi-week doc review or later user feedback would have missed.
- Workflow split: Claude / Claude Cowork → open-ended research and discovery (murky, early-stage, ongoing conversation); Claude Code + Managed Agents → writing and shipping a custom agent once the job to be done is clear.
- To build an agent, she "loads the Managed Agents skill in Claude Code" and sketches what she's looking for; after invocation, Claude builds the agent and explains its integration steps, letting her redirect as needed.
- Developers can start the same way with the built-in `claude-api` skill by prompting "start onboarding for managed agents in Claude API" — consistent with the `/claude-api managed-agents-onboard` subcommand already documented in [[ClaudeCodeSkills]].
- Managed Agents sessions run in the cloud, so she can walk away and return to completed work; this lets her automate "long tail" operational processes that previously couldn't scale due to per-launch quirks.
- Framing: PM work used to split into "craft" (the part that mattered) vs. "alignment" (meetings, status reports, ticket backlogs, advocacy); Claude workflows free up time for the former.
- Closing call to action: any PM who hasn't built an agent yet should start "this week" — framed as "a single prompt and a few API calls away."
- Anomaly: the article repeats its own opening sentence verbatim as both the description/dek and the first body paragraph (lines 13 and 15 of the raw source are identical) — appears to be a scraping/formatting artifact from the source page rather than intentional repetition. Also, the "Examples of these agents include:" line (raw line 35) is immediately followed by no actual list — the concrete examples were apparently dropped in scraping. No prompt-injection-style text was found in the raw file.

## Related

- [[ClaudeManagedAgents]] — the product Jess Yan builds and the platform she uses to build her own PM agents
- [[ClaudeCode]] — where she prototypes agents against pre-production API specs
- [[ClaudeCowork]] — used alongside Claude for open-ended research/discovery
- [[ClaudeCodeSkills]] — the `claude-api` skill and its `managed-agents-onboard` subcommand referenced here
- [[summary-2026-03-19 - Product management on the AI exponential]] — related PM-philosophy piece linked from this article
- [[AgenticCoding]] — the build-with-what-you-ship pattern this article illustrates
