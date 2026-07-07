---
title: "SpecFirstDevelopment"
type: concept
tags: [methodology, planning, claude-code, software-development, hackathon]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Spec-first development is a software development methodology where detailed specifications and plans are created before writing any code. It emphasizes thinking and design work upfront to enable faster, more directed implementation afterward. This pattern emerged as a common thread across multiple winning projects in the Built with Opus 4.7 hackathon.

## Key Information

- **Core principle**: Invest time in thinking and specification before coding, even under time pressure. The upfront investment in clarity pays off in execution speed.
- **Contrasts with**: The tendency of AI-assisted developers (and especially students) to jump straight to code generation without understanding the problem.

### Hackathon Examples

- **Paula Vásquez-Henríquez (Maieutic)**: Dedicated two full days of the five-day hackathon to pure thought work — creating a design spec and technical spec before writing a single line of code. "Those two days of spec felt slow at the time, but they were what let the rest of the week move fast."
- **Benjamin Torralbo (MaestrIA)**: Asked Claude Code to design specs, staged action plans, and security models before writing any feature. "Before writing any feature, I asked Claude Code to design the specs, the staged action plan, and the security model."
- **Idriss Benguezzou and Adam Hnaien (ARIA)**: Spent the entire second day of the hackathon in planning mode with a GitHub Project board, scoping every milestone, issue, and acceptance criterion before writing the first line of code. "One day of planning let us spend the rest of the week executing, not improvising."
- **Alexis Chapellier (Wrench Board)**: Used Claude Design and the [[Superpowers]] framework to produce first a spec and then a plan for each app responsibility before executing in Claude Code.

### Relationship to AI-Assisted Development

Spec-first development is particularly important in AI-assisted coding contexts because:
- It prevents the "generate and hope" anti-pattern where developers prompt for code without understanding the problem.
- It provides a benchmark against which AI-generated code can be evaluated (see [[EvalDrivenDevelopment]]).
- It keeps the human in the role of architect and decision-maker while the AI handles implementation.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ExplorePlanCodeCommit]] — Claude Code's recommended workflow with explicit planning phase
- [[EvalDrivenDevelopment]] — complementary methodology, evaluation before features
- [[Maieutic]] — IDE that enforces spec-first development for students
- [[Superpowers]] — skills framework that structures the brainstorm-then-plan workflow
- [[ClaudeDesign]] — design tool used for spec-first prototyping
