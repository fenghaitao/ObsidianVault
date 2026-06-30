---
title: "summary-20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry"
type: source
tags: [source, transcript, ai, comprehension, skills, sentry, claude, agent-manager, code-comprehension]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"]
last_updated: 2026-06-30
---

## Core Summary
Priscila Andre de Oliveira, Senior Software Engineer at Sentry, argues that the biggest unlock from AI in a large codebase is not generation — it is comprehension. She tracked her own AI usage across 116 sessions: 67% was comprehension (understanding code, architecture, conventions) and only 2% was code generation. Based on this insight, she built a custom Claude skill called "Catch Me Up" that structures comprehension questions into six exploration modes: Architecture, Convention, Feature Trace, Syntax, Testing, and History. She describes herself as an "agent manager" who no longer writes code — only prompts — but insists that understanding what the AI produces is essential: "Don't ship slop code into the codebase that pays your salary. Ship keynote code."

## Key Points
- **67% comprehension, 2% generation**: Priscila had Claude analyze 116 of her AI sessions. The overwhelming majority of her AI usage was comprehension — understanding existing code, conventions, architecture, and history — not generating new code.
- **"Catch Me Up" skill**: A custom Claude skill she built locally that structures comprehension queries into six exploration modes:
  - Architecture — how the system is organized
  - Convention — patterns, lint rules, coding standards
  - Feature Trace — following a feature through the codebase
  - Syntax — language-specific constructs
  - Testing — how tests are structured and run
  - History — git blame, why changes were made
- The skill produces visual outputs (organograms, tables, flow diagrams) because she is a visual, frontend-oriented developer who learns better from structure.
- **Agent Manager identity**: Since December 2025, she has not coded at all — only prompting. She jokingly calls herself an "agent manager" with no salary raise but reports that "don't complain."
- **Sentry's internal AI tools**: Abacus (tracks internal AI usage), Warden (code review agent in PRs), Junior (Slack bot that analyzes bug reports and creates PRs), and an AI SDK testing repository where contributors are told to only prompt, not code.
- **Quality matters even with AI**: Sentry ran a three-month "quality quarter" focused on removing `any` types from TypeScript, eliminating TODO comments, simplifying code, and removing unused feature flags. Technical debt cleanup makes the codebase more legible for AI.
- **Sentry's codebase context**: 15+ years of code, ~400 employees, 100k organizations depending on it, ~100 PRs merged daily, fair source, constantly deprecating and adding components and lint rules.
- **The missing step in AI workflows**: Jake Nations' three-phase approach (Research → Planning → Implementation) is right, but Priscila argues it is missing a critical step: you must **understand** the research your agent did before planning. AI can misunderstand the codebase, and you need comprehension to steer it correctly.
- **Armin Ronacher quote**: She quotes the Flask creator: "When more and more people tell me they no longer know what code is in their own codebase, I feel like something is very wrong here."
- **AI as the tireless teammate**: "AI is the teammate who never gets tired of your questions. There are no dumb questions. It's the cheapest senior engineer out there."
- **Keynote code vs. slop code**: She advocates shipping "keynote code" (the term the industry is using for high-quality AI-generated code) rather than slop code, especially in a codebase that pays your salary.
- **Sentry is a full observability platform**: Beyond error and performance monitoring, Sentry now includes metrics, profiling, and agentic monitoring tools.

### Sentry AI Tools
- **Abacus**: Internal tool to track AI usage at Sentry
- **Warden**: A code review agent that operates on PRs
- **Junior**: A Slack bot that analyzes threads where bugs or UI issues are reported, then creates PRs to fix them
- **AI SDK Testing Repository**: A Sentry repository for testing AI integrations; contributors are instructed to only prompt, never code directly

### The Comprehension Skill in Practice
- Priscila demonstrated using "Catch Me Up" on a new repository where she was told not to code. She prompted: "I am a new contributor. Catch me up on how this repository works and clarify what it simulates a Sentry envelope and intercepts it during tests."
- The skill provided a summary, a flow diagram showing how things work, and specifically answered her question: does it simulate envelopes? No, it intercepts real ones.
- She also uses the skill to review colleagues' PRs when she has context but not enough to approve confidently.

## Related
- [[Priscila Andre de Oliveira]] — speaker, Senior Software Engineer at Sentry
- [[Sentry]] — employer, full observability platform
- [[AI Comprehension]] — core concept: 67% of AI usage is comprehension
- [[Catch Me Up Skill]] — the custom Claude skill she built
- [[AI Usage Tracking]] — tracking and categorizing your own AI prompts
- [[Agent Manager]] — her self-given title, managing AI agents
- [[Verdaccio]] — open-source NPM registry she maintains
- [[Vienna JS]] — JavaScript meetup in Vienna she co-organizes
- [[ClaudeCode]] — the AI coding agent she uses daily
- [[JakeNations]] — referenced for three-phase approach
- [[ThreePhaseApproach]] — methodology she critiques as missing a comprehension step
- [[ArminRonacher]] — quoted on not knowing your own codebase
- [[VibeCoding]] — referenced as context for the industry shift
- [[Keynote Code]] — term for high-quality AI-generated code (vs slop)
- [[Quality Quarter]] — Sentry's three-month technical debt cleanup
- [[aiDotEngineer]] — event host
