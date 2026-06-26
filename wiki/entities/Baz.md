---
title: "Baz"
type: entity
tags: [company, ai-code-review, developer-tools, agentic]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
Baz (stylized as "Buzz" in the transcript) is a company building AI-powered code reviewers and other agentic developer tools aimed at improving R&D productivity for developers, PMs, and other technical roles.

## Key Information
- Founded in 2023.
- Core product is an AI-powered code reviewer that has been under development for several years.
- The "spec reviewer" is one of their products: an agentic reviewer that compares requirements (from tickets and Figma designs) against actual implementations.
- The spec reviewer collects requirements from ticketing systems (Jira, Linear), reads Figma designs multimodally, then uses Playwright's MCP server to open a browser and verify implementations against requirements.
- The spec reviewer produces pass/fail verdicts with screenshot evidence, saving PMs significant time on manual validation work.
- Nimrod Hauser is a founding engineer.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[NimrodHauser]] — founding engineer
- [[Playwright]] — MCP server used for browser automation
- [[ThirdPartyToolOptimization]] — framework presented using Baz's spec reviewer as a case study
