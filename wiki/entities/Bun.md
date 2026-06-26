---
title: "Bun"
type: entity
tags: [tool, javascript-runtime, typescript, prototyping]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Bun is a fast JavaScript runtime and toolkit that includes built-in TypeScript compilation, making it ideal for rapid prototyping without a separate compile step. Used by Thariq Shihipar for agent prototyping in the Claude Agent SDK workshop.

## Key Information
- Preferred for prototyping because it eliminates the TypeScript-to-JavaScript compilation step, simplifying the agent's workflow
- Has linting built in, further reducing toolchain complexity for agents
- Used in the workshop to run chat.ts for the tool-calling agent demo and for the Agent SDK agent script
- The choice of Bun over Node.js was deliberate: TypeScript is better for code generation (types), and Bun removes the compile burden

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[CodeGenerationForNonCoding]] — Bun simplifies the code generation workflow
