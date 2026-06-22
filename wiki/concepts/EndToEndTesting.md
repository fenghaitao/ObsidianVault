---
title: "EndToEndTesting"
type: concept
tags: [testing, qa, quality]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260414 - We build fast. But does it work.md]
last_updated: 2026-06-22
---

## Definition

End-to-end (E2E) testing is the final layer of quality assurance that verifies real users can complete critical flows in an application without hitting errors. In the AI era, it's the layer that catches what unit tests and integration tests miss — the gap between "tests pass in CI" and "users can actually use the app."

## Key Information

- QA testing is the new bottleneck: shipping fast only matters if what you ship actually works.
- Confidence comes from stacking layers: unit tests (agents write in code) + integration tests + end-to-end tests.
- Each layer catches what others miss.
- Tools like [[KainAI]] let non-technical team members build E2E tests by clicking through the app.
- Key capabilities: auto-detect user actions, secrets for credentials, video playback of test runs, CI integration.
- When tests fail, auto-create issues in Linear/Jira/GitHub for agents or team to fix.

## Related

- [[KainAI]] — a tool for E2E testing
- [[SpecDrivenDevelopment]] — the methodology
- [[VerificationCriteria]] — complementary pattern
- [[VercelAgentBrowser]] — Cole Medin's browser-automation testing tool
- [[BrianCasel]] — advocate
