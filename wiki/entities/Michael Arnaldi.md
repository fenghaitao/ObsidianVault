---
title: "Michael Arnaldi"
type: entity
tags: [person, effect, effectful, typescript, library-author, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

Michael Arnaldi is the creator of the Effect TypeScript library and founder of Effectful. He presented at aiDotEngineer on "vibe engineering" — building applications with AI from scratch using the Effect library.

## Key Information

- Creator of Effect, a TypeScript library for building type-safe, composable applications
- Founder of Effectful, the company behind Effect
- Has not written code by hand since approximately late summer 2025 — all coding done via AI
- Started programming at age 12
- Primarily does library-level coding (low-level type machinery) in both TypeScript and Rust
- Uses GPT 5.4 as his primary model; previously used Claude Sonnet 4
- Switched from Anthropic to OpenAI models after Anthropic restricted usage of open-source coding agents like OpenCode
- Maintains a repository called "accountability" with extensive custom ESLint rules to constrain AI behavior
- Developed the "clone the repo" pattern: giving AI access to library source code as a git subtree is more effective than documentation or MCP servers
- Advocates for generating per-model pattern files since GPT and Claude respond differently to prompting styles
- Uses Ralph loops (simple bash scripts running iterative agent tasks) for context management
- Prefers lowercase prompts for GPT models (they "get scared" by uppercase) and uppercase for Claude models

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Effect]] — TypeScript library he created
- [[Effectful]] — his company
- [[Clone the Repo Pattern]] — his core technique
- [[Vibe Engineering]] — his development approach
- [[Back Pressure Loop]] — his ESLint-based AI guardrail pattern
- [[Model Prompting Styles]] — his observations on GPT vs Claude
