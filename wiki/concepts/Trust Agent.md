---
title: "Trust Agent"
type: concept
tags: [AI, agent, trust, safety, linkedin]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/41 - Why AI is disrupting traditional product management ｜ Tomer Cohen (LinkedIn CPO).md"]
last_updated: 2026-07-10
---

## Definition

A trust agent is an AI agent built at LinkedIn that evaluates product specs and ideas for trust vulnerabilities, harm vectors, and safety risks specific to the LinkedIn platform.

## Key Information

- Built by LinkedIn's head of trust, reflecting the principle that domain experts should build their own agents.
- When a builder creates a spec or idea, the trust agent evaluates it and identifies vulnerabilities and potential harm vectors.
- Retroactively tested on the "Open to Work" feature spec: it found all originally identified issues plus additional holes that were only caught later in production.
- Trust is particularly important at LinkedIn due to unique vectors (e.g., job seekers being more vulnerable to scams).
- The trust agent is designed to work with other agents (e.g., growth agent) via the orchestrator layer.
- This is an example of an agent that cannot be purchased off-the-shelf because LinkedIn's trust vectors are unique to its platform.

## Related

- [[summary-41 - Why AI is disrupting traditional product management ｜ Tomer Cohen (LinkedIn CPO)]] — source summary
- [[Agent Orchestration]] — coordination framework
- [[Growth Agent]] — complementary agent
- [[Full-Stack Builder Model]] — parent concept
