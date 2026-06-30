---
title: "summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft"
type: source
tags: [source, transcript, testing, playwright, mcp, tdd, microsoft, github, ai, functionality-testing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Core Summary
Marlene Mhangami (Senior Developer Advocate at Microsoft and GitHub, Core AI group) argues that as AI-generated code accelerates — from 1 billion commits in 2025 to a projected 14 billion in 2026 — maintaining clean code bases is critical for realizing AI productivity gains. She advocates for a modified TDD workflow using Playwright MCP for behavioral/functionality testing rather than code-coverage-focused unit tests. In this workflow, AI agents handle the red (write failing Playwright behavioral tests) and green (make tests pass quickly) phases, while developers focus on the refactoring phase. She demonstrates this using GitHub Copilot CLI with Playwright MCP server and Work IQ for M365 integration.

## Key Points

### The Code Growth Problem
- GitHub saw ~1 billion commits in 2025 (most active year ever)
- GitHub COO Kyle Daigle reported ~275 million commits per week in 2026, projecting ~14 billion by year end
- A growing share of commits are AI co-authored (Claude co-signs, Copilot co-signs, Codex does not)
- The core question: does more code mean more productivity?

### AI Productivity Depends on Clean Code Bases
- Referenced a Stanford University study of 120,000 developers presented at AI Engineer
- Key finding: clean code bases amplify AI gains; unchecked AI amplifies entropy
- Case study: a company used AI unchecked — PR count increased but code quality decreased, time spent on rework and refactoring increased, net productivity gain was only ~1%
- Clean code practices needed: good test coverage, type coverage, documentation, modularity
- Advocates for standardizing practices across teams and the industry

### Red-Green TDD with AI
- TDD was "pronounced dead" in 2014 by DHH (Rails creator) who criticized overfocus on unit tests and code coverage
- Simon Willison recently published about using red-green TDD
- Traditional TDD flow: feature request → write failing test (red) → make test pass quickly (green) → refactor for quality
- With AI: red and green phases become fast (agent-generated), developer spends most time on refactoring
- Trigger for writing tests shifts from "new method" to "new feature request" — focusing on behavior, not implementation

### Problems with Code Coverage
- Over-indexing on code coverage leads to testing implementation details
- Example: test tied to a method name like `calculate` breaks on rename even if functionality is fine
- Better to test behavior (final result) or stable contracts (API, exported modules)
- Recommended talk: Ian Cooper's "TDD Where It All Went Wrong"
- AI can generate self-affirming tests: tests that pass but don't validate actual system behavior

### Playwright for Functionality Testing
- Playwright: open-source testing framework by Microsoft for end-to-end browser testing
- Simulates user interactions (clicking, typing, navigating)
- Supports Python, TypeScript, C#, with headed and headless modes
- Three ways to connect coding agents to Playwright:
  1. **Playwright MCP Server** — MCP server for agent integration
  2. **CLI tool** — command-line interface
  3. **Playwright Agents** — installs three agent.md files: planner (plans which tests), generator (generates tests), healer (fixes tests)

### Demo: Tailspin Toys
- Scenario: developer at Tailspin Toys adding search bar (text search + Azure AI search) and category/price filter sidebar
- Used GitHub Copilot CLI with Work IQ (M365 skill for Outlook integration) to pull feature requirements
- Agent examined codebase, wrote failing Playwright tests for each feature
- Agent then generated code to pass tests (green phase)
- Playwright tests ran automatically: opened page, typed inputs, tested search bar, tested category filter, tested price range filter
- All tests passed — confirmed app behavior worked as expected

### Best Practices
- Add Playwright screenshots to PRs
- Run in headless mode for background execution
- Commit code before agent makes changes (preserve state)
- One test per feature (behavior-triggered, not method-triggered)
- For complex state management: use Playwright Agents (specialized agent.md instructions)
- For non-browser testing: test APIs directly

## Related
- [[Marlene Mhangami]] — speaker
- [[Microsoft]] — employer, Playwright creator
- [[GitHub]] — employer
- [[GitHubCopilot]] — tool used in demo
- [[Playwright]] — testing framework
- [[Playwright MCP]] — MCP server for Playwright
- [[Playwright Agents]] — planner/generator/healer agent files
- [[Work IQ]] — Microsoft M365 integration skill
- [[TDD with AI]] — methodology
- [[Red-Green TDD]] — specific TDD flavor
- [[Functionality Testing]] — testing beyond code coverage
- [[Self-Affirming Tests]] — AI-generated tests that don't validate behavior
- [[Code Coverage]] — limitations of coverage-focused testing
- [[Clean Code Bases]] — prerequisite for AI productivity
- [[AI-Generated Tests]] — risks and practices
- [[Kyle Daigle]] — GitHub COO, commit stats source
- [[SimonWillison]] — red-green TDD practitioner
- [[DHH]] — TDD critic (2014)
- [[Ian Cooper]] — "TDD Where It All Went Wrong" author
- [[Tailspin Toys]] — demo company
- [[AgentEntropy]] — unchecked AI amplifies entropy
- [[CodebaseTestability]] — prerequisite for effective testing
