---
title: "Dark Factory Pattern"
type: concept
tags: [ai, software-engineering, automation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s term (also "software factory") for a stage of AI-assisted software development beyond "[[Agentic Engineering]]": nobody writes the code, and nobody reads the code either — yet professional quality practices and expectations still apply, unlike careless "vibe coding." Named by analogy to factory automation so complete that the factory floor can run with the lights off, since no humans need to be physically present.

## Key Information

- Central case study: [[StrongDM]] (a security/access-management company) adopted a two-rule policy — nobody types code (all written by AI, already common practice) and nobody reads the code (the newer, harder rule) — and had to invent ways to validate quality without code review.
- StrongDM's solution: replacing a human QA department with a 24/7 swarm of simulated end-users (bots posting realistic Slack messages like "can someone give me access to Jira?") — hitting a simulated version of Slack/Jira/Okta that StrongDM built itself from public API docs and open-source client libraries, since real services rate-limit high-volume automated testing. Reportedly cost ~$10,000/day in tokens.
- Raises open questions beyond functional QA: passing a simulated-user test doesn't guarantee security or other non-functional qualities — Willison notes AI agents have separately become credible security researchers in the same period (e.g., Anthropic's internal security models reportedly found ~100 real vulnerabilities in Firefox, verified and responsibly disclosed to Mozilla).
- Framed by Willison as the current frontier/open problem in agentic engineering — actively being explored, not yet solved or common practice.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — describes this pattern
- [[StrongDM]] — central case study
- [[Agentic Engineering]] — the preceding, more conservative stage this goes beyond
- [[Firefox]] — case study for AI-driven security research quality
