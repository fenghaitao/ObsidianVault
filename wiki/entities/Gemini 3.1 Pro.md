---
title: "Gemini 3.1 Pro"
type: entity
tags: [model, google, deepmind, gemini, large-model]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar.md"]
last_updated: 2026-06-30
---

## Definition
Gemini 3.1 Pro is the largest model in Google DeepMind's Gemini 3.1 series, offering the highest capability at a higher cost and slower speed. It is used by Augment Code and Replit as the default model for their AI agent systems. In Sonar's LLM code quality evaluation, Gemini 3.1 Pro High scored the highest SWE-bench pass rate (84.17%) among 53+ models while maintaining relatively concise code generation.

## Key Information
- Largest and most capable model in the Gemini 3.1 series
- More expensive and slower than Flash and Flash Light variants
- Augment Code defaults to Gemini 3.1 Pro for performance and cost reasons in their agent system
- Replit also defaults to Gemini 3.1 Pro for their agent system
- Supports multimodal inputs (video, images, audio, text, code) and outputs (text, code, audio, images)
- Used in AI Studio's "Build" feature for app creation with databases and authentication
- **Sonar evaluation (Gemini 3.1 Pro High)**: 84.17% SWE-bench pass rate (accuracy leader), 307K LOC (relatively concise), 234 cyclomatic complexity, 614 bugs/M LOC, 210 security issues/M LOC — evaluated February 19th on 4,444+ Java assignments

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20260531 - Can LLMs generate Enterprise Quality Code — Prasenjit Sarkar, Sonar]] — source
- [[Google DeepMind]] — creator
- [[Gemini 3.1 Flash Live]] — real-time sibling
- [[Gemini 3.1 Flash Light]] — smaller sibling
- [[Augment Code]] — user
- [[Replit]] — user
- [[Sonar Leaderboard]] — code quality evaluation
- [[LLM Code Quality Evaluation]] — evaluation framework
- [[SWE-bench]] — benchmark used for pass rate
