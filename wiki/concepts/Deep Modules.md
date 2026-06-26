---
title: "Deep Modules"
type: concept
tags: [software-design, architecture, modularity, code-quality, ai-coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Definition
Deep modules are a software design concept from John Ousterhout's "A Philosophy of Software Design." A deep module has lots of functionality hidden behind a simple interface — it encapsulates complexity so that consumers can use it without understanding its internals.

## Key Information
- From John Ousterhout's "A Philosophy of Software Design"
- Deep modules: lots of functionality, simple interface — hiding complexity behind a clean boundary
- Contrast with shallow modules: little functionality, complex interface
- Good codebases have relatively few large deep modules with simple interfaces
- Deep modules make codebases testable: you test at the simple interface without needing to understand internal complexity
- AI tends to create shallow module codebases — lots of tiny blobs that are hard to navigate and understand
- Shallow module codebases cause AI to fail at understanding what the code does — it can't explore effectively
- Matt Pocock's "Improve Codebase Architecture" skill restructures shallow module codebases into deep module codebases
- Deep modules also save human cognitive load: you can treat them as "gray boxes" — design the interface, review the implementation less
- The interface should be carefully designed by humans; the implementation can be delegated to AI
- Deep modules are a prerequisite for effective TDD with AI

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[JohnOusterhout]] — author of A Philosophy of Software Design
- [[Shallow Modules]] — the contrasting concept
- [[Design the Interface, Delegate the Implementation]] — strategy enabled by deep modules
- [[MattPocock]] — speaker who advocates this pattern
- [[CodebaseTestability]] — related concept
- [[Modularity]] — broader concept
