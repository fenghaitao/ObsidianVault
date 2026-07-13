---
title: "Contextual Actions"
type: concept
tags: [ux, ai-agent, mixed-initiative]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue.md"]
last_updated: 2026-07-12
---

## Definition

A UX concept, explicitly borrowed by [[Alexander Imbiricos]] (Codex product lead, [[OpenAI]]) from video-game design (his example: pressing a single context-sensitive action button in a game like Halo, which does "the right thing" depending on what you're near): an AI agent should be able to proactively surface a specific, relevant action at the moment it's useful, rather than requiring the user to explicitly invoke it or bombarding them with generic notifications.

## Key Information

- Central rationale for building [[Atlas]] (OpenAI's browser): being inside the browser's rendering engine gives an agent first-class, reliable context about what a user is doing on the web — far better than hacking OS accessibility APIs (inconsistent support across desktop software) or relying on screenshots (slower, less reliable) — enabling genuinely useful contextual actions rather than guesses.
- Imbiricos's stated alternative failure mode: if an agent can only communicate that it helped via push notifications, users would get "a thousand push notifications a day of an AI saying 'hey, I did this thing, do you like it?'" — annoying and unsustainable at the scale of thousands of potential daily interventions.
- Paired with clear user-controlled boundaries: a user chooses whether to open something in the AI-aware browser (inviting agent help) or a different browser (opting out), rather than the agent acting on everything indiscriminately.
- Connected to Imbiricos's broader product philosophy of making AI "maximally accelerating" without requiring the user to constantly think about when/how to invoke it (see [[Codex]]).

## Related

- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue]] — source summary
- [[Alexander Imbiricos]] — originator of this application of the concept
- [[Atlas]] — product built around this design philosophy
- [[Codex]] — related "maximally accelerating" product philosophy
