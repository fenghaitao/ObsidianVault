---
title: "AI-Generated Tests"
type: concept
tags: [testing, ai, code-generation, code-quality, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
AI-generated tests are test cases written by AI coding agents rather than human developers. While AI is highly capable at writing test code (especially with frameworks like Playwright), it carries the risk of producing self-affirming tests that achieve code coverage without validating actual system behavior.

## Key Information
- AI is particularly effective at generating Playwright tests because LLMs are highly capable at writing Playwright code
- Risk: AI can generate self-affirming tests — tests that pass and achieve code coverage but don't validate actual behavior
- Mitigation: use TDD (write failing test first) so the agent must write the test before the implementation, preventing it from "cheating"
- Mitigation: use behavioral/functionality tests (Playwright) rather than unit tests tied to implementation details
- Playwright Agents include a "healer" agent.md file specifically designed to fix failing tests automatically
- Best practice: commit code before the agent starts making changes, so state is preserved if the agent generates problematic tests
- Best practice: one test per feature, triggered by feature requests, not per method

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[Self-Affirming Tests]] — key risk
- [[TDD with AI]] — methodology that mitigates risks
- [[Red-Green TDD]] — write test first to prevent cheating
- [[Playwright]] — framework AI is good at generating tests for
- [[Playwright Agents]] — includes healer for fixing tests
- [[Code Coverage]] — metric that can be misleading with AI tests
- [[Functionality Testing]] — preferred approach
