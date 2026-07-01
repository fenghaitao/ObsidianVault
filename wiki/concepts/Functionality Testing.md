---
title: "Functionality Testing"
type: concept
tags: [testing, tdd, playwright, behavioral-testing, code-quality, ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Functionality testing is a testing approach that validates the actual behavior of a system from the user's perspective, as opposed to code coverage-focused unit testing that validates implementation details. With AI tools like Playwright MCP, functionality tests can be generated and run by coding agents, enabling a workflow where AI handles test creation and execution while developers focus on code quality.

## Key Information
- Tests the system's behavior and end results, not internal implementation details
- Contrasts with code coverage-focused unit testing: a test tied to a method name like `calculate` breaks on rename even if functionality is fine
- Better approaches: test behavior (final end result) or stable contracts (API, exported modules) that survive internal refactors
- AI enables functionality testing at scale: agents write Playwright tests that simulate real user interactions (clicking, typing, navigating, filtering)
- Trigger shifts from "new method added to a class" (traditional unit test trigger) to "new feature request received" (behavioral trigger)
- Playwright screenshots from test runs provide visual evidence of correct behavior
- Recommended: one test per feature, not one test per method
- For non-browser scenarios, API testing is a valid alternative to browser-based functionality testing

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[Playwright]] — testing framework
- [[Playwright MCP]] — MCP server integration
- [[Code Coverage]] — contrasting approach
- [[SelfAffirming Tests]] — problem with coverage-focused AI tests
- [[RedGreen TDD]] — TDD flavor focused on behavior
- [[TDD with AI]] — methodology
- [[Marlene Mhangami]] — speaker
- [[Ian Cooper]] — "TDD Where It All Went Wrong" author
- [[BrowserBased Autonomous Testing]] — related approach
