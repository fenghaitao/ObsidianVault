---
title: "BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"
author: "Michal Cichra"
company: "Safe Intelligence"
date: 2026-06-03
tags: [adr, bdd, prd, decision-capture, agent-harness, design-system, cucumber, executable-specifications]
---

# BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

## Core Thesis

Both humans and AI agents suffer from limited context — people forget and leave, LLMs have no memory and suffer context compacts. To operate products and teams sustainably at scale, you must capture decisions in structured, enforceable formats: Architecture Decision Records (ADRs) for why and how things are built, Product Requirements Documents (PRDs) for why features exist, Behavior-Driven Development (BDD) with Cucumber for executable, readable specifications, and Design Systems for consistent UI. These are tied together by a reinforcement loop (git hooks, skills, CI, linters) that enforces rules automatically, giving agents feedback at commit time and linking them back to the governing documents.

## Key Points

### The Limited Context Problem

- The Five Monkeys Experiment allegory: monkeys are replaced one by one until none of the originals remain, yet they keep enforcing rules without knowing why. Humans and LLMs share this trait — limited context.
- After operating a product for a while, teams ask: "Why do we have this flow? Why is this feature's goal? Why is this code shaped like that? Why does this belong here?"
- The founding engineer may not be available to answer. These problems show up in every org, and with AI, much sooner than they used to.

### Architecture Decision Records (ADRs)

- ADRs record why you do something and how you enforce it. Cover examples by reference docs and code snippets.
- Example: split code in layers to prevent N+1 queries, enforce the split by linting imports in modules. Also enforce that database reads return plain shapes instead of ORM objects to prevent duplication.
- There is no single format — it is just a concept, a text document. A tool is still needed to enforce the rule, but the tool links back to the ADR explaining why the rule exists and how to fix violations.
- Agents go and find the ADR to understand why a rule exists and how to fix the issue.

### Product Requirements Documents (PRDs)

- A lightweight document describing why a feature exists, what problems it solves, and how the user journeys through the application.
- Captures the why, the problem, the goal, and the journey that connects them.
- Not just for agents — also for your future self 6 weeks from now when you forget why you did something.
- It can be very light; does not need to be a massive exhaustive document.

### Behavior-Driven Development (BDD) with Cucumber

- Spec-driven development describes how something should work, but how do you validate the product actually adheres to the spec?
- One thing harder than reading AI-generated code is reading AI-generated tests.
- BDD provides an intermediate layer that describes product behavior in human language — readable and executable.
- Cucumber: almost forgotten, suddenly useful again. Easier to review than average tests. Connects scenarios directly to PRDs and critical user journeys.
- The language is on you — there are multiple ways to write features, but they describe how to go through the application, why things exist, and how they run. Can refer back to all documents about why things exist.
- BDD closes the loop that spec-driven development leaves open.

### Design Systems for Consistent UI

- Making consistent UIs with agents is "just another level of hard."
- Design systems and pattern libraries were the way to build consistent UIs before AI and remain the way now.
- Document your language: define components (e.g., primary button is blue, has this shape, this size), define rules (e.g., only one primary button visible per page).
- Define components and patterns with previews and snippets so agents can see them. Review whether outputs adhere to principles and visuals.
- Build from small pieces into bigger ones, compose and reuse. Define rules like "no inline styles anywhere else."

### The Decision Capture Loop (Harness)

- How to keep teams and agents consistent: the reinforcement loop.
- Simple loop: git hooks → skills → CI → linters → other checks.
- The agent's goal is to deliver a pull request. To do that, they must use git, so git hooks run predefined tasks. The same tasks execute on CI — if agents skip hooks, they get caught.
- Includes: linting, formatting, type checking, code duplication, architecture checks, document linting — everything possible.
- Code reviews are no longer about style, tabs, and spaces. These are rules, enforced and automated — there is no space for discussion about them anymore.
- "What you cannot find, you cannot enforce." Example: architecture enforcement via module import restrictions. BDD end-to-end tests cannot access database modules. Rendering templates cannot talk to database — N+1 queries are prevented entirely, not just found.
- Agent tries to commit → gets rejected → gets linked back to the governing document → reads it → fixes it → iterates.
- The loop is generic but the focus changes per context: ADR skill, PRD skill, UI loop (skip checks, iterate in browser quickly), test skill (run focused suite based on code coverage and file changes), goal execution skill (keep decisions for later review).

### Context Compacts Are OK

- Drawback: the approach is context-heavy — you can run out of half the context just starting research.
- But Michal has no fear of context compacts. Sessions with 20-50 context compacts are fine because the important things survive and the agent will always look them up again.
- The goal is multi-hour sessions with a clear goal where agents operate autonomously with defined rules.

## Entities

- [[Michal Cichra]] — speaker, Safe Intelligence, previously Microsoft, Red Hat, 10 years on a single product
- [[SafeIntelligence]] — company, released Spec 27 product for agent testing
- [[Spec 27]] — new product from Safe Intelligence to test agents

## Concepts

- [[Architecture Decision Record (ADR)]] — records why something is done and how it is enforced
- [[PRD (Product Requirements Document)]] — lightweight document capturing why a feature exists, the problem, goal, and user journey
- [[Behavior-Driven Development (BDD)]] — executable, readable specifications describing product behavior in human language
- [[Cucumber]] — BDD tool, almost forgotten, suddenly useful again for AI-generated code
- [[Design System]] — component and pattern library for building consistent UIs with agents
- [[Decision Capture Loop]] — the reinforcement loop of git hooks, skills, CI, and linters that enforces rules automatically
- [[Executable Specifications]] — BDD specs that are both human-readable and executable as code, closing the spec-driven development loop
- [[Architecture Enforcement]] — preventing problems entirely by restricting module imports rather than finding them

## Related

- [[summary-20260531 - Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence]] — related talk from same company on spec-driven testing
- [[SpecificationDrivenDevelopment]] — BDD closes the loop that spec-driven development leaves open
- [[AgentHarness]] — the reinforcement loop concept
- [[Agent-Specific MD Files]] — related to how agents look up rules
- [[Enforce Dont Instruct]] — related principle about automated enforcement
- [[Compacting]] — context compacts are a central concern addressed in this talk
