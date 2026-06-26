---
title: "AI SDK"
type: entity
category: tool
---

# AI SDK

## Definition

The AI SDK (Vercel AI SDK) is a TypeScript toolkit by Vercel for building AI-powered applications. It provides primitives like `streamText`, `Agent`, `useChat`, and tool integration for creating AI agents and chat interfaces.

## Key Information

- **Creator**: Vercel
- **Type**: TypeScript library
- **Key Components**:
  - `streamText` — Core function for streaming LLM responses
  - `Agent` — Agent class that loops between LLM calls and tool calls
  - `useChat` — React hook for consuming chat streams in the frontend
  - Tool definitions with Zod schemas for input validation
- **Integration**: Works with the Workflow DevKit via the `DurableAgent` class, which wraps `Agent` with `use step` markers on LLM calls
- **Usage**: Used as the foundation for the coding agent demo in Peter Wielander's presentation

## Related

- [[Vercel]]
- [[WorkflowDevKit]]
- [[NextJS]]
- [[DurableAgents]]
- [[WorkflowPattern]]
