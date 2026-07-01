---
title: "summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock"
type: source
tags: [source, transcript, ai, workflow, ai-coding, planning, tdd, kanban, parallel-agents, afk, smart-zone, dumb-zone, vertical-slices, traceable-bullets, deep-modules, software-fundamentals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Core Summary
Matt Pocock delivers a 2-hour workshop walking through his complete AI coding workflow from idea to implementation. The workflow moves through: (1) a "Grill Me" session to reach shared understanding with the AI, (2) writing a PRD as a destination document, (3) breaking the PRD into a Kanban board of independently grabbable issues using vertical slices (traceable bullets), and (4) running AFK (away-from-keyboard) agents that pick up and implement issues sequentially or in parallel. He grounds the entire approach in classic software engineering books: the smart zone/dumb zone concept from Dex Horthy (Human Layer), deep vs shallow modules from John Ousterhout, traceable bullets from The Pragmatic Programmer, the design concept from Frederick P. Brooks, and TDD from Kent Beck. He also introduces Sandcastle, his TypeScript library for running parallel agent loops in Docker sandboxes.

## Key Points
- **Smart Zone and Dumb Zone**: LLMs perform best in the first ~100K tokens of a context window. Beyond that, attention relationships strain quadratically and the model gets progressively dumber. Tasks must be sized to stay within the smart zone
- **LLMs are like the guy from Memento**: Every time you clear context, the LLM resets to its base system prompt. Pocock prefers this over compacting because the reset state is always the same and predictable
- **Compacting vs Clearing**: Compacting squeezes conversation history into a smaller space but Pocock dislikes it. He prefers clearing context and returning to a known base state, optimizing for that reset
- **Grill Me Skill**: A skill that makes the AI interview the user relentlessly about every aspect of a plan until shared understanding is reached. Can ask 40-100+ questions. Based on Frederick P. Brooks' "design concept." Essential for human-in-the-loop alignment before any code is written
- **PRD as Destination Document**: After grilling, the conversation is summarized into a Product Requirements Document containing problem statements, user stories, implementation decisions, and testing decisions. Pocock does not review PRDs because the shared design concept already exists
- **Kanban Board with Blocking Relationships**: Instead of sequential multi-phase plans, break the PRD into independently grabbable issues with blocking relationships. This creates a directed acyclic graph (DAG) that enables parallelization by multiple agents
- **Traceable Bullets / Vertical Slices**: From The Pragmatic Programmer. AI loves to code horizontally (layer by layer: database, then API, then frontend) but this delays feedback until phase 3. Vertical slices cross all layers, giving immediate integrated feedback. Like tracer rounds that show where you're aiming
- **AFK Tasks vs Human-in-the-Loop Tasks**: Planning and alignment must be human-in-the-loop. Implementation can be AFK. This creates a "day shift" (human plans) and "night shift" (AI implements) workflow
- **Ralph Loop**: Named after Ralph Wiggum. A simple loop where the AI picks the next AFK task from the backlog, implements it with TDD, runs feedback loops (tests, type checks), and repeats until all tasks are complete
- **TDD with AI**: Test-driven development is essential for agents. Red-green-refactor prevents the AI from cheating on tests by forcing it to write a failing test first, then implement. TDD adds good tests and prevents the AI from "outrunning its headlights"
- **Feedback Loops as Speed Limit**: The quality of your feedback loops (tests, type checking, linting) determines the ceiling of AI coding quality. Bad feedback loops = bad AI output. The rate of feedback is your speed limit
- **Deep Modules vs Shallow Modules**: From John Ousterhout. Deep modules have lots of functionality behind simple interfaces and are easy to test. Shallow modules are many small files with complex dependencies, hard for AI to navigate. AI tends to produce shallow module codebases
- **Design the Interface, Delegate the Implementation**: You design module interfaces; let AI handle the implementation inside. This preserves your mental model of the codebase while moving fast
- **Doc Rot**: Keeping old PRDs and plans in the repo creates documentation that rots as code changes. This stale documentation can mislead agents. Pocock prefers closing GitHub issues (visual indicator of completion) or deleting markdown files
- **Push vs Pull for Coding Standards**: Push = always send coding standards to the agent (e.g., Claude.md). Pull = let the agent pull standards via skills when needed. Pocock recommends pull for implementers and push for automated reviewers
- **Sandcastle**: Pocock's TypeScript library for running parallel agent loops. Creates git worktrees, sandboxes them in Docker, runs implementers in parallel, then merges results with a merger agent that resolves conflicts
- **QA and Taste**: QA is where human taste is imposed back onto the codebase. Automating everything (idea creation, QA, research) produces slop. Human touch is essential for quality
- **Improve Codebase Architecture Skill**: A skill that scans the codebase for architectural improvement candidates, identifying clusters of related modules that could be tested as a unit, and proposing deep module refactors
- **Key books referenced**: A Philosophy of Software Design (John Ousterhout), The Pragmatic Programmer (Hunt & Thomas), The Design of Design (Frederick P. Brooks), Domain-Driven Design (Eric Evans), Refactoring (Martin Fowler)

## Related
- [[MattPocock]] — speaker, workshop presenter
- [[aiDotEngineer]] — conference
- [[ClaudeCode]] — the AI coding tool used in the workshop
- [[DexHorthy]] — creator of smart zone / dumb zone concept
- [[Human Layer]] — Dex Horthy's company
- [[Sandcastle]] — Pocock's parallel agent loop library
- [[JohnOusterhout]] — author of A Philosophy of Software Design
- [[FredBrooks]] — author of The Design of Design
- [[KentBeck]] — creator of TDD
- [[Smart Zone and Dumb Zone]] — LLM context window performance zones
- [[Compacting]] — squeezing conversation history
- [[Grill Me]] — the AI interviewing skill
- [[PRD (Product Requirements Document)]] — destination document
- [[Kanban Board for AI Tasks]] — parallelizable issue board
- [[Traceable Bullets]] — vertical slices for feedback
- [[Vertical Slices]] — crossing all layers for integrated testing
- [[AFK Tasks]] — away-from-keyboard tasks
- [[Day Shift Night Shift]] — planning vs implementation workflow
- [[Ralph Loop]] — iterative small-change loop
- [[Doc Rot]] — documentation rotting in repo
- [[Push vs Pull Coding Standards]] — enforcing standards on agents
- [[TDD with AI]] — test-driven development for agents
- [[Feedback Loops as AI Speed Limit]] — feedback quality determines AI ceiling
- [[Memento Pattern for LLMs]] — LLMs reset to base state
- [[Deep Modules]] — from John Ousterhout
- [[Shallow Modules]] — from John Ousterhout
- [[Design the Interface, Delegate the Implementation]] — tip from prior talk
- [[Design Concept]] — from Frederick P. Brooks
- [[SpecsToCode]] — movement Pocock critiques
- [[Software Fundamentals Matter More Than Ever]] — related thesis
- [[VibeCoding]] — related anti-pattern
- [[Skills]] — agent playbooks
- [[SubAgents]] — delegation pattern
- [[Parallel Agents]] — multi-agent execution
- [[CodeSlop]] — what un-reviewed AI output produces
- [[Taste (Software)]] — human judgment in QA
