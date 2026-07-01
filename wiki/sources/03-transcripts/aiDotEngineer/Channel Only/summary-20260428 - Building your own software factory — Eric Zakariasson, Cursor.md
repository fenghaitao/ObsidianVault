---
title: "Building your own software factory — Eric Zakariasson, Cursor"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md"
author: "Eric Zakariasson"
organization: "Cursor"
date: 2026-04-28
tags: [software-factory, agent-autonomy, cursor, guardrails, ai-engineering]
---

# Building your own software factory — Eric Zakariasson, Cursor

## Core Thesis

Eric Zakariasson, an engineer at Cursor working on developer experience, presents his practical framework for building a "software factory" — an autonomous software development system where AI agents handle most coding, testing, and review. Building a factory requires three layers: **primitives and patterns** (codebase structure agents can navigate), **guardrails** (rules, hooks, tests that constrain agent behavior), and **enablers** (skills, MCPs, environments that empower agents). As the factory matures, the human's role shifts from worker to manager, overseeing a fleet of agents running asynchronously, and the factory improves through a flywheel of identifying failures, codifying rules, and automating repetitive touchpoints.

## Key Points

1. **Levels of Autonomy**: Dan Shapiro's six-stage framework — from spicy autocomplete (Level 1) through pair programmer (Level 2-3), AI-generated majority code (Level 3), manager-like delegation (Level 4), to the dark factory (Level 6) where agents operate as a black box.

2. **Why build a factory**: Higher throughput (agents run 24/7), consistent output via assembly lines, and better leverage of human taste and creativity.

3. **Three layers of factory building**:
   - **Primitives & Patterns**: Modularized codebases, colocated code, established usage patterns (auth methods, startup scripts, test boilerplates) that agents can discover and reproduce.
   - **Guardrails**: Rules that emerge dynamically from agent failures (not pre-installed), hooks on sensitive code areas, and tests for agent self-verification.
   - **Enablers**: Skills, MCPs, external context access, and reproducible environments (isolated VMs) that let agents be free.

4. **Verifiable systems**: The most underinvested area — agents must verify their own work through unit tests, integration tests, UI tests (Playwright, computer use), and automated code review (Bugbot).

5. **Cursor 3**: A complete rewrite of Cursor without VS Code, designed for an agent-first workflow with multi-agent orchestration, nested agents, and aggregated status views.

6. **Cloud Agents**: Each agent gets an isolated VM with reproducible environments, enabling infinite scaling. Agents can use computer-use tools to test their own work and return video evidence.

7. **Worker to Manager**: The human shifts from writing code to scoping work, parallelizing tasks, preserving tribal knowledge, and frontloading context via specs and plans.

8. **Sync to Async**: Most work happens in the background; humans need to trust agents more and provide more context upfront.

9. **Scaling the factory**: From 5 to 10 to 50 to 100 agents — observe outcomes, build automations for repetitive tasks, and let agents identify their own improvement opportunities.

10. **Automations at Cursor**: Daily review summaries, PR comment extraction for learning, agentic code owners (risk-based auto-approval), and continual learning plugins that extract rules from agent transcripts.

11. **Key principles**: Be clear about intent, don't outsource important decisions (security, payments, auth), build tools and systems, store context for later, and let agents be free — even give them a channel to complain.

## Entities

- [[EricZakariasson]] — Engineer at Cursor, presenter
- [[DanShapiro]] — Author of six levels of AI coding autonomy framework
- [[Cursor]] — AI-powered code editor, updated with Cursor 3 and Cloud Agents
- [[Cursor3]] — Complete rewrite of Cursor, agent-first IDE without VS Code
- [[CursorCloudAgents]] — Cursor's cloud-based isolated VM agent infrastructure
- [[Bugbot]] — Cursor's internal automated PR review tool
- [[Glass]] — Cursor's internal interface/IDE component
- [[Lovable]] — AI app builder company; gave agents a Slack vent channel
- [[Ableton]] — Music production software used as UI reference in Eric's demo
- [[Playwright]] — Browser automation library used for end-to-end agent testing
- [[DataDog]] — Log and monitoring service
- [[Linear]] — Project management tool
- [[Notion]] — Documentation and spec management tool
- [[Slack]] — Team communication platform
- [[OrbStack]] — Container runtime used in Cursor's dev environment
- [[ClickHouse]] — Columnar database used in Cursor's backend
- [[Electron]] — Desktop app framework used by Cursor

## Concepts

- [[SoftwareFactory]] — Autonomous software development system with assembly lines of AI agents
- [[LevelsOfAutonomy]] — Dan Shapiro's six-stage framework for AI coding autonomy
- [[Dark Factory]] — Level 6 autonomy: black box where agents ship, test, and build autonomously
- [[PrimitivesAndPatterns]] — Codebase structures and conventions that make agent work easier
- [[Guardrails]] — Rules, hooks, and checks constraining agent behavior in a software factory
- [[CursorRules]] — Dynamic rules emerging from agent failures, acting as SOPs for agent behavior
- [[Enablers]] — Skills, MCPs, and capabilities that empower agents to work autonomously
- [[VerifiableSystems]] — Systems where agents can verify their own work through automated tests
- [[AgentFirstWorkflow]] — Design paradigm where the IDE is built for agent interaction first
- [[WorkerToManager]] — Mindset shift from writing code to overseeing a fleet of AI agents
- [[SyncToAsync]] — Shift from synchronous to asynchronous work as agents run in the background
- [[AgentTrust]] — Building trust in agents through guardrails, verification, and frontloaded context
- [[IsolatedEnvironments]] — Using separate VMs per agent for clean, reproducible, side-effect-free work
- [[HumanInTheLoopAutomation]] — Identifying and automating away human-in-the-loop touchpoints
- [[ContinualLearning]] — Automatically extracting rules and memories from agent transcripts over time
- [[AgenticCodeOwners]] — Automated code owner review system that assesses PR risk and auto-approves low-risk changes
- [[AgentFeedbackLoop]] — Flywheel of identifying failures, creating rules, and improving the factory

## Related

- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — complementary perspective on agent-ready codebases
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — Replit's framework for autonomous coding agents
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — parallel agent orchestration at scale
- [[MCP]] — Model Context Protocol for agent-tool integration
- [[Computer Use]] — browser testing via screenshots used by Cursor Cloud Agents
- [[VibeCoding]] — AI-assisted coding approach referenced in Q&A
