---
title: "AI SDK"
type: entity
category: tool
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md"]
last_updated: 2026-06-26
---

# AI SDK

## Definition

The AI SDK (Vercel AI SDK) is a TypeScript toolkit by Vercel for building AI-powered applications. It provides primitives like `streamText`, `Agent`, `useChat`, and tool integration for creating AI agents and chat interfaces. It has over 10 million downloads per week.

## Key Information

- **Creator**: Vercel
- **Lead**: Last Gammel (based in Berlin)
- **Scale**: Over 10 million downloads per week (as of April 2026)
- **Type**: TypeScript library
- **Key Components**:
  - `streamText` — Core function for streaming LLM responses
  - `Agent` — Agent class that loops between LLM calls and tool calls
  - `useChat` — React hook for consuming chat streams in the frontend
  - Tool definitions with Zod schemas for input validation
- **Integration**: Works with the Workflow DevKit via the `DurableAgent` class, which wraps `Agent` with `use step` markers on LLM calls
- **Usage**: Used as the foundation for the coding agent demo in Peter Wielander's presentation
- **Significance**: Cited by Malte Ubl as evidence of Europe's leadership in AI engineering innovation

## Related

- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source
- [[Vercel]]
- [[Last Gammel]] — lead developer
- [[WorkflowDevKit]]
- [[NextJS]]
- [[DurableAgents]]
- [[WorkflowPattern]]
