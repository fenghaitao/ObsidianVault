---
title: "Feedback Loops as AI Speed Limit"
type: concept
tags: [ai, feedback, testing, code-quality, agents, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
The principle that the quality and speed of a codebase's feedback loops (tests, type checking, linting) determines the ceiling of what AI coding agents can achieve. Without good feedback loops, AI is "coding blind" and will produce poor output regardless of model capability.

## Key Information
- "The quality of your feedback loops influences how good your AI can code — that is the ceiling"
- If you're getting bad outputs from AI, you often need to increase the quality of your feedback loops, not change the model or prompt
- Essential feedback loops: tests (NPM run test), type checking (NPM run type check), linting
- AI without feedback loops is "totally coding blind"
- The Ralph Loop runs feedback loops after each implementation: tests and type checks, fixing any errors found
- In the workshop demo, the AI ran tests (284 tests in the repo), got one type error, and fixed it autonomously
- This principle extends the Pragmatic Programmer's idea that "the rate of feedback is your speed limit"
- Frontend testing is particularly hard — Pocock's demo only tested the service layer, not the UI
- Good feedback loops are a prerequisite for AFK tasks: without them, the AI cannot self-correct

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — advocates this principle
- [[TDD with AI]] — the primary feedback mechanism
- [[Ralph Loop]] — where feedback loops run
- [[Traceable Bullets]] — vertical slices for integrated feedback
- [[Deep Modules]] — codebase structure for testability
- [[CodebaseTestability]] — prerequisite
- [[Verification in Agentic Loops]] — related concept
- [[AutomatedValidation]] — related concept
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (eval feedback loops for agent optimization)
- [[Agent Optimization]] — optimization depends on eval feedback loops
- [[EvalFlywheel]] — continuous improvement via feedback
