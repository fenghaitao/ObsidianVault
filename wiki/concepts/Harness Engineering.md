---
title: "Harness Engineering"
type: concept
tags: [agentic-engineering, context-engineering, software-engineering, openai, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Harness Engineering is the discipline of building systems, structures, and processes that enable coding agents to do the full job of software engineering. Coined by Ryan Lopopolo (OpenAI), it shifts the engineer's role from writing code to building guardrails, writing documentation, and designing context-efficient systems that steer agents toward acceptable output.

## Key Information
- Coined by Ryan Lopopolo, MTS at OpenAI, based on 9 months of building software exclusively with agents
- Core premise: implementation is no longer the scarce resource — code is free and infinitely abundant
- Scarce resources are human time, human/model attention, and model context window
- Engineers become "staff engineers" driving as many agent team members as token budgets allow
- The important artifact is not the code but the prompt and guardrails that produced it
- Key practices: persona-oriented documentation, reviewer agents in CI, just-in-time context surfacing, Garbage Collection Day
- Centralize leverage around 5-10 skills rather than going wide; hide infrastructure complexity beneath skills
- Entry point should be the coding agent (e.g., Codex), not the development environment
- Future vision: take a token budget and a quarter/half/year of work, human input to rank priorities, give it to machines

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[RyanLopopolo]] — coined the term
- [[Token Billionaire]] — related concept
- [[Code is Free]] — foundational premise
- [[Garbage Collection Day]] — systematic slop elimination practice
- [[Reviewer Agents]] — CI-based automated code review
- [[JustInTime Context Surfacing]] — deferred instruction pattern
- [[NonFunctional Requirements Specification]] — writing down NFRs for agents
- [[PersonaOriented Documentation]] — docs from different engineering perspectives
- [[ContextEfficient Code Structure]] — structuring repos for agent efficiency
- [[LLM as Fuzzy Compiler]] — mental model
- [[Code as Disposable Build Artifact]] — related paradigm
- [[AgenticEngineering]] — broader paradigm
- [[ContextEngineering]] — related discipline
