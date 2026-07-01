---
title: "summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock"
type: source
tags: [source, transcript, ai, software-fundamentals, software-design, specs-to-code, tdd, ubiquitous-language, deep-modules, ai-coding]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md"]
last_updated: 2026-06-26
---

## Core Summary
Matt Pocock, creator of the popular "Claude Code for Real Engineers" course, argues that software fundamentals matter more than ever in the age of AI coding. He critiques the "specs-to-code" movement (where you write a spec, let AI generate code, and never look at the code) as producing progressively worse code through software entropy. Instead, he presents five practical tips rooted in classic software engineering books: (1) use a "Grill Me" skill to reach shared design concepts with AI, (2) establish a ubiquitous language with AI using domain-driven design, (3) use TDD to force small deliberate steps, (4) structure codebases with deep modules for testability, and (5) design interfaces while delegating implementations to AI. His core message: code is not cheap — bad code is the most expensive it's ever been, because it prevents you from taking advantage of AI's full potential.

## Key Points
- **Specs-to-code doesn't work**: Running the "compiler" (AI) repeatedly on a spec produces progressively worse code due to software entropy — each change made without considering overall design degrades the codebase
- **Code is not cheap**: Bad code is the most expensive it's ever been. AI does really well in good codebases but poorly in bad ones. Good codebases matter more than ever
- **Tip 1 — Grill Me skill**: A simple prompt that makes the AI interview you relentlessly about every aspect of a plan until shared understanding is reached. Based on Frederick P. Brooks' "design concept" from The Design of Design. Better than default plan modes because it reaches shared understanding before creating assets
- **Tip 2 — Ubiquitous Language**: From domain-driven design (DDD), create a shared terminology file with the AI. A markdown file with terms both you and the AI agree on. Improves planning and makes AI think less verbosely, producing more aligned implementations
- **Tip 3 — TDD**: Test-driven development forces the AI to take small deliberate steps. The rate of feedback is your speed limit (from The Pragmatic Programmer). AI by default "outruns its headlights" — produces huge amounts of code before checking
- **Tip 4 — Deep Modules**: From John Ousterhout's A Philosophy of Software Design. Deep modules have lots of functionality hidden behind simple interfaces. Shallow modules have little functionality with complex interfaces. AI tends to create shallow module codebases that are hard to explore and test
- **Tip 5 — Design the Interface, Delegate the Implementation**: Structure code into deep modules with well-designed interfaces. You design the interfaces; let AI handle the implementation inside. Saves your brain from having to understand every detail. Reference Kent Beck: "Invest in the design of the system every day"
- **Strategic vs. Tactical**: AI is a great tactical programmer (sergeant on the ground). You need to be the strategic thinker above it. This requires software fundamental skills we've been using for 20+ years
- **Key books referenced**: A Philosophy of Software Design (John Ousterhout), The Pragmatic Programmer (Hunt & Thomas), The Design of Design (Frederick P. Brooks), Domain-Driven Design (Eric Evans)

## Related
- [[MattPocock]] — speaker, course creator
- [[aiDotEngineer]] — conference
- [[ClaudeCode]] — the AI coding tool he teaches
- [[JohnOusterhout]] — author of A Philosophy of Software Design
- [[FredBrooks]] — author of The Design of Design
- [[KentBeck]] — creator of TDD, "invest in the design of the system every day"
- [[Software Entropy]] — concept from The Pragmatic Programmer
- [[Design Concept]] — from Frederick P. Brooks' The Design of Design
- [[Ubiquitous Language]] — from domain-driven design
- [[Deep Modules]] — from John Ousterhout
- [[Shallow Modules]] — from John Ousterhout
- [[SpecsToCode]] — the movement Pocock critiques
- [[Outrunning Your Headlights]] — from The Pragmatic Programmer
- [[Grill Me]] — the AI interviewing skill
- [[Design the Interface, Delegate the Implementation]] — tip 5
- [[Code is Not Cheap]] — counter-argument to "code is cheap"
- [[Software Fundamentals Matter More Than Ever]] — the core thesis
- [[VibeCoding]] — related anti-pattern
- [[SpecificationDrivenDevelopment]] — related approach
- [[AgenticEngineering]] — related paradigm
- [[Skills]] — agent playbooks
- [[CodeSlop]] — what specs-to-code produces
