---
title: "Self-Affirming Tests"
type: concept
tags: [testing, ai, code-coverage, code-quality, anti-pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Self-affirming tests are AI-generated tests that pass and achieve high code coverage but fail to validate the actual behavior of the system. They are a known pitfall of using AI to generate tests without behavioral validation, where the test suite is green but the application's functionality is not actually verified.

## Key Information
- AI can generate tests that achieve passing code coverage without validating system behavior
- The test suite appears healthy (all green) but provides false confidence
- Related to the broader problem of over-indexing on code coverage metrics
- Contrast with functionality testing: tests should validate what the system does, not just that code paths are exercised
- Marlene Mhangami identifies this as a key risk when developers use AI to generate tests without a behavioral testing approach
- Solution: use Playwright or similar tools to write behavioral tests that simulate real user interactions and verify end results
- Can be prevented by using TDD: write the failing behavioral test first, then generate code to pass it

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[Functionality Testing]] — solution approach
- [[Code Coverage]] — the metric that can be misleading
- [[AIGenerated Tests]] — broader category
- [[TDD with AI]] — methodology that prevents this problem
- [[RedGreen TDD]] — write failing test first to avoid self-affirmation
- [[Marlene Mhangami]] — speaker who identified the risk
