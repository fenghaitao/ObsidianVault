---
title: "Dark Factory"
type: concept
tags: [AI, software-engineering, automation, testing, QA]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

The dark factory (or software factory) is a software development pattern where nobody writes code and nobody reads code. Instead, AI agents generate all code and automated testing (simulated QA swarms, security penetration testing, etc.) ensures quality. The name comes from factory automation: if your factory is so automated that you don't need people, you can turn the lights off.

## Key Information

- Named after factory automation where machines operate without human presence: "if your factory is so automated that you don't need any people there, you can turn the lights off"
- Two rules: (1) Nobody writes any code — all code must be AI-written. (2) Nobody reads the code.
- **StrongDM** pioneered this pattern starting August 2025:
  - Created a simulated QA swarm: AI agents simulated thousands of end users making requests 24/7 in a simulated Slack channel
  - Spent ~$10,000/day on tokens for AI-simulated testing
  - Built simulated versions of Slack, Jira, Okta, and other APIs from public documentation (small Go binaries, cost nothing to run)
  - The simulated Slack even had a fake UI for observation
- The key question: "How do you produce software that works and is good if you're not reading the code?"
- Answers include: better automated testing, AI-driven security penetration testing, and creative QA approaches
- Simon Wilson considers this "the next barrier" — "that's futuristic. We're trying to figure out what that looks like and how we can responsibly build software in that way right now"

## Related

- [[StrongDM]] — the company pioneering this pattern
- [[Agentic Engineering]] — the precursor to dark factory (where you still review code)
- [[YOLO Mode]] — the unsafe agent mode that enables dark factory workflows
- [[Simon Wilson]] — discussed this concept on Lenny's Podcast
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
