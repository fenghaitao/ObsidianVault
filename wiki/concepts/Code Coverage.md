---
title: "Code Coverage"
type: concept
tags: [testing, code-quality, metrics, anti-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Code coverage is a metric measuring what percentage of code is exercised by tests. While useful as a signal, over-indexing on code coverage can lead to testing implementation details rather than system behavior, and AI-generated tests can achieve high coverage without validating actual functionality.

## Key Information
- Measures how much code is exercised by the test suite
- Over-indexing on code coverage has several issues:
  - Tendency to test implementation details (method names, internal structure)
  - Tests break on refactors even when functionality is correct
  - AI can generate self-affirming tests that achieve high coverage without validating behavior
- DHH (Rails creator) criticized TDD's overfocus on code coverage in his 2014 "TDD is dead" post
- Better approach: test behavior (final end results) or stable contracts (APIs, exported modules) that survive internal refactors
- Ian Cooper's talk "TDD Where It All Went Wrong" explores how TDD drifted from behavioral testing to code coverage obsession
- Code coverage is a useful signal but should not be the primary goal of testing

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[Functionality Testing]] — preferred alternative approach
- [[SelfAffirming Tests]] — AI-generated coverage without behavioral validation
- [[AIGenerated Tests]] — risk of misleading coverage
- [[DHH]] — critic of code coverage focus
- [[Ian Cooper]] — "TDD Where It All Went Wrong" author
- [[RedGreen TDD]] — methodology that prioritizes behavior over coverage
- [[TDD with AI]] — broader methodology
