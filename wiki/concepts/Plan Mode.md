---
title: "Plan Mode"
type: concept
tags: [claude-code, product-feature, ai]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

[[Claude Code]] feature that instructs the model not to write any code yet, letting it discuss and refine an approach with the user first; [[Boris Cherny]] starts roughly 80% of his own tasks this way.

## Key Information

- Implementation is deliberately simple: per Cherny, it's just one injected sentence telling the model to hold off on writing code — "there's actually like nothing fancy going on."
- Activated via shift-tab-twice in the terminal, a button in the desktop and web apps, and (recently) the Slack integration; coming soon to mobile.
- Cherny's workflow: iterate in plan mode until the plan looks right, then let the model execute with auto-accepted edits — with Opus 4.6, a good plan is usually "one-shotted" correctly on the first execution pass.

## Related

- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Boris Cherny]] — primary user/advocate
- [[Claude Code]] — product this feature belongs to
