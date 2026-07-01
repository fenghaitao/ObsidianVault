---
title: "TDD with AI"
type: concept
tags: [ai, tdd, testing, agents, implementation, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
TDD with AI is the application of test-driven development (red-green-refactor) to AI-assisted coding. The AI writes a failing test first, then implements the code to make it pass, then refactors. Matt Pocock considers TDD absolutely essential for getting the most out of coding agents. Raj uses TDD as the core analogy for Demand-Driven Context: write failing tests (problems agents fail on), then implement (fill knowledge gaps).

## Key Information
- The AI follows red-green-refactor: write a failing test (red), implement to make it pass (green), then refactor
- TDD prevents the AI from "cheating" on tests. Without TDD, AI tends to write all the implementation first, then write tests that simply validate the already-written code
- TDD forces the AI to instrument the code before writing it, making it harder to cheat
- TDD adds good tests to the codebase as a side effect
- Pocock has "warped his whole technique around getting TDD to work better" because it's so effective
- AI tends to write bad tests when not constrained by TDD: wrapping every tiny function in its own test boundary, mocking dependencies in ways that miss integration bugs
- TDD is part of the Ralph Loop: explore repo, use TDD to complete the task, run feedback loops
- TDD works best in codebases with deep modules that are easy to test
- The "rate of feedback is your speed limit" — TDD provides rapid feedback that keeps AI on track
- **Demand-Driven Context Analogy**: "In a TDD approach, we just write the failed test cases. We don't build the product first. We see what code is missing for the failed test case to pass and we just give that code and gradually build the product. In the same way, we give problems that agent will definitely fail and we gradually fill those gaps." The Demand-Driven Context cycle mirrors red-green-refactor: problem (red) → fill gaps (green) → curate knowledge (refactor).
- **Marlene Mhangami's Playwright TDD Workflow**: AI agents write failing Playwright behavioral tests (red), generate code to pass them (green), and developers focus on refactoring. This shifts the trigger for writing tests from "new method" to "new feature request." The red and green phases become fast with AI, allowing developers to invest more time in refactoring for quality.
- **Self-affirming tests risk**: AI can generate tests that pass and achieve code coverage without validating actual behavior. TDD (writing tests first) mitigates this.
- **Simon Willison** published about using red-green TDD with AI agents, advocating the write-failing-test-first approach.

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source (Playwright TDD workflow)
- [[MattPocock]] — advocates TDD for AI
- [[KentBeck]] — creator of TDD
- [[Ralph Loop]] — where TDD is used
- [[Feedback Loops as AI Speed Limit]] — why TDD's rapid feedback matters
- [[Deep Modules]] — codebase structure that enables TDD
- [[CodebaseTestability]] — prerequisite for TDD
- [[Verification in Agentic Loops]] — related concept
- [[DemandDriven Context]] — methodology using TDD as core analogy
- [[Agent Failure as Discovery]] — the "red" phase in knowledge TDD
- [[Knowledge Curation]] — the "refactor" phase in knowledge TDD
- [[RedGreen TDD]] — specific TDD flavor
- [[SimonWillison]] — red-green TDD practitioner
- [[Marlene Mhangami]] — Playwright TDD workflow advocate
- [[Playwright]] — testing framework for behavioral TDD
- [[Functionality Testing]] — testing approach in the red phase
- [[SelfAffirming Tests]] — problem TDD prevents
- [[AIGenerated Tests]] — risks and mitigation through TDD
