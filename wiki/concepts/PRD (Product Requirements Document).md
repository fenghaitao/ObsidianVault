---
title: "PRD (Product Requirements Document)"
type: concept
tags: [ai, planning, workflow, documentation, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence.md"]
last_updated: 2026-06-30
---

## Definition
In Matt Pocock's AI coding workflow, a PRD (Product Requirements Document) serves as the "destination document" — a summary of the shared design concept reached during a Grill Me session, containing problem statements, user stories, implementation decisions, and testing decisions.

## Key Information

### Matt Pocock's AI Coding Workflow

- In Matt Pocock's AI coding workflow, a PRD serves as the "destination document" — a summary of the shared design concept reached during a Grill Me session, containing problem statements, user stories, implementation decisions, and testing decisions
- The PRD is created after the Grill Me session as a way to capture the shared understanding between human and AI
- Contains: problem statements (what the user is facing), solution description, user stories (often 18+), implementation decisions, and testing decisions
- Pocock does not review PRDs because the shared design concept already exists from the grilling session. Reviewing would only test the LLM's summarization ability, not the correctness of the plan
- The PRD also includes an "out of scope" section listing what will not be tackled, which is important for defining "done"
- The PRD serves as input to the next step: breaking into a Kanban board of independently grabbable issues
- Pocock's "Write a PRD" skill: asks for a long description, optionally installs the repo, interviews the user, then produces a templated PRD
- The PRD can be stored as GitHub issues (Pocock's preference, with 744+ closed issues in his course-video-manager repo) or as local markdown files
- The PRD is not meant to be a permanent artifact — Pocock warns against doc rot from keeping old PRDs in the repo

### Michal Cichra's Lightweight Definition

- A lightweight document describing why a feature exists, what problems it solves, and how the user journeys through the application
- Captures the why, the problem, the goal, and the journey that connects them
- Can be very light — does not need to be a massive exhaustive document
- Not just for agents, but also for your future self 6 weeks from now when you forget why you did something
- PRDs are part of the [[Decision Capture Loop]]: they are governing documents that agents reference when their commits are rejected by automated enforcement

## Related

- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[summary-20260603 - BDD, ADR, PRD, WTF： Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence]] — source transcript
- [[MattPocock]] — workflow creator
- [[Michal Cichra]] — lightweight definition
- [[Grill Me]] — prerequisite step before PRD creation
- [[Kanban Board for AI Tasks]] — next step after PRD
- [[Design Concept]] — the shared understanding the PRD captures
- [[Doc Rot]] — why PRDs should not be kept permanently
- [[SpecsToCode]] — the movement Pocock contrasts with
- [[SpecificationDrivenDevelopment]] — related approach
- [[Decision Capture Loop]] — the enforcement loop PRDs participate in
- [[BehaviorDriven Development (BDD)]] — BDD scenarios connect to PRDs
- [[Architecture Decision Record (ADR)]] — complementary decision record for architecture
