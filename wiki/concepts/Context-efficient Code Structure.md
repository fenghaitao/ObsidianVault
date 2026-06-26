---
title: "Context-efficient Code Structure"
type: concept
tags: [ai, agentic-engineering, code-organization, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Context-efficient code structure is the practice of organizing repositories to minimize the context window tokens needed for agents to understand and modify code. It emphasizes making code as uniform as possible, scoping changes to directory subtrees, and isolating domains by business logic.

## Key Information
- Practice from Ryan Lopopolo's team at OpenAI: 750 packages in a pnpm workspace, isolated by business logic domain or layer of the stack
- Core principle: code in the file system is text, which means it's effectively prompts for the coding agent
- Making code as much the same as possible means the agent develops transferable context regardless of where it looks
- Rules: one way to do bounded concurrency, one ORM, one programming language, one way of writing CI scripts, one way of adding lint rules
- Individual small util packages encapsulate reusable functionality, linted on being used, encoding leverage
- Structuring repos so most changes are scoped to a directory subtree helps agents work locally
- Package privacy enforces invariants about public vs. private APIs
- Even without microservices, structuring monorepos this way improves agent performance
- Large-scale refactoring to achieve uniformity is free — fire off 15 agents to complete migrations

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[ContextEngineering]] — related discipline
- [[Code is Free]] — enables large-scale refactoring for uniformity
- [[AgentReadyCodebases]] — related concept
