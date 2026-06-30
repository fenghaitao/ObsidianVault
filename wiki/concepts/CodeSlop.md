---
title: "CodeSlop"
type: concept
tags: [code-quality, ai-coding, tech-debt]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"]
last_updated: 2026-06-30
---

## Definition
Code slop is AI-generated code that is low-quality, creates disproportionate tech debt, or introduces security vulnerabilities — the software engineering manifestation of the broader slop problem. Mario Zechner's "compounding booboos" and "enterprise-grade complexity in 2 weeks" are concrete examples of code slop at scale.

## Key Information
- Two engineers using AI can create the tech debt of 50 engineers
- Can lead to exposing private data of millions of users — real incidents occurred in the year of the talk
- Measuring AI coding tools by "how long they can run autonomously" (e.g., 30-60 hours) without evaluating code quality is a form of slop
- swyx's principle: "No autonomy without accountability" — autonomy claims must be paired with quality metrics
- Fighting code slop requires: Code Maps for scaling codebase understanding, Semi-Sync Value of Depth for keeping human attention on hard problems, and modularity with clear human-designed boundaries
- Sub-agents can help fight "context rot" which contributes to code slop
- Mario Zechner: agents learn complexity from internet garbage (90% of code is old garbage), every agent decision is local, leading to "enterprise-grade complexity within 2 weeks with just two humans and 10 agents"
- Mario's policy: non-critical code gets "five slop ahead" (relaxed review); critical code must be read line by line

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source
- [[summary-20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — source (Priscila: "Don't ship slop code")
- [[Slop]] — the broader concept
- [[SemiSyncValueOfDepth]] — framework for fighting code slop
- [[Modularity]] — design principle to reduce code slop
- [[SubAgents]] — technique to fight context rot and code slop
- [[ComputerUse]] — AI capability that can both produce and fight code slop
- [[CompoundingBooboos]] — Mario's term for code slop accumulation
- [[Keynote Code]] — the opposite: high-quality AI-generated code
- [[Priscila Andre de Oliveira]] — advocated against shipping slop code
- [[SlowingDownWithAgents]] — Mario's prescription for fighting code slop
