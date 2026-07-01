---
title: "Persona-oriented Documentation"
type: concept
tags: [ai, agentic-engineering, documentation, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Persona-oriented documentation is the practice of writing documentation from the perspective of different engineering personas (front-end architect, reliability engineer, security engineer, product-minded engineer), each specifying what "good" looks like from their domain. This enables reviewer agents and implementation agents to access the best of every team member's expertise.

## Key Information
- Practice from Ryan Lopopolo's team at OpenAI
- Each engineer on a diverse full-stack team brings a different understanding of non-functional requirements
- By writing those down as persona-specific docs, every agent trajectory gets the benefit of every team member's expertise
- Example: a product-minded engineer documents what a good QA plan looks like → a reviewer agent can assert QA plan expectations on every PR
- Personas include: front-end architecture, back-end scalability, product-mindedness, security, reliability
- Each persona feeds a corresponding reviewer agent that runs in CI
- Eliminates the need to block on low-signal code review to learn what good looks like from each perspective
- Stacks leverage: document once, benefit every agent trajectory forever

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[Reviewer Agents]] — consume persona-oriented docs
- [[NonFunctional Requirements Specification]] — what persona docs specify
- [[Garbage Collection Day]] — when persona docs are updated
- [[AgenticEngineering]] — broader paradigm
