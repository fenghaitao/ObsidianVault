---
title: "Web Shell Pattern"
type: concept
tags: [testing, electron, desktop-app, ci, web, rapid-iteration, pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md"]
last_updated: 2026-06-29
---

## Definition
The Web Shell Pattern is a technique for converting an Electron desktop app's front-end (render process) into a standalone web application by abstracting system APIs to fall back to web standards. This enables rapid parallel testing of feature variants via PR preview links, dramatically speeding up development iteration for desktop applications.

## Key Information
- **Problem solved**: Desktop apps can only run one instance at a time, creating friction for testing multiple feature variants in parallel; coworkers must install dependencies locally to test changes
- **Architecture**: The Electron render process (front-end) is made agnostic of Electron by abstracting IPC (Inter-Process Communication) APIs to fall back to web standards when running in a web environment
- **React adaptation**: React routers, sessions, and query layers are moved to web standards so the render process runs independently
- **CI integration**: Every PR generates a preview link deployed online, enabling anyone to test changes instantly without local setup
- **LLM self-verification**: Once preview links exist, LLMs (e.g., Cursor) can go into the preview, test features, and upload screenshots into PRs, automating QA
- **Variant testing**: Enables testing one feature in multiple different variants simultaneously, so teams experience products in practice rather than just seeing them in Figma
- **Granola's implementation**: Turned their Electron meeting notes app into a web shell, which significantly sped up development time and enabled parallel variant testing
- **Implementation simplicity**: Despite appearing complex, the approach is relatively simple — just abstracting IPC APIs and moving React infrastructure to web standards

## Related
- [[Granola]] — company that implemented this pattern
- [[Electron]] — desktop framework the pattern is applied to
- [[Product Feedback Loops]] — the testing half of Granola's feedback loop
- [[Mehedi Hassan]] — speaker who described this pattern
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — source transcript
