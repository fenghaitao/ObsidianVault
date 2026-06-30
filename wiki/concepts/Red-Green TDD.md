---
title: "Red-Green TDD"
type: concept
tags: [tdd, testing, ai, methodology, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Red-Green TDD is a specific flavor of test-driven development consisting of three phases: Red (write a failing test because the feature doesn't exist), Green (write code quickly to make the test pass, prioritizing speed over quality), and Refactor (improve code quality while keeping tests green). Simon Willison recently published about using this approach with AI coding agents.

## Key Information
- Three phases: Red → Green → Refactor
- **Red phase**: Write a failing test for the new feature. With AI, the agent writes behavioral tests (e.g., Playwright tests) that fail because the feature doesn't exist yet
- **Green phase**: Write code to make the test pass as fast as possible. Historically developers might copy from Stack Overflow; with AI, the agent generates the implementation code quickly
- **Refactor phase**: Focus entirely on code quality — refactoring the code that made the test pass to follow best practices. Marlene Mhangami recommends developers spend the most time here
- With AI agents, Red and Green phases become fast (agent-generated), allowing developers to invest more time in Refactoring
- Trigger for writing tests shifts from "new method" to "new feature request" — focusing on behavior rather than implementation
- Simon Willison recently published a blog post advocating this approach
- Contrasts with DHH's 2014 critique that TDD overfocuses on unit tests and code coverage rather than system behavior

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[TDD with AI]] — broader methodology
- [[SimonWillison]] — practitioner who published about it
- [[DHH]] — critic of traditional TDD (2014)
- [[Marlene Mhangami]] — speaker advocating this approach
- [[Functionality Testing]] — the type of tests written in the Red phase
- [[Self-Affirming Tests]] — problem avoided by writing tests first
- [[KentBeck]] — creator of TDD
- [[Ian Cooper]] — "TDD Where It All Went Wrong" author
