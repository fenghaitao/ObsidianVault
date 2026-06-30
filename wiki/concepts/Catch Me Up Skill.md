---
title: "Catch Me Up Skill"
type: concept
tags: [ai, skills, claude, comprehension, code-understanding]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry.md"
last_updated: 2026-06-30
---

## Definition
"Catch Me Up" is a custom Claude skill created by Priscila Andre de Oliveira that structures codebase comprehension queries into six exploration modes. It is a locally-stored markdown file with detailed prompts and clear goals, designed to help developers rapidly understand unfamiliar codebases. The skill emphasizes visual output (organograms, tables, flow diagrams) to aid understanding.

## Key Information
- Created by [[Priscila Andre de Oliveira]] based on the observation that her AI prompts kept repeating comprehension patterns
- A skill is a detailed prompt in a markdown file with clear goals — human language, not code
- Six exploration modes:
  - **Architecture** — how the system is organized, component relationships
  - **Convention** — coding patterns, lint rules, naming standards
  - **Feature Trace** — following a specific feature through the codebase
  - **Syntax** — language-specific constructs and patterns
  - **Testing** — how tests are structured, run, and what patterns are used
  - **History** — git blame analysis, why changes were made, context behind decisions
- Produces visual outputs: organograms, tables, flow diagrams (designed for visual, frontend-oriented developers)
- Used for: onboarding to new repositories, reviewing colleagues' PRs with full context, understanding complex systems before making changes
- Example usage: "I am a new contributor. Catch me up on how this repository works and clarify what it simulates a Sentry envelope and intercepts it during tests."
- The skill answered specific questions precisely: "Does it simulate envelopes? No, it intercepts real ones."
- Stored locally on the user's computer; can be shared with others if desired

## Related
- [[summary-20260527 - The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry]] — source transcript
- [[Priscila Andre de Oliveira]] — creator
- [[AI Comprehension]] — the broader concept this skill enables
- [[Agent Skills]] — the general concept of AI agent skills
- [[ClaudeCode]] — the platform this skill is built for
- [[AI Usage Tracking]] — the analysis that led to this skill's creation
