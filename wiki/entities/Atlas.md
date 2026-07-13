---
title: "Atlas"
type: entity
tags: [product, openai, browser, agent]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue.md"]
last_updated: 2026-07-12
---

## Definition

Atlas is [[OpenAI]]'s browser product. In this source it is referenced as one of the earlier surfaces OpenAI used to experiment with agentic browsing, and as the origin of the "owl" stack that later powered [[Codex]]'s in-app browser.

## Key Information

- Had an agent working inside it at one point — described by Andrew Ambrosino as "pretty cool" but part of a lineage of agentic-browsing attempts (alongside [[Operator]] and Codex's in-app browser) that only fully succeeded once underlying models improved enough.
- The "owl" stack that powers Atlas was later adopted to upgrade Codex's in-app browser from a narrow, developer-only testing tool (limited by Electron's built-in browser capability) into a full multi-tab browser with enterprise login/security support.
- Was one of the surfaces OpenAI attempted to add Codex-style coding-agent capability to, as part of an effort to reach non-engineering personas — an effort that largely failed to draw users away from the Codex app itself.
- Per [[Sander Schulhoff]] (episode 37): after a [[Comet]] (Perplexity's AI browser) data-exfiltration bug caused by a malicious web page tricking the AI into leaking logged-in user data, Schulhoff notes this vulnerability class likely applies to Atlas too, and "probably all the AI browsers."
- Per [[Alexander Imbiricos]] (episode 39, who worked on Atlas before moving to lead [[Codex]] product): the rationale for building a dedicated browser was to get first-class, reliable contextual understanding of a user's in-browser activity — being inside the rendering engine directly, rather than hacking OS accessibility APIs (which have inconsistent support across desktop software) or relying on screenshots (slower, less reliable). This enables "contextual actions" (an idea borrowed explicitly from video-game UX, e.g. Halo's context-sensitive action button): the agent can proactively surface help exactly when relevant, instead of spamming push notifications, while giving users clear boundaries (open something in the AI browser if you want agent help on it; use a different browser if not).
- Heavy internal dogfooding by Atlas's own engineering team drove major acceleration: work that used to take 2-3 engineers 2-3 weeks reportedly now takes one engineer one week, per an engineer Imbiricos previously worked with at his pre-OpenAI startup. Shipped on Mac first; a Windows version was in active development at time of episode, requiring Codex itself to be upgraded with native PowerShell support to assist the porting effort.
- One engineer on the Atlas team set Codex up to validate its own work in a non-trivial way by directly prompting it, "why can't you verify your work? Fix it," in a loop — cited by Imbiricos as an example of configuring a coding agent toward greater autonomy on validation, not just code generation.

## Related

- [[summary-03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino]] — source summary
- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[OpenAI]] — company that builds Atlas
- [[Codex]] — adopted Atlas's "owl" browser stack
- [[Operator]] — related earlier agentic-browsing attempt
- [[ChatGPT]] — related surface in OpenAI's consolidation strategy
- [[Comet]] — comparable AI browser with a documented indirect prompt injection incident
- [[Sander Schulhoff]] — notes the shared vulnerability risk
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI’s biggest bottleneck, and why compute isn’t the issue]] — source summary
- [[Alexander Imbiricos]] — worked on Atlas before leading Codex product; explains the rationale for building it
- [[Contextual Actions]] — UX concept central to Atlas's design philosophy
