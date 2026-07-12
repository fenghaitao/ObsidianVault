---
title: "Context as Key to Agent Success"
type: concept
tags: [AI, agents, best-practice, development, debugging]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"]
last_updated: 2026-07-10
---

## Definition

"Context as Key to Agent Success" is the observation that when AI coding agents fail to do what you want, it's usually a problem of context and underspecification rather than a model capability issue. The fix is to encode tribal knowledge into the codebase through documentation, code comments, code structure, and additional resource files.

## Key Information

- Discovered by the internal OpenAI team maintaining a 100% Codex-written codebase
- When the agent can't do something, the problem is usually: you've underspecified the task, or there's not enough information available to the agent about how to do it
- The solution: add documentation, encode tribal knowledge into the codebase via code comments, code structure, MD files, and skills files
- This is a key paradigm shift from "the model isn't good enough" to "I haven't given it enough context"
- The 100% Codex codebase team has no escape hatch to manually write code — they must solve problems through better context
- Best practices emerging from this experiment include extensive markdown documentation, clear code structure conventions, and skills files
- This insight generalizes beyond coding: any AI agent's effectiveness is bounded by the context and information you provide

## Related

- [[AI-Native Codebase]] — the practice of structuring codebases for AI agents
- [[Codex]] — the agent used in the 100% codebase experiment
- [[Sherwin Wu]] — shared the insight
- [[summary-26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu]] — source summary
