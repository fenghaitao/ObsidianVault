---
title: "StrongDM"
type: entity
tags: [company, security, ai-adopter]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

Security/access-management company (builds software for provisioning employee access to tools like Jira and Slack) that pioneered the "[[Dark Factory Pattern]]" — a policy where employees neither write nor read code, with quality instead verified by a swarm of simulated end-users.

## Key Information

- Adopted a strict "nobody reads the code" policy starting around August of the prior year; built a swarm of AI agents simulating employees making realistic access requests in a simulated Slack channel, running 24/7 (reportedly ~$10,000/day in token costs).
- Built its own simulated versions of Slack, Jira, and Okta (from public API docs and open-source client libraries) specifically because testing against the real services at that volume would hit rate limits.
- Presented this approach in a public demo [[Simon Willison]] attended in October.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — describes this company's approach
- [[Dark Factory Pattern]] — concept this company pioneered
