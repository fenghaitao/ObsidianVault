---
title: "StrongDM"
type: entity
tags: [company, security, AI, dark-factory, access-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

StrongDM is a security software company specializing in access management (granting/revoking access to tools like Jira, Slack, Okta for employees). They became notable in the AI community for pioneering the "dark factory" software development pattern, where they adopted a policy of both nobody writing code and nobody reading code, relying instead on automated AI testing and QA.

## Key Information

- Security software for access management — "not the kind of thing that you should be vibe coding at all"
- Pioneered the "dark factory" pattern starting in August 2025
- Two rules: (1) Nobody writes any code (all code must be AI-written). (2) Nobody reads the code.
- Created a simulated QA swarm: AI agents simulated thousands of end users making requests 24/7 in a simulated Slack channel
- Spent ~$10,000/day on tokens for AI-simulated testing
- Built simulated versions of Slack, Jira, Okta, and other APIs from public documentation — creating small Go binaries that cost nothing to run
- The simulated Slack even had a fake UI that they could use to observe what was happening
- Simon Wilson attended their demo in October 2025 and cited them as a fascinating example of "thinking outside the box" for AI-driven development

## Related

- [[Dark Factory]] — the software development pattern they pioneered
- [[Simon Wilson]] — cited StrongDM as a case study
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
