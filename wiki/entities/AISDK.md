---
title: "AI SDK"
type: entity
category: tool
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

# AI SDK

## Definition

The AI SDK (Vercel AI SDK) is a TypeScript toolkit by Vercel for building AI-powered applications. It provides primitives like `streamText`, `ToolLoopAgent`, `useChat`, and tool integration for creating AI agents and chat interfaces. Version 6 introduces an object-oriented agent approach with end-to-end type safety, global provider pattern, and structured lifecycle callbacks. It has over 10 million downloads per week.

## Key Information

- **Creator**: Vercel
- **Lead**: Last Gammel (based in Berlin), nicknamed "the mastermind behind the AI SDK"
- **Scale**: Over 10 million downloads per week (as of April 2026)
- **Type**: TypeScript library, platform-agnostic (Next.js, Bun, any JS runtime)
- **Key Components (v6)**:
  - `ToolLoopAgent` — Object-oriented agent primitive that encapsulates model, instructions, tools, and call options into a reusable definition. Separates agent definition from streaming concerns.
  - `streamText` / `generateText` — Core functions for LLM interaction; now support structured outputs natively
  - `useChat` — React hook for consuming chat streams in the frontend
  - Tool definitions with Zod schemas for input validation
  - **Global Provider**: Default AI Gateway provider; models specifiable as plain strings (`"gpt-5-4-mini"`). Overridable with any provider instance.
  - **Call Options Schema**: Zod schema for structured, type-safe inputs passed at call time (sandbox, customer ID, model selection)
  - **Agent Runtime Context**: React-context-like pattern for sharing state across tool executions within an agent run
  - **Prepare Call / Prepare Step**: Lifecycle callbacks for agent invocation setup and per-step context manipulation
  - **End-to-End Type Safety**: `InferAgentUIMessage` creates fully typed messages flowing from agent definition through route handlers to UI components
  - **Three Tool Types**: Custom tools, provider-defined tools, provider-executed tools
  - `createAgentUIStreamResponse` — Handles streaming response from agent to UI
- **v4 Legacy**: `generateText`, `streamText`, `generateObject`, `streamObject` still exist but structured outputs are now pushed into text generation functions
- **Integration**: Works with the Workflow DevKit via the `DurableAgent` class, which wraps `Agent` with `use step` markers on LLM calls
- **Open Code**: Built on AI SDK
- **Significance**: Cited by Malte Ubl as evidence of Europe's leadership in AI engineering innovation

## Related

- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source (v6 features)
- [[Vercel]]
- [[Last Gammel]] — lead developer
- [[NicoAlbanese]] — AI SDK developer
- [[WorkflowDevKit]]
- [[NextJS]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[Tool Loop Agent]] — v6 agent primitive
- [[Call Options Schema]] — v6 pattern
- [[Agent Runtime Context]] — v6 pattern
- [[Prepare Call]] — v6 lifecycle callback
- [[Prepare Step]] — v6 lifecycle callback
- [[Provider-Executed Tools]] — v6 tool type
- [[End-to-End Type Safety in Agents]] — v6 type system
