---
title: "CodeSlop"
type: concept
tags: [code-quality, ai-coding, tech-debt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md"]
last_updated: 2026-06-25
---

## Definition
Code slop is AI-generated code that is low-quality, creates disproportionate tech debt, or introduces security vulnerabilities — the software engineering manifestation of the broader slop problem.

## Key Information
- Two engineers using AI can create the tech debt of 50 engineers
- Can lead to exposing private data of millions of users — real incidents occurred in the year of the talk
- Measuring AI coding tools by "how long they can run autonomously" (e.g., 30-60 hours) without evaluating code quality is a form of slop
- swyx's principle: "No autonomy without accountability" — autonomy claims must be paired with quality metrics
- Fighting code slop requires: Code Maps for scaling codebase understanding, Semi-Sync Value of Depth for keeping human attention on hard problems, and modularity with clear human-designed boundaries
- Sub-agents can help fight "context rot" which contributes to code slop

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[Slop]] — the broader concept
- [[SemiSyncValueOfDepth]] — framework for fighting code slop
- [[Modularity]] — design principle to reduce code slop
- [[SubAgents]] — technique to fight context rot and code slop
- [[ComputerUse]] — AI capability that can both produce and fight code slop
