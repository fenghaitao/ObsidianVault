---
title: "summary-03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino"
type: source
tags: [source, original-material, podcast, openai, codex, product-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino.md"]
last_updated: 2026-07-10
---

## Core Summary

Andrew Ambrosino, product and engineering lead for the [[Codex]] app at [[OpenAI]], discusses how AI has inverted the traditional product-development process: because implementation (writing code/prototypes) has become nearly free, the scarce resource is now curation and judgment — what he and others call "[[Taste]]." Rather than de-risking ideas through documents and research before building (the old, implementation-is-expensive model), teams at OpenAI now let dozens of uncoordinated people prototype the same feature simultaneously, and the hard work is choosing what to keep, refine, and ship. This shift is also collapsing traditional functional boundaries between product, design, and engineering — Ambrosino argues people are now defined by "the average of where they're working" rather than a fixed role, a phenomenon he calls "[[Role Collapse]]," while cautioning against fully eliminating specialized roles and best practices. He describes organizing product coverage via a "[[Zone Defense]]" analogy, in which product-minded people spread out to cover different areas rather than clustering, since curation and steering — not implementation — is now the bottleneck. The episode also covers the history and trajectory of the Codex app (from a CLI, to a developer-only desktop app, to browser/computer-use features, to merging with [[ChatGPT]] into a general knowledge-work "super app"), the practice of aggressive internal [[Dogfooding]], the necessity of shipping features repeatedly as underlying models improve (citing [[Operator]] and [[Atlas]] as earlier, too-early attempts at agentic browsing that Codex later succeeded at), and why AI still struggles with visual/product design (harder to grade than code, requires novelty rather than pattern-matching, and needs a deeper semantic/abstraction layer between design intent and code).

## Key Points

- Implementation is no longer the expensive part of building software; curation, judgment, and "taste" are now the scarce resource, inverting the traditional research → derisk → prototype → build pipeline.
- OpenAI is merging Codex (originally a developer-focused coding agent/app) with ChatGPT into a single general-purpose knowledge-work "home base" app, because users refused to leave Codex for the other, allegedly-more-general surfaces built for non-engineers.
- Traditional functional roles (PM, designer, engineer) are collapsing into "role fluidity" — people are defined by the average of the work they do, not a fixed job title — but Ambrosino warns against fully abolishing roles/specialties, since that risks discarding real, hard-won best practices.
- "Zone defense" is Ambrosino's analogy for how product people should organize now: spread out to cover distinct areas of the problem space, rather than clustering on the same idea, since curation/steering capacity (not build capacity) is the limiting factor.
- Nearly 100% of OpenAI employees use Codex weekly (not just engineers); usage has grown 6x since January with 5M+ weekly active users.
- AI is still weak at visual/product design relative to code, for practical reasons (design is harder to grade / lacks a clean training signal like "does the code compile") and harder structural reasons (design rewards novelty rather than pattern conformity, and there's a missing semantic/abstraction layer connecting visual design to the underlying code architecture).
- Product timing matters enormously: the same Codex app shape shipped in February succeeded, but Ambrosino believes it would have failed if released in November — only the underlying model capability changed. Teams should build ambitious features "too early" and let them "wait for the model to catch up" rather than judging the feature concept as failed.
- Internal culture of heavy, continuous dogfooding (the "dogfooding loop") drives the roadmap — the team builds features by using its own unfinished product and fixing what's broken, even when this makes their own process less efficient in the short term.
- The design process ("user research → divergence → convergence") isn't dead but has to be decoupled from specific mediums/tools; prototypes and PRDs are both still useful depending on whether the goal is product clarity (favor documents) or testing an interaction (favor a prototype).
- Anecdote: an in-house videographer (Brent) used Codex to edit Adobe Premiere Pro video files directly, and Codex ultimately built its own Premiere Pro extension to accomplish tasks it couldn't do by file-editing alone — illustrating a general pattern of AI agents integrating with existing specialty tools rather than replacing them outright.

## Related

- [[Andrew Ambrosino]] — podcast guest, product/engineering lead for Codex
- [[OpenAI]] — company building Codex and ChatGPT
- [[Codex]] — the product at the center of the discussion
- [[ChatGPT]] — the app Codex is merging into
- [[Atlas]] — OpenAI's browser, referenced as an earlier agentic-browsing attempt
- [[Operator]] — earlier ChatGPT agent feature, referenced as a too-early attempt
- [[Lenny's Podcast]] — the podcast/show this transcript is from
- [[Taste]] — central concept: curation/judgment as the new bottleneck
- [[Role Collapse]] — collapsing boundaries between PM/design/engineering roles
- [[Zone Defense]] — Ambrosino's product-org coverage analogy
- [[Dogfooding]] — internal usage-driven development practice at Codex
- [[Design Process]] — discussion of whether the traditional design process is "dead"
- [[Member Of Technical Staff]] — job-title convention discussed as a sign of role fluidity
